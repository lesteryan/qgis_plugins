# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MapToolKit
                                 A QGIS plugin
 lesteryan map tool kit
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-04-26
        git sha              : $Format:%H$
        copyright            : (C) 2023 by lesteryan
        email                : cgmsyx@163.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *
# from QtCore.Qt import DockWidgetArea
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .mtk_dock_widget import MapToolKitDockWidget
import os.path
import time
import random
from shapely import wkt, wkb
import urllib
import json
from typing import Tuple, List

from .core.NdsUtil import NdsUtil
from .core.QgsCoordTrans import QgsCoordTrans


class MapToolKit:
    """QGIS Plugin Implementation."""

    epsg_id_wgs84 = 'EPSG:4326'
    epsg_id_webmercator = 'EPSG:3857'
    crs_wgs84 = QgsCoordinateReferenceSystem(epsg_id_wgs84)
    crs_webmecator = QgsCoordinateReferenceSystem(epsg_id_webmercator)
    supported_coords = [QgsCoordTrans.COORD.COORD_WGS84, QgsCoordTrans.COORD.COORD_GCJ02, QgsCoordTrans.COORD.COORD_WEBMERCATOR]
    xyz_layers = {
        '': '',
        'amap vector':'http://webrd03.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
        'amap satelite':'https://webst03.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}',
        'osm vector':'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
        }
    first_start = True

    def __init__(self, iface : QgisInterface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
      
        self.task_manager = QgsApplication.taskManager()
        self.plugin_dir = os.path.dirname(__file__)

        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'MapToolKit_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        self.actions = []
        self.menu = self.tr(u'&MapToolKit')

    def tr(self, message):
        return QCoreApplication.translate('MapToolKit', message)

    def initGui(self):
        QgsMessageLog.logMessage(f'initGui {self.first_start}')
        self.first_start = False

        self.dlg = MapToolKitDockWidget()
        self.iface.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.dlg)

        self.widget = self.dlg.widget
        self.map_tool = None

        self.widget.combo_simple_coordstype.addItems(self.supported_coords)
        self.widget.combo_wkt_coordstype.addItems(self.supported_coords)
        self.widget.combo_geojson_coordstype.addItems(self.supported_coords)
        self.widget.combo_coords_a.addItems(self.supported_coords)
        self.widget.combo_coords_b.addItems(self.supported_coords)
        self.widget.combo_coords_a.setCurrentIndex(0)
        self.widget.combo_coords_b.setCurrentIndex(1)

        self.widget.combo_xyzlayer_layertype.addItems(list(self.xyz_layers.keys()))
        self.widget.combo_xyzlayer_layertype.currentIndexChanged.connect(self.combo_xyz_index_changed)
        self.widget.button_xyzlayer_draw.clicked.connect(self.button_xyz_layer_add_clicked)

        self.widget.button_draw_nds_wgs84.clicked.connect(self.button_draw_nds_wgs84_clicked)
        self.widget.button_draw_nds_gcj02.clicked.connect(self.button_draw_nds_gcj02_clicked)
        self.widget.button_get_bound_tile.clicked.connect(self.button_get_bound_tile_clicked)

        self.widget.button_draw_coordpick_point.clicked.connect(self.button_coordpick_point_cliked)
        self.widget.button_draw_coordpick_line.clicked.connect(self.button_coordpick_line_cliked)
        self.widget.button_draw_coordpick_polygon.clicked.connect(self.button_coordpick_polygon_cliked)

        self.widget.button_draw_wkt.clicked.connect(self.button_draw_wkt_clicked)
        self.widget.button_draw_wkb.clicked.connect(self.button_draw_wkb_clicked)

        self.widget.button_draw_geojson.clicked.connect(self.button_draw_geojson_clicked)

        self.widget.button_coordstrans_a2b.clicked.connect(self.button_coordtransform_a2b_clicked)
        self.widget.button_coordstrans_b2a.clicked.connect(self.button_coordtransform_b2a_clicked)

        self.widget.button_draw_point.clicked.connect(self.button_draw_point_clicked)
        self.widget.button_draw_line.clicked.connect(self.button_draw_line_clicked)
        self.widget.button_draw_polygon.clicked.connect(self.button_draw_polygon_clicked)

        self.canvas.extentsChanged.connect(self.handleLayerExtentChanged)

        # self.widget.pushButton_test.clicked.connect(self.click_test)

    def unload(self):
        self.iface.removeDockWidget(self.dlg)
        if self.map_tool is not None:
            self.canvas.unsetMapTool(self.map_tool)

    def button_coordpick_point_cliked(self):
        if self.map_tool is not None:
            self.map_tool.draw_finish_event.disconnect(self.coodinate_pick_finished)

        self.map_tool = DrawTool(self.canvas, QgsWkbTypes.PointGeometry)
        self.map_tool.draw_finish_event.connect(self.coodinate_pick_finished)
        self.canvas.setMapTool(self.map_tool)

    def button_coordpick_line_cliked(self):
        if self.map_tool is not None:
            self.map_tool.draw_finish_event.disconnect(self.coodinate_pick_finished)

        self.map_tool = DrawTool(self.canvas, QgsWkbTypes.LineGeometry)
        self.map_tool.draw_finish_event.connect(self.coodinate_pick_finished)
        self.canvas.setMapTool(self.map_tool)

    def button_coordpick_polygon_cliked(self):
        if self.map_tool is not None:
            self.map_tool.draw_finish_event.disconnect(self.coodinate_pick_finished)

        self.map_tool = DrawTool(self.canvas, QgsWkbTypes.PolygonGeometry)
        self.map_tool.draw_finish_event.connect(self.coodinate_pick_finished)
        self.canvas.setMapTool(self.map_tool)

    def coodinate_pick_finished(self, geometry: QgsGeometry):
        QgsMessageLog.logMessage(f'coodinate_pick_finished {geometry.asWkt()}')
            

    def handleLayerExtentChanged(self, layer = None):
        if self.canvas.scale() > 194089792:
            reply =  QMessageBox.question(self.dlg, 'tips', 'canvas scale too large, go to default zoom ?', QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.canvas.setExtent(QgsRectangle(12962995.7347147744148970,4853260.9332224922254682,12963803.4525721203535795,4853649.7979973917827010))

    def draw_nds_tile(self, layer_name: str, tileid_str: str, coords_sys: str):
        if(len(tileid_str) == 0):
            self.iface.messageBar().pushMessage("Error", "invalid nds string", level=Qgis.Critical)
            return 

        fields = QgsFields()
        fields.append(QgsField("tile_id", QVariant.Int))
        fields.append(QgsField("level", QVariant.Int))

        nds_layer = QgsVectorLayer(f'Polygon?crs={self.epsg_id_wgs84}', layer_name, 'memory')
        symbol = QgsFillSymbol.createSimple({'color': '#00000000', 'style': 'solid', 'outline_color': 'red', 'stroke_width': '1'})
        nds_layer.renderer().setSymbol(symbol)
        
        nds_layer.dataProvider().addAttributes(fields)
        nds_layer.updateFields()

        QgsProject.instance().addMapLayer(nds_layer)

        layer_settings = QgsPalLayerSettings()
        text_format = QgsTextFormat()
        text_format.setColor(QColor("red"))
        layer_settings.setFormat(text_format)
        layer_settings.fieldName = "tile_id"
        layer_settings.placement = QgsPalLayerSettings.AroundPoint
        layer_settings.enabled = True
        labels = QgsVectorLayerSimpleLabeling(layer_settings)

        nds_layer.setLabeling(labels)
        nds_layer.setLabelsEnabled(True)

        tiles = list(map(lambda x : int(x.strip()), tileid_str.strip().split(',')))
        for tileid in tiles:
            level = NdsUtil.get_tile_level(tileid)
            p = NdsUtil.get_tile_polygon_of_deg(tileid)
            points = list(map(lambda l : QgsPointXY(l[0], l[1]), p))
            polygon = QgsGeometry.fromPolygonXY([points])
            polygon = QgsCoordTrans.geometry_trans(polygon, coords_sys, QgsCoordTrans.COORD.COORD_WGS84)

            feature = QgsFeature()
            feature.setFields(fields)
            feature.setId(tileid)
            feature.setGeometry(polygon)
            feature.setAttribute('tile_id', tileid)
            feature.setAttribute('level', level)
            # polygon_feature.setSymbol(symbol)

            nds_layer.dataProvider().addFeature(feature)
        
        nds_layer.updateExtents()

    def button_draw_nds_wgs84_clicked(self):
        QgsMessageLog.logMessage(self.widget.text_tile_content.toPlainText())
        self.draw_nds_tile(self.widget.edit_tile_layer_name.text(), self.widget.text_tile_content.toPlainText(), QgsCoordTrans.COORD.COORD_WGS84)

    def button_draw_nds_gcj02_clicked(self):
        self.draw_nds_tile(self.widget.edit_tile_layer_name.text(), self.widget.text_tile_content.toPlainText(), QgsCoordTrans.COORD.COORD_GCJ02)

    def button_get_bound_tile_clicked(self):
        extent = self.iface.mapCanvas().extent()
        crs = self.iface.activeLayer().crs()
        if(crs.authid() != self.epsg_id_wgs84):
            transform = QgsCoordinateTransform(crs, QgsCoordinateReferenceSystem(self.epsg_id_wgs84), QgsProject.instance())
            extent = transform.transform(extent)
   
        x1, y1, x2, y2 = extent.xMinimum(), extent.yMinimum(), extent.xMaximum(), extent.yMaximum()
        level = self.widget.spin_tile_level.value()
        tile_ids = NdsUtil.get_bound_tileids(x1, y1, x2, y2, level)
        tile_ids_str = ','.join(list(map(str, tile_ids)))
        self.widget.text_tile_content.setPlainText(tile_ids_str)

    def combo_xyz_index_changed(self):
        xyz_name = self.widget.combo_xyzlayer_layertype.currentText()
        self.widget.label_xyz_server.setText(self.xyz_layers[xyz_name])

    def draw_geometry(self, layer_name: str, geometry: QgsGeometry):
        geom_type = self.wkbType2String(geometry)
        uri = f'{geom_type}?crs={self.epsg_id_wgs84}'

        QgsMessageLog.logMessage(f'{uri}')

        layer = QgsVectorLayer(uri, layer_name, 'memory')
        pr = layer.dataProvider()

        feature = QgsFeature()
        feature.setGeometry(geometry)
        pr.addFeature(feature)
        layer.updateExtents()
        QgsProject.instance().addMapLayer(layer)

    def wkbType2String(self, g: QgsGeometry) -> str:
        geometry = g.get()
        if isinstance(geometry, QgsPoint) or isinstance(geometry, QgsPointXY) or isinstance(geometry, QgsMultiPoint):
            return 'Point'
        elif isinstance(geometry, QgsLineString) or isinstance(geometry, QgsMultiLineString):
            return 'LineString'
        elif isinstance(geometry, QgsPolygon) or isinstance(geometry, QgsMultiPolygon):
            return 'Polygon'

        raise Exception(f'invalid geometry type {type(geometry)}')

    def button_draw_wkt_clicked(self):
        geom = QgsGeometry.fromWkt(self.widget.text_wkt_content.toPlainText())

        if geom is None or geom.isEmpty():
            self.iface.messageBar().pushMessage("Error", "invalid wkt string", level=Qgis.Critical)
            return 
    
        coord_type = self.widget.combo_wkt_coordstype.currentText()
        geom = QgsCoordTrans.geometry_trans(geom, coord_type, QgsCoordTrans.COORD.COORD_WGS84)
        layer_name = self.widget.edit_wkt_layer_name.text()
        self.draw_geometry(layer_name, geom)

    def button_draw_wkb_clicked(self):
        geom = QgsGeometry.fromWkb(bytearray.fromhex(self.widget.text_wkt_content.toPlainText()))
        coord_type = self.widget.combo_wkt_coordstype.currentText()
        geom = QgsCoordTrans.geometry_trans(geom, coord_type, QgsCoordTrans.COORD.COORD_WGS84)
        layer_name = self.widget.edit_wkt_layer_name.text()
        self.draw_geometry(layer_name, geom)

    def button_draw_geojson_clicked(self):
        features = QgsJsonUtils.stringToFeatureList(self.widget.text_geojson_content.toPlainText())
        coord_type = self.widget.combo_geojson_coordstype.currentText()
        features = QgsCoordTrans.features_trans(features, coord_type, QgsCoordTrans.COORD.COORD_WGS84)

        layer_name = self.widget.edit_geojson_layer_name.text()

        geom_type = self.wkbType2String(features[0].geometry())
        uri = f'{geom_type}?crs={self.epsg_id_wgs84}'
        layer = QgsVectorLayer(uri, layer_name, 'memory')
        pr = layer.dataProvider()

        # 添加字段和特征到 Layer 中
        for feature in features:
            pr.addFeatures([feature])

        layer.updateExtents()
        QgsProject.instance().addMapLayer(layer)

    # mode 0 point 1 line 2 polygone
    def draw(self, layer_name: str, coords_str: str, mode: int, coords_sys: str):
        coords = list(map(lambda x : float(x.strip()), coords_str.strip().split(',')))
        points = []
        for i in range(0, len(coords), 2):
            x, y = coords[i + 0], coords[i + 1]
            points.append(QgsPointXY(x, y))

        if mode == 0:
            geometry = QgsGeometry.fromMultiPointXY(points)
        elif mode == 1:
            geometry = QgsGeometry.fromPolylineXY(points)
        elif mode == 2:
            geometry = QgsGeometry.fromPolygonXY([points])

        geometry = QgsCoordTrans.geometry_trans(geometry, coords_sys, QgsCoordTrans.COORD.COORD_WGS84)

        if geometry is not None and not geometry.isEmpty():
            self.draw_geometry(layer_name, geometry)  

    def button_draw_point_clicked(self):
        layer_name = self.widget.edit_simple_layer_name.text()
        coords = self.widget.text_simple_content.toPlainText()
        coords_type = self.widget.combo_simple_coordstype.currentText()
        self.draw(layer_name, coords, 0, coords_type)

    def button_draw_line_clicked(self):
        layer_name = self.widget.edit_simple_layer_name.text()
        coords = self.widget.text_simple_content.toPlainText()
        coords_type = self.widget.combo_simple_coordstype.currentText()
        self.draw(layer_name, coords, 1, coords_type)

    def button_draw_polygon_clicked(self):
        layer_name = self.widget.edit_simple_layer_name.text()
        coords = self.widget.text_simple_content.toPlainText()
        coords_type = self.widget.combo_simple_coordstype.currentText()
        self.draw(layer_name, coords, 2, coords_type)

    def button_coordtransform_a2b_clicked(self):
        src_coords_sys = self.widget.combo_coords_a.currentText()
        dest_coords_sys = self.widget.combo_coords_b.currentText()
        coords_str = self.widget.text_coords_a.toPlainText()
        result_str = QgsCoordTrans.coords_transform(coords_str, src_coords_sys, dest_coords_sys)
        self.widget.text_coords_b.setPlainText(result_str)


    def button_coordtransform_b2a_clicked(self):
        src_coords_sys = self.widget.combo_coords_b.currentText()
        dest_coords_sys = self.widget.combo_coords_a.currentText()
        coords_str = self.widget.text_coords_b.toPlainText()
        result_str = QgsCoordTrans.coords_transform(coords_str, src_coords_sys, dest_coords_sys)
        self.widget.text_coords_a.setPlainText(result_str)

    def button_xyz_layer_add_clicked(self):
        layer_name = self.widget.combo_xyzlayer_layertype.currentText()
        layer_uri = self.widget.label_xyz_server.text()

        if layer_name is None or layer_uri is None :
            return 
        
        layer_uri = urllib.parse.quote(layer_uri)
        layer_uri = f'url={layer_uri}&type=xyz&zmax=18&zmin=0'
        QgsMessageLog.logMessage(layer_uri)
        layer = QgsRasterLayer(layer_uri, layer_name, "wms")

        QgsProject.instance().addMapLayer(layer)  

    def click_test(self):

        QgsMessageLog.logMessage(f'aoh.... {type(self.canvas.mapTool())}')


        # try:
        #     # QgsMessageLog.logMessage('click')
        #     # task1 : QgsTask = QgsTask.fromFunction('Waste cpu 1', self.mytask, on_finished=self.completed, arg1=3)
        #     # self.task_manager.addTask(task1)

        #     pass
        # except Exception:
        #     QgsMessageLog.logMessage('aoh....')

class DrawTool(QgsMapTool):
    draw_finish_event = pyqtSignal(QgsGeometry)

    def __init__(self, canvas: QgsMapCanvas, geometry_type: QgsWkbTypes):
        super().__init__(canvas)
        self.canvas = canvas
        self.geometry_type = geometry_type
        self.geometry_index = 0
        self.point_count = 0
        self.rubber_band = QgsRubberBand(self.canvas, self.geometry_type)
        self.rubber_band.setColor(QColor(0x112233))


    def reset(self):
        self.rubber_band.reset(self.geometry_type)

    def canvasPressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.point_count = self.point_count + 1
            point = self.toMapCoordinates(event.pos())
            self.rubber_band.addPoint(point, geometryIndex=self.geometry_index)
        elif event.button() == QtCore.Qt.RightButton:
            if self.point_count == 0:
                self.deactivate()
            else:
                self.geometry_index = self.geometry_index + 1
                self.point_count = 0
            # QgsMessageLog.logMessage(f'right {self.rubber_band.numberOfVertices()}')
            # self.rubber_band.closePoints(True, self.rubber_band.numberOfVertices())

    # def canvasReleaseEvent(self, event):
    #     QgsMessageLog.logMessage('canvasReleaseEvent')
    #     if event.button() == QtCore.Qt.RightButton:
    #         geom = self.rubber_band.asGeometry()
    #         self.draw_finish_event.emit(geom)

    #         self.reset()

    def deactivate(self):
        geom = self.rubber_band.asGeometry()
        self.draw_finish_event.emit(geom)

        self.reset()
        super().deactivate()
        
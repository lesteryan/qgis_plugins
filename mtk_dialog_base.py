# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mtk_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MapToolKitDialogBase(object):
    def setupUi(self, MapToolKitDialogBase):
        MapToolKitDialogBase.setObjectName("MapToolKitDialogBase")
        MapToolKitDialogBase.resize(473, 341)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MapToolKitDialogBase.sizePolicy().hasHeightForWidth())
        MapToolKitDialogBase.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MapToolKitDialogBase)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabwidget = QtWidgets.QTabWidget(MapToolKitDialogBase)
        self.tabwidget.setObjectName("tabwidget")
        self.tab_simple = QtWidgets.QWidget()
        self.tab_simple.setObjectName("tab_simple")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_simple)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.text_simple_content = QtWidgets.QPlainTextEdit(self.tab_simple)
        self.text_simple_content.setObjectName("text_simple_content")
        self.verticalLayout_6.addWidget(self.text_simple_content)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.tab_simple)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.edit_simple_layer_name = QtWidgets.QLineEdit(self.tab_simple)
        self.edit_simple_layer_name.setObjectName("edit_simple_layer_name")
        self.horizontalLayout_10.addWidget(self.edit_simple_layer_name)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_draw_wgs84_point = QtWidgets.QPushButton(self.tab_simple)
        self.button_draw_wgs84_point.setObjectName("button_draw_wgs84_point")
        self.gridLayout.addWidget(self.button_draw_wgs84_point, 1, 0, 1, 1)
        self.button_draw_wgs84_line = QtWidgets.QPushButton(self.tab_simple)
        self.button_draw_wgs84_line.setObjectName("button_draw_wgs84_line")
        self.gridLayout.addWidget(self.button_draw_wgs84_line, 1, 1, 1, 1)
        self.button_draw_gcj02_point = QtWidgets.QPushButton(self.tab_simple)
        self.button_draw_gcj02_point.setObjectName("button_draw_gcj02_point")
        self.gridLayout.addWidget(self.button_draw_gcj02_point, 2, 0, 1, 1)
        self.button_draw_gcj02_line = QtWidgets.QPushButton(self.tab_simple)
        self.button_draw_gcj02_line.setObjectName("button_draw_gcj02_line")
        self.gridLayout.addWidget(self.button_draw_gcj02_line, 2, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.tabwidget.addTab(self.tab_simple, "")
        self.tab_tile = QtWidgets.QWidget()
        self.tab_tile.setObjectName("tab_tile")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_tile)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_tile_content = QtWidgets.QPlainTextEdit(self.tab_tile)
        self.text_tile_content.setObjectName("text_tile_content")
        self.verticalLayout_3.addWidget(self.text_tile_content)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.tab_tile)
        self.label.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.spin_tile_level = QtWidgets.QSpinBox(self.tab_tile)
        self.spin_tile_level.setMinimum(1)
        self.spin_tile_level.setMaximum(15)
        self.spin_tile_level.setProperty("value", 13)
        self.spin_tile_level.setObjectName("spin_tile_level")
        self.horizontalLayout_4.addWidget(self.spin_tile_level)
        self.button_get_bound_tile = QtWidgets.QPushButton(self.tab_tile)
        self.button_get_bound_tile.setObjectName("button_get_bound_tile")
        self.horizontalLayout_4.addWidget(self.button_get_bound_tile)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab_tile)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.edit_tile_layer_name = QtWidgets.QLineEdit(self.tab_tile)
        self.edit_tile_layer_name.setObjectName("edit_tile_layer_name")
        self.horizontalLayout_5.addWidget(self.edit_tile_layer_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_draw_nds_wgs84 = QtWidgets.QPushButton(self.tab_tile)
        self.button_draw_nds_wgs84.setObjectName("button_draw_nds_wgs84")
        self.horizontalLayout_3.addWidget(self.button_draw_nds_wgs84)
        self.button_draw_nds_gcj02 = QtWidgets.QPushButton(self.tab_tile)
        self.button_draw_nds_gcj02.setObjectName("button_draw_nds_gcj02")
        self.horizontalLayout_3.addWidget(self.button_draw_nds_gcj02)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tabwidget.addTab(self.tab_tile, "")
        self.tab_geom = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_geom.sizePolicy().hasHeightForWidth())
        self.tab_geom.setSizePolicy(sizePolicy)
        self.tab_geom.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.tab_geom.setObjectName("tab_geom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_geom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text_wkt_content = QtWidgets.QPlainTextEdit(self.tab_geom)
        self.text_wkt_content.setObjectName("text_wkt_content")
        self.verticalLayout_2.addWidget(self.text_wkt_content)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab_geom)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.edit_wkt_layer_name = QtWidgets.QLineEdit(self.tab_geom)
        self.edit_wkt_layer_name.setObjectName("edit_wkt_layer_name")
        self.horizontalLayout_2.addWidget(self.edit_wkt_layer_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.button_draw_wkt = QtWidgets.QPushButton(self.tab_geom)
        self.button_draw_wkt.setObjectName("button_draw_wkt")
        self.horizontalLayout_6.addWidget(self.button_draw_wkt)
        self.button_draw_wkb = QtWidgets.QPushButton(self.tab_geom)
        self.button_draw_wkb.setObjectName("button_draw_wkb")
        self.horizontalLayout_6.addWidget(self.button_draw_wkb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tabwidget.addTab(self.tab_geom, "")
        self.tab_geojson = QtWidgets.QWidget()
        self.tab_geojson.setObjectName("tab_geojson")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_geojson)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.text_geojson_content = QtWidgets.QPlainTextEdit(self.tab_geojson)
        self.text_geojson_content.setObjectName("text_geojson_content")
        self.verticalLayout_4.addWidget(self.text_geojson_content)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.tab_geojson)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.edit_geojson_layer_name = QtWidgets.QLineEdit(self.tab_geojson)
        self.edit_geojson_layer_name.setObjectName("edit_geojson_layer_name")
        self.horizontalLayout_8.addWidget(self.edit_geojson_layer_name)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_draw_geojson = QtWidgets.QPushButton(self.tab_geojson)
        self.button_draw_geojson.setObjectName("button_draw_geojson")
        self.horizontalLayout_9.addWidget(self.button_draw_geojson)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.tabwidget.addTab(self.tab_geojson, "")
        self.tab_coordtransform = QtWidgets.QWidget()
        self.tab_coordtransform.setObjectName("tab_coordtransform")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_coordtransform)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.tab_coordtransform)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.text_coords_wgs84 = QtWidgets.QPlainTextEdit(self.tab_coordtransform)
        self.text_coords_wgs84.setObjectName("text_coords_wgs84")
        self.verticalLayout_9.addWidget(self.text_coords_wgs84)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.button_coordstrans_gcj02_to_wgs84 = QtWidgets.QPushButton(self.tab_coordtransform)
        self.button_coordstrans_gcj02_to_wgs84.setObjectName("button_coordstrans_gcj02_to_wgs84")
        self.verticalLayout_7.addWidget(self.button_coordstrans_gcj02_to_wgs84)
        self.button_coordstrans_wgs84_to_gcj02 = QtWidgets.QPushButton(self.tab_coordtransform)
        self.button_coordstrans_wgs84_to_gcj02.setObjectName("button_coordstrans_wgs84_to_gcj02")
        self.verticalLayout_7.addWidget(self.button_coordstrans_wgs84_to_gcj02)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.tab_coordtransform)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.text_coords_gcj02 = QtWidgets.QPlainTextEdit(self.tab_coordtransform)
        self.text_coords_gcj02.setObjectName("text_coords_gcj02")
        self.verticalLayout_8.addWidget(self.text_coords_gcj02)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.tabwidget.addTab(self.tab_coordtransform, "")
        self.tab_about = QtWidgets.QWidget()
        self.tab_about.setObjectName("tab_about")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_about)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.tab_about)
        self.label_5.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_5.setWordWrap(True)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.tabwidget.addTab(self.tab_about, "")
        self.verticalLayout.addWidget(self.tabwidget)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(MapToolKitDialogBase)
        self.tabwidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MapToolKitDialogBase)

    def retranslateUi(self, MapToolKitDialogBase):
        _translate = QtCore.QCoreApplication.translate
        MapToolKitDialogBase.setWindowTitle(_translate("MapToolKitDialogBase", "MapToolKit"))
        self.text_simple_content.setPlainText(_translate("MapToolKitDialogBase", "116.43903117075563,39.91104010187582,116.43901342113355,39.91150480496536,116.43943805910575,39.911054391124026,116.43942031257961,39.911492021957876"))
        self.label_8.setText(_translate("MapToolKitDialogBase", "layer name"))
        self.edit_simple_layer_name.setText(_translate("MapToolKitDialogBase", "simple_layer_1"))
        self.button_draw_wgs84_point.setText(_translate("MapToolKitDialogBase", "draw wgs84 point"))
        self.button_draw_wgs84_line.setText(_translate("MapToolKitDialogBase", "draw wgs84 line"))
        self.button_draw_gcj02_point.setText(_translate("MapToolKitDialogBase", "draw gcj02 point"))
        self.button_draw_gcj02_line.setText(_translate("MapToolKitDialogBase", "draw gcj02 line"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_simple), _translate("MapToolKitDialogBase", "simple"))
        self.text_tile_content.setPlainText(_translate("MapToolKitDialogBase", "557005127,557005138,557005139,557005133,557005144,557005145,557005135,557005146,557005147"))
        self.label.setText(_translate("MapToolKitDialogBase", "level"))
        self.button_get_bound_tile.setText(_translate("MapToolKitDialogBase", "get bound tile"))
        self.label_2.setText(_translate("MapToolKitDialogBase", "layer name"))
        self.edit_tile_layer_name.setText(_translate("MapToolKitDialogBase", "nds_layer_1"))
        self.button_draw_nds_wgs84.setText(_translate("MapToolKitDialogBase", "draw wgs84 tile"))
        self.button_draw_nds_gcj02.setText(_translate("MapToolKitDialogBase", "draw gcj02 tile"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_tile), _translate("MapToolKitDialogBase", "nds tile"))
        self.text_wkt_content.setPlainText(_translate("MapToolKitDialogBase", "MULTILINESTRING((116.44522127226753 39.912404037289974, 116.44520362408929 39.91286879286403, 116.44562718036195 39.912417573904435, 116.44560953218377 39.912855256338304),(116.44630369384947 39.91289360982063, 116.44630663521292 39.912419830006485, 116.44658606469875 39.91242659831269, 116.44672430875875 39.912528122824426, 116.44658018197185 39.912686049543254, 116.44631251793982 39.912683793450014, 116.44658900605981 39.91268830563695, 116.44675666375173 39.91282592719065, 116.4465978301501 39.91290714633831, 116.44630663521292 39.91289812199335))"))
        self.label_3.setText(_translate("MapToolKitDialogBase", "layer name"))
        self.edit_wkt_layer_name.setText(_translate("MapToolKitDialogBase", "wkt_layer_1"))
        self.button_draw_wkt.setText(_translate("MapToolKitDialogBase", "draw wkt"))
        self.button_draw_wkb.setText(_translate("MapToolKitDialogBase", "draw wkb"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_geom), _translate("MapToolKitDialogBase", "wkt"))
        self.text_geojson_content.setPlainText(_translate("MapToolKitDialogBase", "{\n"
"  \"type\": \"FeatureCollection\",\n"
"  \"features\": [\n"
"    {\n"
"      \"type\": \"Feature\",\n"
"      \"properties\": {},\n"
"      \"geometry\": {\n"
"        \"coordinates\": [\n"
"          [\n"
"            116.44522127226753,\n"
"            39.912404037289974\n"
"          ],\n"
"          [\n"
"            116.44520362408929,\n"
"            39.91286879286403\n"
"          ],\n"
"          [\n"
"            116.44562718036195,\n"
"            39.912417573904435\n"
"          ],\n"
"          [\n"
"            116.44560953218377,\n"
"            39.912855256338304\n"
"          ]\n"
"        ],\n"
"        \"type\": \"LineString\"\n"
"      }\n"
"    },\n"
"    {\n"
"      \"type\": \"Feature\",\n"
"      \"properties\": {},\n"
"      \"geometry\": {\n"
"        \"coordinates\": [\n"
"          [\n"
"            116.44630369384947,\n"
"            39.91289360982063\n"
"          ],\n"
"          [\n"
"            116.44630663521292,\n"
"            39.912419830006485\n"
"          ],\n"
"          [\n"
"            116.44658606469875,\n"
"            39.91242659831269\n"
"          ],\n"
"          [\n"
"            116.44672430875875,\n"
"            39.912528122824426\n"
"          ],\n"
"          [\n"
"            116.44658018197185,\n"
"            39.912686049543254\n"
"          ],\n"
"          [\n"
"            116.44631251793982,\n"
"            39.912683793450014\n"
"          ],\n"
"          [\n"
"            116.44658900605981,\n"
"            39.91268830563695\n"
"          ],\n"
"          [\n"
"            116.44675666375173,\n"
"            39.91282592719065\n"
"          ],\n"
"          [\n"
"            116.4465978301501,\n"
"            39.91290714633831\n"
"          ],\n"
"          [\n"
"            116.44630663521292,\n"
"            39.91289812199335\n"
"          ]\n"
"        ],\n"
"        \"type\": \"LineString\"\n"
"      }\n"
"    }\n"
"  ]\n"
"}"))
        self.label_4.setText(_translate("MapToolKitDialogBase", "layer name"))
        self.edit_geojson_layer_name.setText(_translate("MapToolKitDialogBase", "geojson_layer_1"))
        self.button_draw_geojson.setText(_translate("MapToolKitDialogBase", "draw"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_geojson), _translate("MapToolKitDialogBase", "geojson"))
        self.label_7.setText(_translate("MapToolKitDialogBase", "wgs84"))
        self.button_coordstrans_gcj02_to_wgs84.setText(_translate("MapToolKitDialogBase", "<<"))
        self.button_coordstrans_wgs84_to_gcj02.setText(_translate("MapToolKitDialogBase", ">>"))
        self.label_6.setText(_translate("MapToolKitDialogBase", "gcj02"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_coordtransform), _translate("MapToolKitDialogBase", "coordtransform"))
        self.label_5.setText(_translate("MapToolKitDialogBase", "<html><head/><body><p><span style=\" font-size:36pt;\">MapToolKit</span><br/><br/></p><p><br/><span style=\" font-size:14pt;\">a plugin to view simple geometry data kit <br/></span></p><p><a href=\"https://github.com/users/lesteryan\"><span style=\" text-decoration: underline; color:#0068da;\">Source Code and Bug Tracker</span></a></p><p><span style=\" font-size:14pt;\">enjoy it! </span></p><p><span style=\" font-size:14pt;\">Made in China by </span><a href=\"cgmsyx@163.com\"><span style=\" text-decoration: underline; color:#0068da;\">lesteryan</span></a><span style=\" font-size:14pt;\"><br/><br/></span></p></body></html>"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_about), _translate("MapToolKitDialogBase", "about"))

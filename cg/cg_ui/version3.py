# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'version3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_cg_sector(object):
    def setupUi(self, cg_sector):
        cg_sector.setObjectName("cg_sector")
        cg_sector.resize(720, 623)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(cg_sector)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tabWidget = QtWidgets.QTabWidget(cg_sector)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.requisition_receipt_btn = PrimaryPushButton(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requisition_receipt_btn.sizePolicy().hasHeightForWidth())
        self.requisition_receipt_btn.setSizePolicy(sizePolicy)
        self.requisition_receipt_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.requisition_receipt_btn.setObjectName("requisition_receipt_btn")
        self.horizontalLayout_15.addWidget(self.requisition_receipt_btn)
        self.requisition_accept_btn = PrimaryPushButton(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requisition_accept_btn.sizePolicy().hasHeightForWidth())
        self.requisition_accept_btn.setSizePolicy(sizePolicy)
        self.requisition_accept_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.requisition_accept_btn.setObjectName("requisition_accept_btn")
        self.horizontalLayout_15.addWidget(self.requisition_accept_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.verticalLayout_13.addLayout(self.horizontalLayout_15)
        self.requisition_table_view = TableView(self.tab_1)
        self.requisition_table_view.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.requisition_table_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.requisition_table_view.setAlternatingRowColors(True)
        self.requisition_table_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.requisition_table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.requisition_table_view.setObjectName("requisition_table_view")
        self.verticalLayout_13.addWidget(self.requisition_table_view)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = StrongBodyLabel(self.tab_2)
        self.label_12.setMinimumSize(QtCore.QSize(96, 0))
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(518, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 2)
        self.order_search = PrimaryToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_search.sizePolicy().hasHeightForWidth())
        self.order_search.setSizePolicy(sizePolicy)
        self.order_search.setMinimumSize(QtCore.QSize(75, 26))
        self.order_search.setObjectName("order_search")
        self.gridLayout.addWidget(self.order_search, 1, 2, 1, 1)
        self.order_save = PrimaryToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_save.sizePolicy().hasHeightForWidth())
        self.order_save.setSizePolicy(sizePolicy)
        self.order_save.setMinimumSize(QtCore.QSize(75, 26))
        self.order_save.setObjectName("order_save")
        self.gridLayout.addWidget(self.order_save, 2, 2, 1, 1)
        self.order_add = ToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_add.sizePolicy().hasHeightForWidth())
        self.order_add.setSizePolicy(sizePolicy)
        self.order_add.setMinimumSize(QtCore.QSize(75, 26))
        self.order_add.setObjectName("order_add")
        self.gridLayout.addWidget(self.order_add, 3, 2, 1, 1)
        self.order_delete = ToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_delete.sizePolicy().hasHeightForWidth())
        self.order_delete.setSizePolicy(sizePolicy)
        self.order_delete.setMinimumSize(QtCore.QSize(75, 26))
        self.order_delete.setObjectName("order_delete")
        self.gridLayout.addWidget(self.order_delete, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 98, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 2, 1, 1)
        self.order_table_view = TableView(self.tab_2)
        self.order_table_view.setObjectName("order_table_view")
        self.gridLayout.addWidget(self.order_table_view, 1, 0, 5, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = StrongBodyLabel(self.tab_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)
        self.order_detail_id = LineEdit(self.tab_2)
        self.order_detail_id.setMinimumSize(QtCore.QSize(121, 0))
        self.order_detail_id.setMaximumSize(QtCore.QSize(121, 16777215))
        self.order_detail_id.setObjectName("order_detail_id")
        self.gridLayout_3.addWidget(self.order_detail_id, 0, 2, 1, 1)
        self.label_10 = StrongBodyLabel(self.tab_2)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 3, 1, 1)
        self.order_supplier = LineEdit(self.tab_2)
        self.order_supplier.setObjectName("order_supplier")
        self.gridLayout_3.addWidget(self.order_supplier, 0, 4, 1, 2)
        self.label_2 = StrongBodyLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 2)
        self.dateTimeEdit = DateTimeEdit(self.tab_2)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_3.addWidget(self.dateTimeEdit, 1, 2, 1, 1)
        self.label_7 = StrongBodyLabel(self.tab_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 3, 1, 2)
        self.order_receipt_box = LineEdit(self.tab_2)
        self.order_receipt_box.setObjectName("order_receipt_box")
        self.gridLayout_3.addWidget(self.order_receipt_box, 1, 5, 1, 1)
        self.label_8 = BodyLabel(self.tab_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.order_remarks = TextEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_remarks.sizePolicy().hasHeightForWidth())
        self.order_remarks.setSizePolicy(sizePolicy)
        self.order_remarks.setMinimumSize(QtCore.QSize(300, 0))
        self.order_remarks.setMaximumSize(QtCore.QSize(16777215, 100))
        self.order_remarks.setObjectName("order_remarks")
        self.gridLayout_3.addWidget(self.order_remarks, 2, 1, 1, 5)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = BodyLabel(self.tab_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.order_bom = LineEdit(self.tab_2)
        self.order_bom.setObjectName("order_bom")
        self.gridLayout_2.addWidget(self.order_bom, 0, 1, 1, 2)
        self.label_6 = BodyLabel(self.tab_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 2)
        self.order_price = LineEdit(self.tab_2)
        self.order_price.setMinimumSize(QtCore.QSize(96, 0))
        self.order_price.setObjectName("order_price")
        self.gridLayout_2.addWidget(self.order_price, 1, 2, 1, 1)
        self.label_9 = BodyLabel(self.tab_2)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 2)
        self.order_quantity = LineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_quantity.sizePolicy().hasHeightForWidth())
        self.order_quantity.setSizePolicy(sizePolicy)
        self.order_quantity.setMinimumSize(QtCore.QSize(96, 0))
        self.order_quantity.setObjectName("order_quantity")
        self.gridLayout_2.addWidget(self.order_quantity, 2, 2, 1, 1)
        self.label_11 = BodyLabel(self.tab_2)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 2)
        self.order_total_price = LineEdit(self.tab_2)
        self.order_total_price.setMinimumSize(QtCore.QSize(96, 0))
        self.order_total_price.setObjectName("order_total_price")
        self.gridLayout_2.addWidget(self.order_total_price, 3, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = StrongBodyLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(558, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 1, 1, 2)
        self.receive_table_view = TableView(self.tab_3)
        self.receive_table_view.setObjectName("receive_table_view")
        self.gridLayout_4.addWidget(self.receive_table_view, 1, 0, 5, 2)
        self.receive_search = PrimaryPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receive_search.sizePolicy().hasHeightForWidth())
        self.receive_search.setSizePolicy(sizePolicy)
        self.receive_search.setMinimumSize(QtCore.QSize(75, 26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/.designer/backup/python/pyQT-sqlite-gui/icons/sc_refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.receive_search.setIcon(icon)
        self.receive_search.setObjectName("receive_search")
        self.gridLayout_4.addWidget(self.receive_search, 1, 2, 1, 1)
        self.receive_save = PrimaryPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receive_save.sizePolicy().hasHeightForWidth())
        self.receive_save.setSizePolicy(sizePolicy)
        self.receive_save.setMinimumSize(QtCore.QSize(75, 26))
        self.receive_save.setIcon(icon)
        self.receive_save.setObjectName("receive_save")
        self.gridLayout_4.addWidget(self.receive_save, 2, 2, 1, 1)
        self.receive_add = PushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receive_add.sizePolicy().hasHeightForWidth())
        self.receive_add.setSizePolicy(sizePolicy)
        self.receive_add.setMinimumSize(QtCore.QSize(75, 26))
        self.receive_add.setIcon(icon)
        self.receive_add.setObjectName("receive_add")
        self.gridLayout_4.addWidget(self.receive_add, 3, 2, 1, 1)
        self.receive_delete = PushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receive_delete.sizePolicy().hasHeightForWidth())
        self.receive_delete.setSizePolicy(sizePolicy)
        self.receive_delete.setMinimumSize(QtCore.QSize(75, 26))
        self.receive_delete.setIcon(icon)
        self.receive_delete.setObjectName("receive_delete")
        self.gridLayout_4.addWidget(self.receive_delete, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 168, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 5, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_17 = StrongBodyLabel(self.tab_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 1)
        self.receive_id = LineEdit(self.tab_3)
        self.receive_id.setObjectName("receive_id")
        self.gridLayout_5.addWidget(self.receive_id, 0, 1, 1, 1)
        self.label_13 = StrongBodyLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)
        self.receive_item = LineEdit(self.tab_3)
        self.receive_item.setObjectName("receive_item")
        self.gridLayout_5.addWidget(self.receive_item, 1, 1, 1, 1)
        self.label_18 = StrongBodyLabel(self.tab_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 2, 0, 1, 1)
        self.receive_time = DateTimeEdit(self.tab_3)
        self.receive_time.setObjectName("receive_time")
        self.gridLayout_5.addWidget(self.receive_time, 2, 1, 1, 1)
        self.label_19 = StrongBodyLabel(self.tab_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 3, 0, 1, 1)
        self.receive_quantity = LineEdit(self.tab_3)
        self.receive_quantity.setObjectName("receive_quantity")
        self.gridLayout_5.addWidget(self.receive_quantity, 3, 1, 1, 1)
        self.label_20 = StrongBodyLabel(self.tab_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 4, 0, 1, 1)
        self.receive_qualified = LineEdit(self.tab_3)
        self.receive_qualified.setObjectName("receive_qualified")
        self.gridLayout_5.addWidget(self.receive_qualified, 4, 1, 1, 1)
        self.label_21 = StrongBodyLabel(self.tab_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 5, 0, 1, 1)
        self.receive_status = CheckBox(self.tab_3)
        self.receive_status.setObjectName("receive_status")
        self.gridLayout_5.addWidget(self.receive_status, 5, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_22 = BodyLabel(self.tab_3)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 0, 0, 1, 1)
        self.receive_btn = PrimaryPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receive_btn.sizePolicy().hasHeightForWidth())
        self.receive_btn.setSizePolicy(sizePolicy)
        self.receive_btn.setMinimumSize(QtCore.QSize(75, 26))
        self.receive_btn.setObjectName("receive_btn")
        self.gridLayout_6.addWidget(self.receive_btn, 1, 0, 1, 1)
        self.receive_remarks = TextEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receive_remarks.sizePolicy().hasHeightForWidth())
        self.receive_remarks.setSizePolicy(sizePolicy)
        self.receive_remarks.setMaximumSize(QtCore.QSize(300, 150))
        self.receive_remarks.setObjectName("receive_remarks")
        self.gridLayout_6.addWidget(self.receive_remarks, 0, 1, 2, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = StrongBodyLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(60, 30))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.supplier_choose_box = ComboBox(self.tab_4)
        self.supplier_choose_box.setMinimumSize(QtCore.QSize(151, 30))
        self.supplier_choose_box.setMaximumSize(QtCore.QSize(16777215, 30))
        self.supplier_choose_box.setObjectName("supplier_choose_box")
        self.horizontalLayout.addWidget(self.supplier_choose_box)
        spacerItem5 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem6 = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem6)
        self.supplier_location = BodyLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supplier_location.sizePolicy().hasHeightForWidth())
        self.supplier_location.setSizePolicy(sizePolicy)
        self.supplier_location.setMinimumSize(QtCore.QSize(211, 50))
        self.supplier_location.setMaximumSize(QtCore.QSize(16777215, 60))
        self.supplier_location.setText("")
        self.supplier_location.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.supplier_location.setWordWrap(True)
        self.supplier_location.setObjectName("supplier_location")
        self.horizontalLayout_16.addWidget(self.supplier_location)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_14 = StrongBodyLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(71, 16))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_17.addWidget(self.label_14)
        self.supplier_id = BodyLabel(self.tab_4)
        self.supplier_id.setMinimumSize(QtCore.QSize(131, 16))
        self.supplier_id.setMaximumSize(QtCore.QSize(16777215, 16))
        self.supplier_id.setText("")
        self.supplier_id.setObjectName("supplier_id")
        self.horizontalLayout_17.addWidget(self.supplier_id)
        self.verticalLayout_9.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_15 = StrongBodyLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(61, 16))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_18.addWidget(self.label_15)
        self.supplier_tel = BodyLabel(self.tab_4)
        self.supplier_tel.setMinimumSize(QtCore.QSize(141, 16))
        self.supplier_tel.setMaximumSize(QtCore.QSize(16777215, 16))
        self.supplier_tel.setText("")
        self.supplier_tel.setObjectName("supplier_tel")
        self.horizontalLayout_18.addWidget(self.supplier_tel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_21.addLayout(self.verticalLayout_9)
        self.supplier_logo = QtWidgets.QGraphicsView(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supplier_logo.sizePolicy().hasHeightForWidth())
        self.supplier_logo.setSizePolicy(sizePolicy)
        self.supplier_logo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.supplier_logo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.supplier_logo.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.supplier_logo.setObjectName("supplier_logo")
        self.horizontalLayout_21.addWidget(self.supplier_logo)
        self.verticalLayout_10.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_16 = BodyLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_19.addWidget(self.label_16)
        self.supplier_profile = PlainTextEdit(self.tab_4)
        self.supplier_profile.setMinimumSize(QtCore.QSize(331, 0))
        self.supplier_profile.setObjectName("supplier_profile")
        self.horizontalLayout_19.addWidget(self.supplier_profile)
        self.verticalLayout_10.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem7)
        self.supplier_list = PrimaryPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supplier_list.sizePolicy().hasHeightForWidth())
        self.supplier_list.setSizePolicy(sizePolicy)
        self.supplier_list.setObjectName("supplier_list")
        self.horizontalLayout_20.addWidget(self.supplier_list)
        self.supplier_evaluate = PushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supplier_evaluate.sizePolicy().hasHeightForWidth())
        self.supplier_evaluate.setSizePolicy(sizePolicy)
        self.supplier_evaluate.setObjectName("supplier_evaluate")
        self.horizontalLayout_20.addWidget(self.supplier_evaluate)
        spacerItem8 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_22.addLayout(self.verticalLayout_10)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.supplier_graphic_1 = QtWidgets.QGraphicsView(self.tab_4)
        self.supplier_graphic_1.setObjectName("supplier_graphic_1")
        self.verticalLayout_8.addWidget(self.supplier_graphic_1)
        self.supplier_graphic_2 = QtWidgets.QGraphicsView(self.tab_4)
        self.supplier_graphic_2.setObjectName("supplier_graphic_2")
        self.verticalLayout_8.addWidget(self.supplier_graphic_2)
        self.supplier_graphic_3 = QtWidgets.QGraphicsView(self.tab_4)
        self.supplier_graphic_3.setObjectName("supplier_graphic_3")
        self.verticalLayout_8.addWidget(self.supplier_graphic_3)
        self.horizontalLayout_22.addLayout(self.verticalLayout_8)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_22)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.query_choose_btn = PrimaryPushButton(self.tab_5)
        self.query_choose_btn.setIcon(icon)
        self.query_choose_btn.setObjectName("query_choose_btn")
        self.horizontalLayout_25.addWidget(self.query_choose_btn)
        self.query_save = PrimaryPushButton(self.tab_5)
        self.query_save.setIcon(icon)
        self.query_save.setObjectName("query_save")
        self.horizontalLayout_25.addWidget(self.query_save)
        self.query_add = PushButton(self.tab_5)
        self.query_add.setIcon(icon)
        self.query_add.setObjectName("query_add")
        self.horizontalLayout_25.addWidget(self.query_add)
        self.query_delete = PushButton(self.tab_5)
        self.query_delete.setIcon(icon)
        self.query_delete.setObjectName("query_delete")
        self.horizontalLayout_25.addWidget(self.query_delete)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_25)
        self.query_list_view = TableView(self.tab_5)
        self.query_list_view.setObjectName("query_list_view")
        self.verticalLayout_6.addWidget(self.query_list_view)
        self.verticalLayout_12.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_11.addWidget(self.tabWidget)

        self.retranslateUi(cg_sector)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(cg_sector)

    def retranslateUi(self, cg_sector):
        _translate = QtCore.QCoreApplication.translate
        cg_sector.setWindowTitle(_translate("cg_sector", "Form"))
        self.requisition_receipt_btn.setText(_translate("cg_sector", "读取采购请求"))
        self.requisition_accept_btn.setText(_translate("cg_sector", "接收请求"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("cg_sector", "请购单接收"))
        self.label_12.setText(_translate("cg_sector", "采购明细预览："))
        self.order_search.setText(_translate("cg_sector", "导入"))
        self.order_save.setText(_translate("cg_sector", "保存"))
        self.order_add.setText(_translate("cg_sector", "增加"))
        self.order_delete.setText(_translate("cg_sector", "删除"))
        self.label.setText(_translate("cg_sector", "采购明细号："))
        self.label_10.setText(_translate("cg_sector", "   供应商："))
        self.label_2.setText(_translate("cg_sector", "预计到货时间："))
        self.label_7.setText(_translate("cg_sector", "   收货单号："))
        self.label_8.setText(_translate("cg_sector", "          备注："))
        self.label_3.setText(_translate("cg_sector", "物料编码："))
        self.label_6.setText(_translate("cg_sector", "物料价格："))
        self.label_9.setText(_translate("cg_sector", "订货批量："))
        self.label_11.setText(_translate("cg_sector", "商品总价："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("cg_sector", "采购订单管理"))
        self.label_5.setText(_translate("cg_sector", "到货接收："))
        self.receive_search.setText(_translate("cg_sector", "读取"))
        self.receive_save.setText(_translate("cg_sector", "保存"))
        self.receive_add.setText(_translate("cg_sector", "增加"))
        self.receive_delete.setText(_translate("cg_sector", "删除"))
        self.label_17.setText(_translate("cg_sector", "收货单号："))
        self.label_13.setText(_translate("cg_sector", "物料编码："))
        self.label_18.setText(_translate("cg_sector", "到货时间："))
        self.label_19.setText(_translate("cg_sector", "到货量："))
        self.label_20.setText(_translate("cg_sector", "合格品数："))
        self.label_21.setText(_translate("cg_sector", "入库状态："))
        self.receive_status.setText(_translate("cg_sector", "已入库"))
        self.label_22.setText(_translate("cg_sector", "备注："))
        self.receive_btn.setText(_translate("cg_sector", "入库操作"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("cg_sector", "到货接收"))
        self.label_4.setText(_translate("cg_sector", "供应商："))
        self.label_14.setText(_translate("cg_sector", "供应商编号："))
        self.label_15.setText(_translate("cg_sector", "公司电话："))
        self.label_16.setText(_translate("cg_sector", "简介："))
        self.supplier_list.setText(_translate("cg_sector", "在售清单"))
        self.supplier_evaluate.setText(_translate("cg_sector", "生成评价"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("cg_sector", "供应商管理与评价"))
        self.query_choose_btn.setText(_translate("cg_sector", "选择文件"))
        self.query_save.setText(_translate("cg_sector", "保存"))
        self.query_add.setText(_translate("cg_sector", "增加"))
        self.query_delete.setText(_translate("cg_sector", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("cg_sector", "采购业务综合查询"))
from qfluentwidgets import BodyLabel, CheckBox, ComboBox, DateTimeEdit, LineEdit, PlainTextEdit, PrimaryPushButton, PrimaryToolButton, PushButton, StrongBodyLabel, TableView, TextEdit, ToolButton

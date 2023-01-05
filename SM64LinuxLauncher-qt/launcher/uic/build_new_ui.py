# Form implementation generated from reading ui file './SM64LinuxLauncher-qt/launcher/res/ui/build_new.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BuildNewDialog(object):
    def setupUi(self, BuildNewDialog):
        BuildNewDialog.setObjectName("BuildNewDialog")
        BuildNewDialog.resize(802, 300)
        self.gridLayout = QtWidgets.QGridLayout(BuildNewDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.l_now_building = QtWidgets.QLabel(BuildNewDialog)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.l_now_building.setFont(font)
        self.l_now_building.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.l_now_building.setObjectName("l_now_building")
        self.gridLayout.addWidget(self.l_now_building, 0, 0, 1, 1)
        self.texture_pack_folder = QtWidgets.QLineEdit(BuildNewDialog)
        self.texture_pack_folder.setReadOnly(True)
        self.texture_pack_folder.setObjectName("texture_pack_folder")
        self.gridLayout.addWidget(self.texture_pack_folder, 4, 1, 1, 1)
        self.texture_pack_select = QtWidgets.QPushButton(BuildNewDialog)
        self.texture_pack_select.setObjectName("texture_pack_select")
        self.gridLayout.addWidget(self.texture_pack_select, 4, 2, 1, 1)
        self.model_pack_folder = QtWidgets.QLineEdit(BuildNewDialog)
        self.model_pack_folder.setReadOnly(True)
        self.model_pack_folder.setObjectName("model_pack_folder")
        self.gridLayout.addWidget(self.model_pack_folder, 3, 1, 1, 1)
        self.l_build_what = QtWidgets.QLabel(BuildNewDialog)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.l_build_what.setFont(font)
        self.l_build_what.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.l_build_what.setObjectName("l_build_what")
        self.gridLayout.addWidget(self.l_build_what, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 2)
        self.b_continue = QtWidgets.QPushButton(BuildNewDialog)
        self.b_continue.setObjectName("b_continue")
        self.gridLayout.addWidget(self.b_continue, 6, 3, 1, 2)
        self.l_model_pack = QtWidgets.QLabel(BuildNewDialog)
        self.l_model_pack.setObjectName("l_model_pack")
        self.gridLayout.addWidget(self.l_model_pack, 3, 0, 1, 1)
        self.model_pack_select = QtWidgets.QPushButton(BuildNewDialog)
        self.model_pack_select.setObjectName("model_pack_select")
        self.gridLayout.addWidget(self.model_pack_select, 3, 2, 1, 1)
        self.texture_pack_clear = QtWidgets.QPushButton(BuildNewDialog)
        self.texture_pack_clear.setObjectName("texture_pack_clear")
        self.gridLayout.addWidget(self.texture_pack_clear, 4, 3, 1, 2)
        self.repo_custom_name = QtWidgets.QLineEdit(BuildNewDialog)
        self.repo_custom_name.setText("")
        self.repo_custom_name.setObjectName("repo_custom_name")
        self.gridLayout.addWidget(self.repo_custom_name, 2, 1, 1, 4)
        self.l_custom_name = QtWidgets.QLabel(BuildNewDialog)
        self.l_custom_name.setObjectName("l_custom_name")
        self.gridLayout.addWidget(self.l_custom_name, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 4, 1, 1)
        self.model_pack_clear = QtWidgets.QPushButton(BuildNewDialog)
        self.model_pack_clear.setObjectName("model_pack_clear")
        self.gridLayout.addWidget(self.model_pack_clear, 3, 3, 1, 2)
        self.l_texture_pack = QtWidgets.QLabel(BuildNewDialog)
        self.l_texture_pack.setObjectName("l_texture_pack")
        self.gridLayout.addWidget(self.l_texture_pack, 4, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(BuildNewDialog)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 6, 2, 1, 1)

        self.retranslateUi(BuildNewDialog)
        self.model_pack_select.clicked.connect(BuildNewDialog.pick_model_pack_folder) # type: ignore
        self.texture_pack_select.clicked.connect(BuildNewDialog.pick_texture_pack_folder) # type: ignore
        self.b_continue.clicked.connect(BuildNewDialog.b_continue) # type: ignore
        self.model_pack_clear.clicked.connect(self.model_pack_folder.clear) # type: ignore
        self.texture_pack_clear.clicked.connect(self.texture_pack_folder.clear) # type: ignore
        self.cancel_button.clicked.connect(BuildNewDialog.b_cancel) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(BuildNewDialog)

    def retranslateUi(self, BuildNewDialog):
        _translate = QtCore.QCoreApplication.translate
        BuildNewDialog.setWindowTitle(_translate("BuildNewDialog", "Build New Instance"))
        self.l_now_building.setText(_translate("BuildNewDialog", "Now Building:"))
        self.texture_pack_select.setText(_translate("BuildNewDialog", "Browse"))
        self.l_build_what.setText(_translate("BuildNewDialog", "Placeholder"))
        self.b_continue.setText(_translate("BuildNewDialog", "Continue"))
        self.l_model_pack.setText(_translate("BuildNewDialog", "Pick a Model pack folder (optional, Render96 ONLY)"))
        self.model_pack_select.setText(_translate("BuildNewDialog", "Browse"))
        self.texture_pack_clear.setText(_translate("BuildNewDialog", "Clear"))
        self.l_custom_name.setText(_translate("BuildNewDialog", "Type A Custom Name to use in the Main Screen (optional)"))
        self.model_pack_clear.setText(_translate("BuildNewDialog", "Clear"))
        self.l_texture_pack.setText(_translate("BuildNewDialog", "Pick a Texture Pack folder (optional)"))
        self.cancel_button.setText(_translate("BuildNewDialog", "Cancel"))

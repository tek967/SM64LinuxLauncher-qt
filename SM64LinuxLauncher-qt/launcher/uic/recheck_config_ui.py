# Form implementation generated from reading ui file './SM64LinuxLauncher-qt/launcher/res/ui/recheck_config.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RecheckConfigurationDialog(object):
    def setupUi(self, RecheckConfigurationDialog):
        RecheckConfigurationDialog.setObjectName("RecheckConfigurationDialog")
        RecheckConfigurationDialog.resize(830, 465)
        self.gridLayout = QtWidgets.QGridLayout(RecheckConfigurationDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.l_repo = QtWidgets.QLabel(RecheckConfigurationDialog)
        self.l_repo.setObjectName("l_repo")
        self.gridLayout.addWidget(self.l_repo, 1, 0, 1, 1)
        self.l_jobs = QtWidgets.QLabel(RecheckConfigurationDialog)
        self.l_jobs.setObjectName("l_jobs")
        self.gridLayout.addWidget(self.l_jobs, 5, 0, 1, 1)
        self.l_texture_pack = QtWidgets.QLabel(RecheckConfigurationDialog)
        self.l_texture_pack.setObjectName("l_texture_pack")
        self.gridLayout.addWidget(self.l_texture_pack, 7, 0, 1, 1)
        self.b_model_pack_edit = QtWidgets.QPushButton(RecheckConfigurationDialog)
        self.b_model_pack_edit.setObjectName("b_model_pack_edit")
        self.gridLayout.addWidget(self.b_model_pack_edit, 9, 2, 1, 1)
        self.l_title = QtWidgets.QLabel(RecheckConfigurationDialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l_title.setFont(font)
        self.l_title.setObjectName("l_title")
        self.gridLayout.addWidget(self.l_title, 0, 0, 1, 1)
        self.l_baserom_path = QtWidgets.QLabel(RecheckConfigurationDialog)
        self.l_baserom_path.setObjectName("l_baserom_path")
        self.gridLayout.addWidget(self.l_baserom_path, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 1, 1, 1)
        self.l_rom_region = QtWidgets.QLabel(RecheckConfigurationDialog)
        self.l_rom_region.setObjectName("l_rom_region")
        self.gridLayout.addWidget(self.l_rom_region, 3, 0, 1, 1)
        self.l_additional_makeopts = QtWidgets.QLabel(RecheckConfigurationDialog)
        self.l_additional_makeopts.setObjectName("l_additional_makeopts")
        self.gridLayout.addWidget(self.l_additional_makeopts, 6, 0, 1, 1)
        self.l_custom_name = QtWidgets.QLabel(RecheckConfigurationDialog)
        self.l_custom_name.setObjectName("l_custom_name")
        self.gridLayout.addWidget(self.l_custom_name, 4, 0, 1, 1)
        self.line_edit_texture_pack = QtWidgets.QLineEdit(RecheckConfigurationDialog)
        self.line_edit_texture_pack.setReadOnly(True)
        self.line_edit_texture_pack.setObjectName("line_edit_texture_pack")
        self.gridLayout.addWidget(self.line_edit_texture_pack, 7, 1, 1, 1)
        self.l_model_pack = QtWidgets.QLabel(RecheckConfigurationDialog)
        self.l_model_pack.setObjectName("l_model_pack")
        self.gridLayout.addWidget(self.l_model_pack, 9, 0, 1, 1)
        self.line_edit_model_pack = QtWidgets.QLineEdit(RecheckConfigurationDialog)
        self.line_edit_model_pack.setText("")
        self.line_edit_model_pack.setReadOnly(True)
        self.line_edit_model_pack.setObjectName("line_edit_model_pack")
        self.gridLayout.addWidget(self.line_edit_model_pack, 9, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(RecheckConfigurationDialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 3, 1, 1)
        self.b_texture_pack_path = QtWidgets.QPushButton(RecheckConfigurationDialog)
        self.b_texture_pack_path.setObjectName("b_texture_pack_path")
        self.gridLayout.addWidget(self.b_texture_pack_path, 7, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(RecheckConfigurationDialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 9, 3, 1, 1)
        self.line_edit_build_flags = QtWidgets.QLineEdit(RecheckConfigurationDialog)
        self.line_edit_build_flags.setText("")
        self.line_edit_build_flags.setReadOnly(False)
        self.line_edit_build_flags.setObjectName("line_edit_build_flags")
        self.gridLayout.addWidget(self.line_edit_build_flags, 6, 1, 1, 3)
        self.combobox_jobs = QtWidgets.QComboBox(RecheckConfigurationDialog)
        self.combobox_jobs.setObjectName("combobox_jobs")
        self.combobox_jobs.addItem("")
        self.combobox_jobs.addItem("")
        self.combobox_jobs.addItem("")
        self.combobox_jobs.addItem("")
        self.combobox_jobs.addItem("")
        self.combobox_jobs.addItem("")
        self.combobox_jobs.addItem("")
        self.gridLayout.addWidget(self.combobox_jobs, 5, 1, 1, 3)
        self.line_edit_custom_name = QtWidgets.QLineEdit(RecheckConfigurationDialog)
        self.line_edit_custom_name.setReadOnly(True)
        self.line_edit_custom_name.setObjectName("line_edit_custom_name")
        self.gridLayout.addWidget(self.line_edit_custom_name, 4, 1, 1, 3)
        self.combobox_romregion = QtWidgets.QComboBox(RecheckConfigurationDialog)
        self.combobox_romregion.setObjectName("combobox_romregion")
        self.combobox_romregion.addItem("")
        self.combobox_romregion.addItem("")
        self.combobox_romregion.addItem("")
        self.gridLayout.addWidget(self.combobox_romregion, 3, 1, 1, 3)
        self.b_baserom_path = QtWidgets.QPushButton(RecheckConfigurationDialog)
        self.b_baserom_path.setObjectName("b_baserom_path")
        self.gridLayout.addWidget(self.b_baserom_path, 2, 3, 1, 1)
        self.line_edit_baserom_path = QtWidgets.QLineEdit(RecheckConfigurationDialog)
        self.line_edit_baserom_path.setReadOnly(True)
        self.line_edit_baserom_path.setObjectName("line_edit_baserom_path")
        self.gridLayout.addWidget(self.line_edit_baserom_path, 2, 1, 1, 2)
        self.combobox_repo = QtWidgets.QComboBox(RecheckConfigurationDialog)
        self.combobox_repo.setObjectName("combobox_repo")
        self.gridLayout.addWidget(self.combobox_repo, 1, 1, 1, 3)
        self.b_build = QtWidgets.QPushButton(RecheckConfigurationDialog)
        self.b_build.setObjectName("b_build")
        self.gridLayout.addWidget(self.b_build, 11, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 11, 0, 1, 3)

        self.retranslateUi(RecheckConfigurationDialog)
        self.b_baserom_path.clicked.connect(RecheckConfigurationDialog.b_baserom_path) # type: ignore
        self.b_texture_pack_path.clicked.connect(RecheckConfigurationDialog.b_texturepack_path) # type: ignore
        self.b_model_pack_edit.clicked.connect(RecheckConfigurationDialog.b_modelpack_path) # type: ignore
        self.b_build.clicked.connect(RecheckConfigurationDialog.b_build) # type: ignore
        self.pushButton.clicked.connect(self.line_edit_texture_pack.clear) # type: ignore
        self.pushButton_2.clicked.connect(self.line_edit_model_pack.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(RecheckConfigurationDialog)

    def retranslateUi(self, RecheckConfigurationDialog):
        _translate = QtCore.QCoreApplication.translate
        RecheckConfigurationDialog.setWindowTitle(_translate("RecheckConfigurationDialog", "Recheck Configuration"))
        self.l_repo.setText(_translate("RecheckConfigurationDialog", "Repository"))
        self.l_jobs.setText(_translate("RecheckConfigurationDialog", "Jobs (4 is default)"))
        self.l_texture_pack.setText(_translate("RecheckConfigurationDialog", "Texture Pack Path (if set)"))
        self.b_model_pack_edit.setText(_translate("RecheckConfigurationDialog", "Edit"))
        self.l_title.setText(_translate("RecheckConfigurationDialog", "Does This Look Right to you?"))
        self.l_baserom_path.setText(_translate("RecheckConfigurationDialog", "Base ROM Path"))
        self.l_rom_region.setText(_translate("RecheckConfigurationDialog", "ROM Region"))
        self.l_additional_makeopts.setText(_translate("RecheckConfigurationDialog", "Additional Build Flags (if set)"))
        self.l_custom_name.setText(_translate("RecheckConfigurationDialog", "Custom Name (if set)"))
        self.l_model_pack.setText(_translate("RecheckConfigurationDialog", "Model Pack Path (if set)"))
        self.pushButton.setText(_translate("RecheckConfigurationDialog", "Clear"))
        self.b_texture_pack_path.setText(_translate("RecheckConfigurationDialog", "Edit"))
        self.pushButton_2.setText(_translate("RecheckConfigurationDialog", "Clear"))
        self.combobox_jobs.setItemText(0, _translate("RecheckConfigurationDialog", "4"))
        self.combobox_jobs.setItemText(1, _translate("RecheckConfigurationDialog", "1"))
        self.combobox_jobs.setItemText(2, _translate("RecheckConfigurationDialog", "2"))
        self.combobox_jobs.setItemText(3, _translate("RecheckConfigurationDialog", "8"))
        self.combobox_jobs.setItemText(4, _translate("RecheckConfigurationDialog", "10"))
        self.combobox_jobs.setItemText(5, _translate("RecheckConfigurationDialog", "12"))
        self.combobox_jobs.setItemText(6, _translate("RecheckConfigurationDialog", "16"))
        self.combobox_romregion.setItemText(0, _translate("RecheckConfigurationDialog", "USA (us)"))
        self.combobox_romregion.setItemText(1, _translate("RecheckConfigurationDialog", "European PAL (eu)"))
        self.combobox_romregion.setItemText(2, _translate("RecheckConfigurationDialog", "Japanese (jp)"))
        self.b_baserom_path.setText(_translate("RecheckConfigurationDialog", "Edit"))
        self.b_build.setText(_translate("RecheckConfigurationDialog", "Build"))

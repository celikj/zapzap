# Form implementation generated from reading ui file '/home/tosta/Documentos/GitHub/zapzap/zapzap/ui/ui_browser.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1137, 606)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setMinimumSize(QtCore.QSize(50, 0))
        self.frame.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(5, 6, 5, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.page_buttons_layout = QtWidgets.QVBoxLayout()
        self.page_buttons_layout.setSpacing(0)
        self.page_buttons_layout.setObjectName("page_buttons_layout")
        self.verticalLayout.addLayout(self.page_buttons_layout)
        self.line = QtWidgets.QFrame(parent=self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.settings_buttons_layout = QtWidgets.QVBoxLayout()
        self.settings_buttons_layout.setContentsMargins(-1, 0, -1, 0)
        self.settings_buttons_layout.setSpacing(6)
        self.settings_buttons_layout.setObjectName("settings_buttons_layout")
        self.btn_new_account = QtWidgets.QPushButton(parent=self.frame)
        self.btn_new_account.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_new_account.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_new_account.setText("")
        self.btn_new_account.setIconSize(QtCore.QSize(20, 20))
        self.btn_new_account.setFlat(False)
        self.btn_new_account.setObjectName("btn_new_account")
        self.settings_buttons_layout.addWidget(self.btn_new_account)
        spacerItem = QtWidgets.QSpacerItem(20, 473, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.settings_buttons_layout.addItem(spacerItem)
        self.btn_new_chat_number = QtWidgets.QPushButton(parent=self.frame)
        self.btn_new_chat_number.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_new_chat_number.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_new_chat_number.setText("")
        self.btn_new_chat_number.setIconSize(QtCore.QSize(20, 20))
        self.btn_new_chat_number.setObjectName("btn_new_chat_number")
        self.settings_buttons_layout.addWidget(self.btn_new_chat_number)
        self.btn_new_chat = QtWidgets.QPushButton(parent=self.frame)
        self.btn_new_chat.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_new_chat.setText("")
        self.btn_new_chat.setIconSize(QtCore.QSize(20, 20))
        self.btn_new_chat.setObjectName("btn_new_chat")
        self.settings_buttons_layout.addWidget(self.btn_new_chat)
        self.line_2 = QtWidgets.QFrame(parent=self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.settings_buttons_layout.addWidget(self.line_2)
        self.btn_open_settings = QtWidgets.QPushButton(parent=self.frame)
        self.btn_open_settings.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_open_settings.setText("")
        self.btn_open_settings.setIconSize(QtCore.QSize(20, 20))
        self.btn_open_settings.setObjectName("btn_open_settings")
        self.settings_buttons_layout.addWidget(self.btn_open_settings)
        self.verticalLayout.addLayout(self.settings_buttons_layout)
        self.horizontalLayout.addWidget(self.frame)
        self.pages = QtWidgets.QStackedWidget(parent=Form)
        self.pages.setObjectName("pages")
        self.horizontalLayout.addWidget(self.pages)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/qtoaster_donation.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_QtoasterDonation(object):
    def setupUi(self, QtoasterDonation):
        QtoasterDonation.setObjectName("QtoasterDonation")
        QtoasterDonation.resize(414, 84)
        QtoasterDonation.setWindowTitle("")
        QtoasterDonation.setStyleSheet("#frame{\n"
"    border: 1px solid #585A5D;\n"
"    border-radius: 8px; \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #202C33;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(QtoasterDonation)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(parent=QtoasterDonation)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, 9)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(64, 64))
        self.logo.setMaximumSize(QtCore.QSize(64, 64))
        self.logo.setText("")
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelWelcomeTo = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelWelcomeTo.setFont(font)
        self.labelWelcomeTo.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelWelcomeTo.setObjectName("labelWelcomeTo")
        self.verticalLayout_3.addWidget(self.labelWelcomeTo)
        self.labelZapZap = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.labelZapZap.setFont(font)
        self.labelZapZap.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.labelZapZap.setObjectName("labelZapZap")
        self.verticalLayout_3.addWidget(self.labelZapZap)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.donateButton = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.donateButton.sizePolicy().hasHeightForWidth())
        self.donateButton.setSizePolicy(sizePolicy)
        self.donateButton.setMinimumSize(QtCore.QSize(150, 40))
        self.donateButton.setStyleSheet("QPushButton {\n"
"                border: 0px solid black;\n"
"                border-radius: 5px; \n"
"                color: rgb(255, 255, 255);  \n"
"                 background-color: rgb(38, 162, 105);\n"
"                padding: 5px;\n"
"                Text-align:center;\n"
"            }\n"
"            QPushButton:hover {\n"
"                  \n"
"    \n"
"    background-color: rgb(46, 194, 126);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                    background-color: rgb(46, 194, 126);\n"
"            }")
        self.donateButton.setObjectName("donateButton")
        self.verticalLayout_4.addWidget(self.donateButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.closeButton = QtWidgets.QToolButton(parent=self.frame)
        self.closeButton.setStyleSheet("\n"
"                QToolButton {\n"
"                padding: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                background-color: #202C33;\n"
"                }\n"
"         ")
        self.closeButton.setAutoRaise(True)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(QtoasterDonation)
        QtCore.QMetaObject.connectSlotsByName(QtoasterDonation)

    def retranslateUi(self, QtoasterDonation):
        
        self.labelWelcomeTo.setText(_("Welcome to"))
        self.labelZapZap.setText(_("ZapZap"))
        self.donateButton.setText(_("Make a donation"))
        self.closeButton.setText(_("..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtoasterDonation = QtWidgets.QWidget()
    ui = Ui_QtoasterDonation()
    ui.setupUi(QtoasterDonation)
    QtoasterDonation.show()
    sys.exit(app.exec())

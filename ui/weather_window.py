# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 717)
        MainWindow.setStyleSheet("QPushButton { background-color: transparent }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.Change_degree_type_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Change_degree_type_button.setFont(font)
        self.Change_degree_type_button.setStyleSheet("background-color: rgba(255,255,255,0);border: 0px;")
        self.Change_degree_type_button.setObjectName("Change_degree_type_button")
        self.horizontalLayout_2.addWidget(self.Change_degree_type_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.weather_icon_lable = QtWidgets.QLabel(self.centralwidget)
        self.weather_icon_lable.setObjectName("weather_icon_lable")
        self.verticalLayout_4.addWidget(self.weather_icon_lable)
        self.view_lable = QtWidgets.QLabel(self.centralwidget)
        self.view_lable.setObjectName("view_lable")
        self.verticalLayout_4.addWidget(self.view_lable)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.temperature_line_lable = QtWidgets.QLabel(self.centralwidget)
        self.temperature_line_lable.setObjectName("temperature_line_lable")
        self.horizontalLayout.addWidget(self.temperature_line_lable)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sunrise_icon_lable = QtWidgets.QLabel(self.centralwidget)
        self.sunrise_icon_lable.setMinimumSize(QtCore.QSize(91, 101))
        self.sunrise_icon_lable.setObjectName("sunrise_icon_lable")
        self.verticalLayout_6.addWidget(self.sunrise_icon_lable)
        self.sunrise_time_lable = QtWidgets.QLabel(self.centralwidget)
        self.sunrise_time_lable.setObjectName("sunrise_time_lable")
        self.verticalLayout_6.addWidget(self.sunrise_time_lable)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.sunset_icon_lable = QtWidgets.QLabel(self.centralwidget)
        self.sunset_icon_lable.setObjectName("sunset_icon_lable")
        self.verticalLayout_8.addWidget(self.sunset_icon_lable)
        self.sunset_time_lable = QtWidgets.QLabel(self.centralwidget)
        self.sunset_time_lable.setObjectName("sunset_time_lable")
        self.verticalLayout_8.addWidget(self.sunset_time_lable)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_8)
        self.gridLayout_2.addLayout(self.formLayout, 2, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wind_icon_lable = QtWidgets.QLabel(self.centralwidget)
        self.wind_icon_lable.setObjectName("wind_icon_lable")
        self.verticalLayout_3.addWidget(self.wind_icon_lable)
        self.wind_speed_lable = QtWidgets.QLabel(self.centralwidget)
        self.wind_speed_lable.setObjectName("wind_speed_lable")
        self.verticalLayout_3.addWidget(self.wind_speed_lable)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">  Jerusalem</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;\">30°</span></p></body></html>"))
        self.Change_degree_type_button.setText(_translate("MainWindow", "C°| F°"))
        self.weather_icon_lable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/weather_icons/01d.png\"/></p></body></html>"))
        self.view_lable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Clouds</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">overcast clouds</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;\">0</span><span style=\" font-size:30pt; vertical-align:super;\">°</span></p></body></html>"))
        self.temperature_line_lable.setText(_translate("MainWindow", "_________________________________________________"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;\">40</span><span style=\" font-size:30pt; vertical-align:super;\">°</span></p></body></html>"))
        self.sunrise_icon_lable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/weather_icons/sunrise.png\"/></p></body></html>"))
        self.sunrise_time_lable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">sunrise</span></p></body></html>"))
        self.sunset_icon_lable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/weather_icons/sunset.png\"/></p></body></html>"))
        self.sunset_time_lable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">sunset</span></p></body></html>"))
        self.wind_icon_lable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/weather_icons/wind.png\"/></p></body></html>"))
        self.wind_speed_lable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">50 km/h</span></p></body></html>"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    stylesheet = """
background-image: url(/home/ori/PycharmProjects/WeatherApp/icons/background.png);
    """
    app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
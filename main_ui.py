# Steps to add to the UI:
#   - Create a layout for grouped widgets:
#           - Ex: self.box_button_layout = QtWidgets.QHBoxLayout()
#
#   - Create a widget:
#           - Ex: self.pointA_entry = QtWidgets.QLineEdit(self.central_widget)
#           - Make sure to set the widget to self.central_widget
#
#   - Add the widget to the layout
#           - Ex: self.box_button_layout.addWidget(self.pointA_entry)
#
#   - Once all widgets added, add the layout to the central layout
#           - Ex: self.central_layout.addLayout(self.box_button_layout)
#   
# REMEMBER:
#   - Setting text/icon values will either never change or will get overriden
#   - To update text/values, see set_weather function in main_window.py 


from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets
from PyQt6.QtCore import *
import map

class Main_UI():

    def setup_UI(self, Main_Window):

        self.central_widget = QtWidgets.QWidget(Main_Window)
        self.central_widget.setObjectName("central_widget")

        self.central_widget.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 cyan, stop:1 blue);}")

        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget) 
        self.central_layout.setObjectName("central_layout")

        self.box_button_layout = QtWidgets.QHBoxLayout()
        self.box_button_layout.setObjectName("box_button_layout")

        self.topLabel = QtWidgets.QLabel(self.central_widget)
        self.topLabel.setGeometry(QRect(150, 40, 291, 10))
        self.topLabel.setText("Enter Point A ------------------------------------>")
        self.box_button_layout.addWidget(self.topLabel)

        self.pointA_entry = QtWidgets.QComboBox(self.central_widget)
        self.pointA_entry.addItems(self.names)
        self.pointA_entry.setGeometry(QRect(80, 240, 191, 31))
        self.pointA_entry.setStyleSheet("background-color: rgb(255,130,0)")
        self.box_button_layout.addWidget(self.pointA_entry)

        self.topLabel1 = QtWidgets.QLabel(self.central_widget)
        self.topLabel1.setGeometry(QRect(150, 40, 291, 100))
        self.topLabel1.setText("Enter Point B ------------------------------------>")
        self.box_button_layout.addWidget(self.topLabel1)

        self.pointB_entry = QtWidgets.QComboBox(self.central_widget)
        self.pointB_entry.addItems(self.names)
        self.pointB_entry.setGeometry(QRect(1, 1, 1, 1))
        self.pointB_entry.setStyleSheet("background-color: rgb(255,130,0)")
        self.box_button_layout.addWidget(self.pointB_entry)

        self.find_path_button = QtWidgets.QPushButton(self.central_widget)
        self.find_path_button.setText("YEET")
        self.find_path_button.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));"
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 orange, stop:1 white);}"
            "border-radius: -20px\n")
        self.find_path_button.setMinimumSize(QSize(20, 38))
        self.box_button_layout.addWidget(self.find_path_button)

        self.settingsButton = QtWidgets.QPushButton() #Button that opens the settings Menu
        self.settingsButton.setText("Settings")
        self.settingsButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.settingsButton.clicked.connect(self.settingsClicked)
        self.box_button_layout.addWidget(self.settingsButton)

        self.central_layout.addLayout(self.box_button_layout)

        self.central_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scene = QGraphicsScene(-50, -50, 1124, 843)
        self.view = QGraphicsView(self.scene)

        self.map = map.mapObject("Images/map3.jpg")
        self.scene.addItem(self.map)

        self.view.setLayout(self.central_layout)
        Main_Window.setCentralWidget(self.central_widget)
            
    def Resize_Text_Label(self, event):
        '''
        Will hopefully resize things based on window size
        '''
        default_text_size = 9
        if default_text_size < (self.rect().width() // 40):
            new_size = QFont('', self.rect().width() // 40)
        else:
            new_size = QFont('', default_text_size)
        self.setFont(new_size)
        
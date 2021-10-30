from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QColor, QPalette, QFont, QBrush, QPixmap
import sys
import map, Dijkstra

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # so, this window is actually not used, but it was useful in testing, and its init makes a qgraphicsscene window too
        self.setGeometry(100, 100, 600, 600) #Set window size
        palette = self.palette()
        # background color is Tennessee Orange
        palette.setColor(QPalette.ColorRole.Window, QColor(255, 130, 0))
        self.setPalette(palette)

        centralwidget = QWidget() #Create central widget and the main layouts
        self.buttonLayout = QVBoxLayout()
        self.mainLayout = QVBoxLayout()

        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        self.settingsButton = QPushButton() #Button that opens the settings Menu
        self.settingsButton.setText("Settings")
        self.settingsButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.settingsButton.clicked.connect(self.settingsClicked)
        self.buttonLayout.addWidget(self.settingsButton)

        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(20)

        self.mainLayout.addLayout(self.buttonLayout)

        centralwidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralwidget)

        self.scene = QGraphicsScene(-50, -50, 1000, 1000)
        self.view = QGraphicsView(self.scene)

        self.map = map.mapObject()
        self.scene.addItem(self.map)

        self.view.setLayout(self.mainLayout)
        
        # 4 roads
        self.roads = []
        self.n1 = map.road()
        self.n2 = map.road()
        self.n3 = map.road()
        self.n4 = map.road()
        self.n5 = map.road()
        self.n6 = map.road()
        self.n7 = map.road()
        self.n8 = map.road()
        self.n9 = map.road()
        self.n10 = map.road()
        self.n11 = map.road()
        self.n12 = map.road()
        self.n13 = map.road()
        self.n14 = map.road()
        self.n15 = map.road()
        self.n16 = map.road()
        self.n17 = map.road()
        self.n18 = map.road()
        self.n19 = map.road()
        self.n20 = map.road()
        self.n21 = map.road()
        self.n22 = map.road()
        self.n23 = map.road()
        self.n24 = map.road()
        self.n25 = map.road()
        self.n26 = map.road()
        self.n27 = map.road()
        self.n28 = map.road()
        self.n29 = map.road()
        self.n30 = map.road()
        self.n31 = map.road()
        self.n32 = map.road()
        self.n33 = map.road()
        self.n34 = map.road()
        self.n35 = map.road()
        self.n36 = map.road()
        self.n37 = map.road()
        self.n38 = map.road()
        self.n39 = map.road()
        self.n40 = map.road()
        self.n41 = map.road()
        self.n42 = map.road()
        self.n43 = map.road()
        self.n44 = map.road()
        self.n45 = map.road()
        self.n46 = map.road()
        self.n47 = map.road()
        self.n48 = map.road()
        self.n49 = map.road()
        self.n50 = map.road()
        self.n51 = map.road()
        self.n52 = map.road()
        self.n53 = map.road()
        self.n54 = map.road()
        self.n55 = map.road()
        self.n56 = map.road()
        self.n57 = map.road()
        self.n58 = map.road()
        self.n59 = map.road()
        self.n60 = map.road()
        self.n61 = map.road()

        # connections to other nodes
        self.n1.connected.append(self.n2)
        self.n1.connected.append(self.n4)
        self.n1.connected.append(self.n7)
        self.n1.connected.append(self.n10)
        self.n1.connected.append(self.n13)
        self.n1.connected.append(self.n14)
        self.n1.connected.append(self.n19)
        self.n1.connected.append(self.n20)
        self.n1.connected.append(self.n24)
        self.n1.connected.append(self.n31)
        self.n1.connected.append(self.n32)
        self.n1.connected.append(self.n34)

        self.n2.connected.append(self.n34)
        self.n2.connected.append(self.n3)
        self.n2.connected.append(self.n6)
        self.n2.connected.append(self.n1)

        self.n3.connected.append(self.n8)
        self.n3.connected.append(self.n5)
        self.n3.connected.append(self.n2)

        self.n4.connected.append(self.n1)
        self.n4.connected.append(self.n6)
        self.n4.connected.append(self.n5)

        self.n5.connected.append(self.n6)
        self.n5.connected.append(self.n8)
        self.n5.connected.append(self.n4)

        self.n6.connected.append(self.n34)
        self.n6.connected.append(self.n2)
        self.n6.connected.append(self.n3)
        self.n6.connected.append(self.n5)
        self.n6.connected.append(self.n4)
        self.n6.connected.append(self.n7)
        self.n6.connected.append(self.n10)
        self.n6.connected.append(self.n9)
        self.n6.connected.append(self.n11)
        self.n6.connected.append(self.n12)
        self.n6.connected.append(self.n13)
        self.n6.connected.append(self.n14)
        self.n6.connected.append(self.n15)
        self.n6.connected.append(self.n16)

        self.n7.connected.append(self.n1)
        self.n7.connected.append(self.n6)
        self.n7.connected.append(self.n9)

        self.n8.connected.append(self.n3)
        self.n8.connected.append(self.n5)
        self.n8.connected.append(self.n9)
        self.n8.connected.append(self.n11)
        self.n8.connected.append(self.n12)
        self.n8.connected.append(self.n13)
        self.n8.connected.append(self.n6)
        self.n8.connected.append(self.n37)

        self.n9.connected.append(self.n6)
        self.n9.connected.append(self.n7)
        self.n9.connected.append(self.n8)

        self.n10.connected.append(self.n1)
        self.n10.connected.append(self.n11)
        self.n10.connected.append(self.n6)

        self.n11.connected.append(self.n6)
        self.n11.connected.append(self.n8)
        self.n11.connected.append(self.n10)

        self.n12.connected.append(self.n6)
        self.n12.connected.append(self.n13)

        self.n13.connected.append(self.n1)
        self.n13.connected.append(self.n6)
        self.n13.connected.append(self.n8)

        self.n14.connected.append(self.n1)
        self.n14.connected.append(self.n6)
        self.n14.connected.append(self.n15)
        self.n14.connected.append(self.n16)

        self.n15.connected.append(self.n14)
        self.n15.connected.append(self.n16)
        self.n15.connected.append(self.n41)
        self.n15.connected.append(self.n43)
        self.n15.connected.append(self.n6)

        self.n16.connected.append(self.n14)
        self.n16.connected.append(self.n15)
        self.n16.connected.append(self.n17)
        self.n16.connected.append(self.n18)
        self.n16.connected.append(self.n41)
        self.n16.connected.append(self.n43)
        self.n16.connected.append(self.n6)

        self.n17.connected.append(self.n16)
        self.n17.connected.append(self.n43)
        self.n17.connected.append(self.n45)
        self.n17.connected.append(self.n38)

        self.n18.connected.append(self.n16)
        self.n18.connected.append(self.n19)

        self.n19.connected.append(self.n1)
        self.n19.connected.append(self.n18)
        self.n19.connected.append(self.n34)
        self.n19.connected.append(self.n38)

        self.n20.connected.append(self.n1)
        self.n20.connected.append(self.n23)
        self.n20.connected.append(self.n21)
        self.n20.connected.append(self.n38)

        self.n21.connected.append(self.n20)
        self.n21.connected.append(self.n22)
        self.n21.connected.append(self.n38)

        self.n22.connected.append(self.n23)
        self.n22.connected.append(self.n24)
        self.n22.connected.append(self.n21)
        self.n22.connected.append(self.n26)
        
        self.n23.connected.append(self.n24)
        self.n23.connected.append(self.n22)
        self.n23.connected.append(self.n26)

        self.n24.connected.append(self.n1)
        self.n24.connected.append(self.n22)
        self.n24.connected.append(self.n23)

        self.n25.connected.append(self.n20)
        self.n25.connected.append(self.n28)
        self.n25.connected.append(self.n27)

        self.n26.connected.append(self.n23)
        self.n26.connected.append(self.n24)
        self.n26.connected.append(self.n22)

        self.n27.connected.append(self.n25)
        self.n27.connected.append(self.n27)
        self.n27.connected.append(self.n28)

        self.n28.connected.append(self.n24)
        self.n28.connected.append(self.n25)
        self.n28.connected.append(self.n27)

        self.n29.connected.append(self.n1)
        self.n29.connected.append(self.n27)
        self.n29.connected.append(self.n30)

        self.n30.connected.append(self.n29)
        self.n30.connected.append(self.n31)

        self.n31.connected.append(self.n1)
        self.n31.connected.append(self.n30)
        self.n31.connected.append(self.n33)

        self.n32.connected.append(self.n1)
        self.n32.connected.append(self.n31)
        self.n32.connected.append(self.n33)

        self.n33.connected.append(self.n31)
        self.n33.connected.append(self.n32)
        self.n33.connected.append(self.n61)

        self.n34.connected.append(self.n1)
        self.n34.connected.append(self.n6)
        self.n34.connected.append(self.n8)
        self.n34.connected.append(self.n40)
        self.n34.connected.append(self.n35)
        self.n34.connected.append(self.n38)
        self.n34.connected.append(self.n36)
        self.n34.connected.append(self.n50)
        self.n34.connected.append(self.n51)
        self.n34.connected.append(self.n53)
        self.n34.connected.append(self.n42)
        self.n34.connected.append(self.n57)
        self.n34.connected.append(self.n46)
        self.n34.connected.append(self.n47)
        self.n34.connected.append(self.n60)
        self.n34.connected.append(self.n19)

        self.n35.connected.append(self.n34)
        self.n35.connected.append(self.n38)
        self.n35.connected.append(self.n36)

        self.n36.connected.append(self.n34)
        self.n36.connected.append(self.n35)
        self.n36.connected.append(self.n38)
        self.n36.connected.append(self.n50)

        self.n37.connected.append(self.n8)
        self.n37.connected.append(self.n40)
        self.n37.connected.append(self.n38)

        self.n38.connected.append(self.n34)
        self.n38.connected.append(self.n35)
        self.n38.connected.append(self.n36)
        self.n38.connected.append(self.n37)
        self.n38.connected.append(self.n39)
        self.n38.connected.append(self.n43)
        self.n38.connected.append(self.n45)
        self.n38.connected.append(self.n19)
        self.n38.connected.append(self.n17)
        self.n38.connected.append(self.n20)
        self.n38.connected.append(self.n21)
        self.n38.connected.append(self.n50)

        self.n39.connected.append(self.n38)
        self.n39.connected.append(self.n41)

        self.n40.connected.append(self.n6)
        self.n40.connected.append(self.n34)
        self.n40.connected.append(self.n37)
        
        self.n41.connected.append(self.n39)
        self.n41.connected.append(self.n43)
        self.n41.connected.append(self.n15)
        self.n42.connected.append(self.n38)
        self.n42.connected.append(self.n34)
        self.n42.connected.append(self.n53)
        self.n43.connected.append(self.n38)
        self.n43.connected.append(self.n41)
        self.n43.connected.append(self.n15)
        self.n44.connected.append(self.n46)
        self.n45.connected.append(self.n46)
        self.n45.connected.append(self.n38)
        self.n46.connected.append(self.n34)
        self.n46.connected.append(self.n44)
        self.n46.connected.append(self.n45)
        self.n46.connected.append(self.n38)
        self.n47.connected.append(self.n48)
        self.n47.connected.append(self.n60)
        self.n47.connected.append(self.n34)
        self.n48.connected.append(self.n47)
        self.n48.connected.append(self.n60)
        self.n48.connected.append(self.n50)
        self.n49.connected.append(self.n50)
        self.n50.connected.append(self.n36)
        self.n50.connected.append(self.n34)
        self.n50.connected.append(self.n55)
        self.n50.connected.append(self.n58)
        self.n50.connected.append(self.n59)
        self.n50.connected.append(self.n49)
        self.n50.connected.append(self.n48)
        self.n50.connected.append(self.n38)
        self.n50.connected.append(self.n25)
        self.n50.connected.append(self.n21)
        self.n51.connected.append(self.n50)
        self.n51.connected.append(self.n34)
        self.n51.connected.append(self.n52)
        self.n52.connected.append(self.n34)
        self.n52.connected.append(self.n51)
        self.n52.connected.append(self.n54)
        self.n53.connected.append(self.n42)
        self.n53.connected.append(self.n34)
        self.n53.connected.append(self.n54)
        self.n53.connected.append(self.n55)
        self.n54.connected.append(self.n34)
        self.n54.connected.append(self.n52)
        self.n54.connected.append(self.n53)
        self.n54.connected.append(self.n55)
        self.n54.connected.append(self.n56)
        self.n55.connected.append(self.n50)
        self.n55.connected.append(self.n54)
        self.n55.connected.append(self.n56)
        self.n55.connected.append(self.n53)
        self.n56.connected.append(self.n53)
        self.n56.connected.append(self.n54)
        self.n56.connected.append(self.n55)
        self.n56.connected.append(self.n56)
        self.n56.connected.append(self.n57)
        self.n57.connected.append(self.n56)
        self.n57.connected.append(self.n58)
        self.n57.connected.append(self.n34)
        self.n58.connected.append(self.n56)
        self.n58.connected.append(self.n57)
        self.n58.connected.append(self.n59)
        self.n58.connected.append(self.n50)
        self.n59.connected.append(self.n50)
        self.n59.connected.append(self.n58)
        self.n59.connected.append(self.n61)
        self.n60.connected.append(self.n34)
        self.n60.connected.append(self.n47)
        self.n60.connected.append(self.n48)
        self.n61.connected.append(self.n59)
        self.n61.connected.append(self.n33)

        # adding the roads to roads
        self.roads.append(self.n1)
        self.roads.append(self.n2)
        self.roads.append(self.n3)
        self.roads.append(self.n4)
        self.roads.append(self.n5)
        self.roads.append(self.n6)
        self.roads.append(self.n7)
        self.roads.append(self.n8)
        self.roads.append(self.n9)
        self.roads.append(self.n10)
        self.roads.append(self.n11)
        self.roads.append(self.n12)
        self.roads.append(self.n13)
        self.roads.append(self.n14)
        self.roads.append(self.n15)
        self.roads.append(self.n16)
        self.roads.append(self.n17)
        self.roads.append(self.n18)
        self.roads.append(self.n19)
        self.roads.append(self.n20)
        self.roads.append(self.n21)
        self.roads.append(self.n22)
        self.roads.append(self.n23)
        self.roads.append(self.n24)
        self.roads.append(self.n25)
        self.roads.append(self.n26)
        self.roads.append(self.n27)
        self.roads.append(self.n28)
        self.roads.append(self.n29)
        self.roads.append(self.n30)
        self.roads.append(self.n31)
        self.roads.append(self.n32)
        self.roads.append(self.n33)
        self.roads.append(self.n34)
        self.roads.append(self.n35)
        self.roads.append(self.n36)
        self.roads.append(self.n37)
        self.roads.append(self.n38)
        self.roads.append(self.n39)
        self.roads.append(self.n40)
        self.roads.append(self.n41)
        self.roads.append(self.n42)
        self.roads.append(self.n43)
        self.roads.append(self.n44)
        self.roads.append(self.n45)
        self.roads.append(self.n46)
        self.roads.append(self.n47)
        self.roads.append(self.n48)
        self.roads.append(self.n49)
        self.roads.append(self.n50)
        self.roads.append(self.n51)
        self.roads.append(self.n52)
        self.roads.append(self.n53)
        self.roads.append(self.n54)
        self.roads.append(self.n55)
        self.roads.append(self.n56)
        self.roads.append(self.n57)
        self.roads.append(self.n58)
        self.roads.append(self.n59)
        self.roads.append(self.n60)
        self.roads.append(self.n61)

        self.array = Dijkstra.array(self.roads)

        self.view.show()

    def settingsClicked(self, event):
        self.settingsMenu = QMessageBox()
        self.settingsMenu.setText("Settings")
        self.settingsMenu.setFont(QFont("Times", 14, QFont.Weight.Medium))
        self.settingsMenu.setStyleSheet("background-color: white;"
                                        "color: black;"
                                        "padding: 6px;")
            
        # Adds the resume button to the settings
        self.resumeButton = QPushButton()
        self.resumeButton.setText("Resume")
        self.resumeButton.setFont(QFont("Times", 10, QFont.Weight.Medium))
        self.resumeButton.setStyleSheet("background-color: lightGray;"
                                        "color: black;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 55 em;"
                                        "max-width: 55 em;"
                                        "min-height: 15 em;"
                                        "max-height: 15 em;"
                                        "padding: 6 px;")
        self.settingsMenu.addButton(self.resumeButton, QMessageBox.ButtonRole.DestructiveRole)
        # self.resumeButton.clicked.connect(self.resumeClicked)
        self.settingsMenu.setEscapeButton(self.resumeButton)

        # Adds an exit button to settingsMenu
        self.settingsExitButton = QPushButton()
        self.settingsExitButton.setText("Exit")
        self.settingsExitButton.setFont(QFont("Times", 10, QFont.Weight.Medium))
        self.settingsExitButton.setStyleSheet("background-color: lightGray;"
                                            "color: black;"
                                            "border-style: outset;"
                                            "border-width: 1px;"
                                            "border-color: black;"
                                            "min-width: 45 em;"
                                            "max-width: 45 em;"
                                            "min-height: 15 em;"
                                            "max-height: 15 em;"
                                            "padding: 6 px;")
        self.settingsExitButton.clicked.connect(self.exitClicked)
        self.settingsMenu.addButton(self.settingsExitButton, QMessageBox.ButtonRole.DestructiveRole)


        # self.addWidget(self.settingsMenu)
                
        self.settingsMenu.open()

    def exitClicked(self, event):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    #window.show()

    sys.exit(app.exec())

from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QColor, QPalette, QFont, QBrush, QPixmap
import sys, random
from main_ui import Main_UI
import map, Dijkstra

class Main_Window(QMainWindow, Main_UI):
    def __init__(self):
        super(Main_Window, self).__init__()
 
        # 4 roads
        self.roads = []
        self.n1 = map.road("Images/lines/1.png")
        self.n2 = map.road("Images/lines/2.png")
        self.n3 = map.road("Images/lines/3.png")
        self.n4 = map.road("Images/lines/4.png")
        self.n5 = map.road("Images/lines/5.png")
        self.n6 = map.road("Images/lines/6.png")
        self.n7 = map.road("Images/lines/7.png")
        self.n8 = map.road("Images/lines/8.png")
        self.n9 = map.road("Images/lines/9.png")
        self.n10 = map.road("Images/lines/10.png")
        self.n11 = map.road("Images/lines/11.png")
        self.n12 = map.road("Images/lines/12.png")
        self.n13 = map.road("Images/lines/13.png")
        self.n14 = map.road("Images/lines/14.png")
        self.n15 = map.road("Images/lines/15.png")
        self.n16 = map.road("Images/lines/16.png")
        self.n17 = map.road("Images/lines/17.png")
        self.n18 = map.road("Images/lines/18.png")
        self.n19 = map.road("Images/lines/19.png")
        self.n20 = map.road("Images/lines/20.png")
        self.n21 = map.road("Images/lines/21.png")
        self.n22 = map.road("Images/lines/22.png")
        self.n23 = map.road("Images/lines/23.png")
        self.n24 = map.road("Images/lines/24.png")
        self.n25 = map.road("Images/lines/25.png")
        self.n26 = map.road("Images/lines/26.png")
        self.n27 = map.road("Images/lines/27.png")
        self.n28 = map.road("Images/lines/28.png")
        self.n29 = map.road("Images/lines/29.png")
        self.n30 = map.road("Images/lines/30.png")
        self.n31 = map.road("Images/lines/31.png")
        self.n32 = map.road("Images/lines/32.png")
        self.n33 = map.road("Images/lines/33.png")
        self.n34 = map.road("Images/lines/34.png")
        self.n35 = map.road("Images/lines/35.png")
        self.n36 = map.road("Images/lines/36.png")
        self.n37 = map.road("Images/lines/37.png")
        self.n38 = map.road("Images/lines/38.png")
        self.n39 = map.road("Images/lines/39.png")
        self.n40 = map.road("Images/lines/40.png")
        self.n41 = map.road("Images/lines/41.png")
        self.n42 = map.road("Images/lines/42.png")
        self.n43 = map.road("Images/lines/43.png")
        self.n44 = map.road("Images/lines/44.png")
        self.n45 = map.road("Images/lines/45.png")
        self.n46 = map.road("Images/lines/46.png")
        self.n47 = map.road("Images/lines/47.png")
        self.n48 = map.road("Images/lines/48.png")
        self.n49 = map.road("Images/lines/49.png")
        self.n50 = map.road("Images/lines/50.png")
        self.n51 = map.road("Images/lines/51.png")
        self.n52 = map.road("Images/lines/52.png")
        self.n53 = map.road("Images/lines/53.png")
        self.n54 = map.road("Images/lines/54.png")
        self.n55 = map.road("Images/lines/55.png")
        self.n56 = map.road("Images/lines/56.png")
        self.n57 = map.road("Images/lines/57.png")
        self.n58 = map.road("Images/lines/58.png")
        self.n59 = map.road("Images/lines/59.png")
        self.n60 = map.road("Images/lines/60.png")
        self.n61 = map.road("Images/lines/61.png")

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
        self.thing = map.mapObject("Images/lines/38.png")

        self.names = []
        x = 0
        for i in self.roads:
            x += 1
            i.name = str(x)
            self.names.append(str(x))
        self.names.pop()

        self.setup_UI(self)
        self.view.show()

        self.Alist = []
        self.Blist = []

        self.pointA_entry.activated.connect(self.showroadsA)
        self.pointB_entry.activated.connect(self.showroadsB)

        self.find_path_button.pressed.connect(self.yeet)

    def showroadsA(self):
        for i in self.Alist:
            if not i in self.Blist:
                self.scene.removeItem(i)
            self.Alist.remove(i)

        self.curroad = int(self.pointA_entry.currentText())
        self.Alist.append(self.roads[self.curroad])
        self.scene.addItem(self.roads[self.curroad])

    def showroadsB(self):
        for i in self.Blist:
            if not i in self.Alist:
                self.scene.removeItem(i)
            self.Blist.remove(i)

        self.curroad = int(self.pointB_entry.currentText())
        self.Blist.append(self.roads[self.curroad])
        self.scene.addItem(self.roads[self.curroad])

    def yeet(self):
        self.view.show()
        self.curroad = self.Alist[0]
        self.first = self.Alist[0]
        self.dest = self.Blist[0]
        self.next = self.curroad.connected[random.randrange(0, len(self.curroad.connected))]
        self.scene.addItem(self.next)
        self.curroad = self.next
        while (self.curroad != self.dest):
            self.next = self.curroad.connected[random.randrange(0, len(self.curroad.connected))]
            self.next.visited += 1
            self.scene.addItem(self.next)
            self.curroad = self.next

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

        # Adds a reset button to the pause menu
        self.resetButton = QPushButton()
        self.resetButton.setText("Reset")
        self.resetButton.setFont(QFont("Times", 10, QFont.Weight.Medium))
        self.resetButton.setStyleSheet("background-color: lightGray;"
                                             "color: black;"
                                             "border-style: outset;"
                                             "border-width: 1px;"
                                             "border-color: black;"
                                             "min-width: 50 em;"
                                             "max-width: 50 em;"
                                             "min-height: 15 em;"
                                             "max-height: 15 em;"
                                             "padding: 6 px;")
        self.resetButton.clicked.connect(self.resetClicked)
        self.settingsMenu.addButton(self.resetButton, QMessageBox.ButtonRole.DestructiveRole)

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

    def resetClicked(self):
        QApplication.closeAllWindows()

        self.window = Main_Window()
    
    def exitClicked(self, event):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Main_Window()
    #window.show()

    sys.exit(app.exec())

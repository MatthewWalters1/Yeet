from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QColor, QPalette, QFont, QBrush, QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 600) #Set window size and color
        palette = self.palette()
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

        self.scene = QGraphicsScene(-50, -50, 600, 600)

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
        self.resumeButton.clicked.connect(self.resumeClicked)
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
    
    def resumeClicked(self, event):
        print("hi")

    def exitClicked(self, event):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
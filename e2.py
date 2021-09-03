'''
    example.py
    Matthew Walters

    simple text box application (use a header)
'''
import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        #this is the QMainWindow default constructor
        super().__init__()
        #Window's constructor can be whatever you want in addition to that
        self.setGeometry(500, 500, 500, 500)

        self.setWindowTitle("Our Example Application")

        #created our central widget
        central_widget = QWidget()

        #created a vertical box layout
        layout = QVBoxLayout()

        #created a text box
        self.text_box = QTextEdit()

        #add text_box widget to layout
        layout.addWidget(self.text_box)

        #add the layout to our central widget
        central_widget.setLayout(layout)

        #add the central widget to the main window
        self.setCentralWidget(central_widget)

        #display a status bar (at the bottom of the window)
        self.statusBar().showMessage("Important Status...")

        #create a File toolbar with a save option
        file_menu = self.menuBar().addMenu("File")
        
        #just look up what icons you want
        save_icon = QIcon.fromTheme("document-save")
        self.save_action = QAction(save_icon, "Save", self)
        self.save_action.setShortcut("Ctrl+S")
        def SaveEvent(self):
            buffer = self.text_box.toPlainText()

            file_dialog = QFileDialog(self)

            file_name = file_dialog.getSaveFileName(self, "Save File")

            #this is not how you should do it, but for example purposes...
            print(file_name)
            #without clarifying, this assumes there is a file_name[0]
            f = open(file_name[0], 'w')
            f.write(buffer)
            f.close()
            self.statusBar().showMessage("Saved...")
            
        self.save_action.triggered.connect(SaveEvent)
        file_menu.addAction(self.save_action)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec())
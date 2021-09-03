'''
    example.py
    Matthew Walters

    simple text box application (use a header)
'''
import sys
from PyQt6.QtWidgets import QTextEdit, QVBoxLayout, QWidget, QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()

window.setGeometry(10, 10, 100, 100)

window.setWindowTitle("Our Example Application")

#created our central widget
central_widget = QWidget()
#fancy comment
#created a vertical box layout
layout = QVBoxLayout()

#created a text box
text_box = QTextEdit()

#add text_box widget to layout
layout.addWidget(text_box)

#add the layout to our central widget
central_widget.setLayout(layout)

#add the central widget to the main window
window.setCentralWidget(central_widget)


window.show()

sys.exit(app.exec())
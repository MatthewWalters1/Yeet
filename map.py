from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap

class mapObject(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
        self.setPixmap(QPixmap("Images/map.png"))
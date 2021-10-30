from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem
from PyQt6.QtGui import QPixmap

class mapObject(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
        self.setPixmap(QPixmap("Images/map3.jpg"))

class road(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
        self.connected = []
        
class edge():
    def __init__(self):
        self.distance = random.randrange(0,10)
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem
from PyQt6.QtGui import QPixmap
import random

class mapObject(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
        self.setPixmap(QPixmap("Images/map3.jpg"))

class road(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
        self.connected = []
        # self.setPixmap(imageName)

class edge():
    def __init__(self):
        self.distance = random.randrange(0,10)
        self.fakeroad = road()
        self.to = self.fakeroad
        self.frum = self.fakeroad
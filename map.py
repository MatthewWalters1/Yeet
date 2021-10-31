from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem
from PyQt6.QtGui import QPixmap
import random

class mapObject(QGraphicsPixmapItem):
    def __init__(self, imageName):
        super().__init__()
        self.setPixmap(QPixmap(imageName))

class road(QGraphicsPixmapItem):
    def __init__(self, imageName):
        super().__init__()
        self.connected = []
        self.setPixmap(QPixmap(imageName))
        self.name = int
        self.visited = 0

class edge():
    def __init__(self):
        self.distance = random.randrange(0,10)
        self.fakeroad = road("Images/trashmapsicon.png")
        self.to = self.fakeroad
        self.frum = self.fakeroad
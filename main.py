from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from node_graphics_scene import QDMGraphicsScene
from node_graphics_view import QDMGraphicsView
import sys
from Ui_MainWindow import Ui_MainWindow
from node_scene import Scene
from node_node import Node


class NodeEditWind(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(NodeEditWind, self).__init__(parent)
        self.setupUi(self)

        self.scene = Scene()
        self.grScene = self.scene.grScene
        self.graphicsView = QDMGraphicsView(self.grScene)
        self.horizontalLayout.addWidget(self.graphicsView)

        node = Node(self.scene, "这是一个节点")
        #self.addDebugContent()

    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        text = self.grScene.addText("不错！！！", QFont("Ubuntu"))
        text.setFlag(QGraphicsItem.ItemIsSelectable)
        text.setFlag(QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))

        widget1 = QPushButton("Hello world")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setFlag(QGraphicsItem.ItemIsMovable)
        proxy1.setPos(0, 30)

        widget2 = QTextEdit()
        proxy2 = self.grScene.addWidget(widget2)
        proxy2.setFlag(QGraphicsItem.ItemIsSelectable)
        proxy2.setPos(0, 60)

        line = self.grScene.addLine(-200, -200, 400, -100, outlinePen)
        line.setFlag(QGraphicsItem.ItemIsSelectable)
        line.setFlag(QGraphicsItem.ItemIsMovable)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = NodeEditWind()
    main_win.show()
    sys.exit(app.exec_())
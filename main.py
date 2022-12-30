from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from node_graphics_scene import QDMGraphicsScene
from node_graphics_view import QDMGraphicsView
import sys
from Ui_MainWindow import Ui_MainWindow
from node_scene import Scene
from node_node import Node
from node_edge import Edge

class NodeEditWind(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(NodeEditWind, self).__init__(parent)
        self.setupUi(self)

        self.scene = Scene()
        self.grScene = self.scene.grScene
        self.graphicsView = QDMGraphicsView(self.grScene)
        self.horizontalLayout.addWidget(self.graphicsView)

        self.addNode()
        #self.addDebugContent()

    def addNode(self):
        node1 = Node(self.scene,"这是第一个节点",inputs=[1,2,3],outputs=[1])
        node2 = Node(self.scene,"这是第二个节点",inputs=[1,2,3],outputs=[1])
        node3 = Node(self.scene,"这是第三个节点",inputs=[1,2,3],outputs=[1])

        node1.setPos(-350, -250)
        node2.setPos(-75, 0)
        node3.setPos(200, -150)

        edge1 = Edge(self.scene, node1.outputs[0],node2.inputs[0])
        edge2 = Edge(self.scene, node2.outputs[0],node3.inputs[0], type=2)
        

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
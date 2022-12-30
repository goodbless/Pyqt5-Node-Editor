from node_graphics_node import QMGraphicsNode
from node_widget import QDMNodeContentWidget
from PyQt5.QtCore import QFile

class Node():
    def __init__(self, scene, title="Undefined Node", inputs=[], outputs=[]) -> None:
        self.scene = scene

        self.title = title

        self.content = QDMNodeContentWidget()
        self.grNode = QMGraphicsNode(self, self.title)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.inputs = inputs
        self.outputs = outputs

        self.stylesheet_filename = 'qss/nodestyle.qss'
        self.loadStylesheet(self.stylesheet_filename)

    def loadStylesheet(self, filename):
        print('STYLE loading', filename)
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        self.content.setStyleSheet(str(stylesheet, encoding='utf-8'))
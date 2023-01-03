from node_graphics_node import QMGraphicsNode
from node_widget import QDMNodeContentWidget
from PyQt5.QtCore import QFile
from node_socket import *

class Node():
    def __init__(self, scene, title="Undefined Node", inputs=[], outputs=[]) -> None:
        self.scene = scene

        self.title = title

        self.content = QDMNodeContentWidget()
        self.grNode = QMGraphicsNode(self, self.title)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.socket_spacing = 22

        self.inputs = []
        self.outputs = []

        counter = 0
        for item in inputs:
            socket = Socket(node=self, index=counter, position=LEFT_TOP, socket_type=item)
            counter +=1
            self.inputs.append(socket)

        counter = 0
        for item in outputs:
            socket = Socket(node=self, index=counter, position=RIGHT_BOTTOM, socket_type=item)
            counter +=1
            self.outputs.append(socket)

        self.stylesheet_filename = 'qss/nodestyle.qss'
        self.loadStylesheet(self.stylesheet_filename)

    def getSocketPosition(self, index, position):
        if position in (LEFT_TOP, LEFT_BOTTOM):
            x = 0
        else:
            x = self.grNode.width

        if position in (LEFT_BOTTOM, RIGHT_BOTTOM):
            y = -index * self.socket_spacing + self.grNode.height - self.grNode._padding - self.grNode.edge_size
        else:
            y = index * self.socket_spacing + self.grNode.title_height + self.grNode._padding + self.grNode.edge_size

        return [x, y]

    def loadStylesheet(self, filename):
        print('STYLE loading', filename)
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        self.content.setStyleSheet(str(stylesheet, encoding='utf-8'))

    @property
    def pos(self):
        return self.grNode.pos()

    def setPos(self, x, y):
        self.grNode.setPos(x, y)

    def updateConnectedEdges(self):
        for socket in self.inputs + self.outputs:
            if socket.hasEdge():
                socket.edge.updatePosition()
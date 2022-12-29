from node_graphics_node import QMGraphicsNode

class Node():
    def __init__(self, scene, title="Undefined Node") -> None:
        self.scene = scene

        self.title = title

        self.grNode = QMGraphicsNode(self, self.title)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.inputs = []
        self.output = []
from node_graphics_edge import *

EDGE_TYPE_DIRECT = 1
EDGE_TYPE_BEZIER = 2

class Edge:
    def __init__(self, scene, start_socket, end_socket, type=EDGE_TYPE_DIRECT) -> None:
        self.scene = scene

        self.start_socket = start_socket
        self.end_socket = end_socket

        if type == EDGE_TYPE_DIRECT:
            self.grEdge = QDMCGraphicsEdgeDirect(self)
        else:
            self.grEdge = QDMGraphicsEdgeBezier(self)

        self.scene.grScene.addItem(self.grEdge)
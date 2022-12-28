from PyQt5.QtWidgets import QMainWindow, QGraphicsView, QApplication, QSizePolicy
from PyQt5.QtCore import *
from node_graphics_scene import QDMGraphicsScene
import sys
from Ui_MainWindow import Ui_MainWindow


class NodeEditWind(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(NodeEditWind, self).__init__(parent)
        self.setupUi(self)

        self.grScene = QDMGraphicsScene()

        self.graphicsView.setScene(self.grScene)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = NodeEditWind()
    main_win.show()
    sys.exit(app.exec_())
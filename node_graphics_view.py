from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QDMGraphicsView(QGraphicsView):
    def __init__(self, grScene, parent = None):
        super().__init__(parent)
        self.grScene = grScene

        self.zoomInFactor = 1.25
        self.zoom = 5
        self.zoomStep = 1
        self.zoomClamp = False
        self.zoomRange = [0,10]

        self.initUI()
        self.setScene(self.grScene)

    def initUI(self):
        self.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.HighQualityAntialiasing | QPainter.RenderHint.TextAntialiasing | QPainter.RenderHint.SmoothPixmapTransform)

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MidButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonPress(event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MidButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonRelease(event)
        else:
            super().mouseReleaseEvent(event)

    def leftMouseButtonPress(self, event: QMouseEvent) -> None:
        # self.setDragMode(QGraphicsView.ScrollHandDrag)
        return super().mousePressEvent(event)

    def leftMouseButtonRelease(self, event: QMouseEvent) -> None:
        # self.setDragMode(QGraphicsView.NoDrag)
        return super().mouseReleaseEvent(event)

    def rightMouseButtonPress(self, event: QMouseEvent) -> None:
        return super().mousePressEvent(event)

    def rightMouseButtonRelease(self, event: QMouseEvent) -> None:
        return super().mouseReleaseEvent(event)


    def middleMouseButtonPress(self, event: QMouseEvent):
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(), Qt.LeftButton, Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(releaseEvent)

        self.setDragMode(QGraphicsView.ScrollHandDrag)

        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(), Qt.LeftButton, event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(fakeEvent)

    def middleMouseButtonRelease(self, event: QMouseEvent):
        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(), Qt.LeftButton, event.buttons() | Qt.LeftButton, event.modifiers())
        super().mouseReleaseEvent(fakeEvent)
        self.setDragMode(QGraphicsView.NoDrag)


    def wheelEvent(self, event: QWheelEvent) -> None:
        zoomOutFactor = 1/self.zoomInFactor

        if event.angleDelta().y()>0:
            zoomFactor = self.zoomInFactor
            self.zoom += self.zoomStep
        else:
            zoomFactor = zoomOutFactor
            self.zoom -= self.zoomStep

        clamped = False
        if self.zoom < self.zoomRange[0]:
            self.zoom, clamped = self.zoomRange[0],True
        if self.zoom > self.zoomRange[1]:
            self.zoom, clamped = self.zoomRange[1],True

        if not clamped or self.zoomClamp:
            self.scale(zoomFactor, zoomFactor)

    


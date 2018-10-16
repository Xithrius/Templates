import sys

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

import numpy as np
import random


class MyScene(QtWidgets.QGraphicsScene):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = window

    def mousePressEvent(self, event):
        self.window.clicked(event.scenePos().x(),
                            event.scenePos().y(), event.button())

    def mouseDoubleClickEvent(self, event):
        self.window.explode(event.scenePos().x(),
                            event.scenePos().y(), event.button())


class Window(QtWidgets.QWidget):
    COVERED = QtGui.QBrush(QtGui.QColor(100, 100, 100))
    BOMBED = QtGui.QBrush(QtGui.QColor(255, 100, 100))
    FLAGGED = QtGui.QBrush(QtGui.QColor(100, 100, 255))

    def __init__(self, title, tileSize=15, boardShape=(30, 16), numBombs=99):
        super(Window, self).__init__()

        self.boardShape = boardShape
        self.numBombs = numBombs
        self.numSafe = boardShape[0] * boardShape[1] - numBombs

        self.tileSize = tileSize

        self.numClicks = 0

        self.bombs = np.zeros(self.boardShape, dtype=bool)
        self.flagged = np.zeros(self.boardShape, dtype=bool)
        self.surrounding = np.ones(self.boardShape) * -1
        self.texts = []
        self.lines = []

        self.playing = True

        self.scene = MyScene(self)

        sceneRect = QtCore.QRectF(0,
                                  0,
                                  self.boardShape[0] * tileSize,
                                  self.boardShape[1] * tileSize)

        self.view = QtWidgets.QGraphicsView(self.scene)

        self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.view.setFixedSize(self.boardShape[0] * tileSize,
                               self.boardShape[1] * tileSize)
        self.view.setSceneRect(sceneRect)

        layout = QtWidgets.QGridLayout()

        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum,
                           QtWidgets.QSizePolicy.Minimum)

        layout.addWidget(self.view, 0, 0)

        self.restartButton = QtWidgets.QPushButton('Restart')

        self.restartButton.pressed.connect(self.restartGame)

        layout.addWidget(self.restartButton, 1, 0)

        self.populateBombs()
        self.populateCovers(1)

        self.setLayout(layout)

        self.setWindowTitle(title)

        self.setFixedSize(self.size())

        self.center()

        self.view.viewport().installEventFilter(self)

        self.show()

    def restartGame(self):
        for c in self.covers:
            c.setOpacity(1)
            c.setBrush(Window.COVERED)

        self.numClicks = 0

        self.bombs = np.zeros(self.boardShape, dtype=bool)
        self.flagged = np.zeros(self.boardShape, dtype=bool)
        self.surrounding = np.ones(self.boardShape) * -1

        for t in self.texts:
            self.scene.removeItem(t)

        self.texts = []

        for t in self.lines:
            self.scene.removeItem(t)

        self.lines = []

        self.populateBombs()

        self.playing = True

    def populateBombs(self):
        assert self.numBombs < self.boardShape[0] * self.boardShape[1]

        for i in range(self.numBombs):
            x = random.randrange(self.boardShape[0])
            y = random.randrange(self.boardShape[1])

            while self.bombs[x, y]:
                x = random.randrange(self.boardShape[0])
                y = random.randrange(self.boardShape[1])

            self.bombs[x, y] = True

    def eventFilter(self, obj, event):
        if not self.playing:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                return True
        if obj == self.view.viewport() and event.type() == QtCore.QEvent.Wheel:
            return True

        return False

    def populateCovers(self, borderWidth):
        self.covers = []

        for i in range(self.boardShape[0] * self.boardShape[1]):
            pen = QtGui.QPen()

            pen.setWidthF(borderWidth)

            vx, vy = self.indexToXY(i)
            x, y = self.viewToScreen(vx, vy)

            rect = self.scene.addRect(QtCore.QRectF(x, y,
                                                    self.tileSize - borderWidth,
                                                    self.tileSize - borderWidth),
                                      pen=pen,
                                      brush=Window.COVERED)

            self.covers.append(rect)

    def getNumberAt(self, x, y):
        if self.surrounding[x, y] > -1:
            return self.surrounding[x, y]

        total = 0

        for dx in range(max(0, x - 1), min(self.boardShape[0], x + 2)):
            for dy in range(max(0, y - 1), min(self.boardShape[1], y + 2)):
                if dx != x or dy != y:
                    total += self.bombs[dx, dy]

        self.surrounding[x, y] = total

        return total

    def addNumber(self, vx, vy):
        x, y = self.viewToScreen(vx, vy)

        n = self.getNumberAt(vx, vy)

        if n > 0:
            text = self.scene.addText('%i' % n)
            text.setPos(x, y)
            text.setZValue(-1)

            self.texts.append(text)

    def indexToXY(self, i):
        return i % self.boardShape[0], i // self.boardShape[0]

    def xyToIndex(self, x, y):
        return int(y * self.boardShape[0] + x)

    def coverAt(self, x, y):
        return self.covers[self.xyToIndex(*self.screenToView(x, y))]

    def revealBombs(self):
        for i in range(len(self.covers)):
            cover = self.covers[i]
            if self.bombs[self.indexToXY(i)]:
                cover.setBrush(Window.BOMBED)
            else:
                if cover.brush() == Window.FLAGGED:
                    x, y = self.viewToScreen(*self.indexToXY(i))

                    l0 = self.scene.addLine(
                        x, y, x + self.tileSize, y + self.tileSize)
                    l1 = self.scene.addLine(x, y + self.tileSize,
                                            x + self.tileSize, y)

                    self.lines.append(l0)
                    self.lines.append(l1)

    def explode(self, x, y, button):
        x, y = int(x), int(y)
        vx, vy = self.screenToView(x, y)

        if button != 1:
            return

        cover = self.coverAt(x, y)
        if cover.opacity() != 0:
            return

        for dx in range(max(0, vx - 1), min(self.boardShape[0], vx + 2)):
            for dy in range(max(0, vy - 1), min(self.boardShape[1], vy + 2)):
                if dx != vx or dy != vy:
                    self.clicked(*self.viewToScreen(dx, dy), 1)

    def clicked(self, x, y, button):
        x, y = int(x), int(y)
        vx, vy = self.screenToView(x, y)
        cover = self.coverAt(x, y)
        if cover.opacity() == 0:
            return

        if button == 1:
            if cover.brush() == Window.FLAGGED:
                return

            if self.bombs[self.screenToView(x, y)]:
                if self.numClicks > 0:
                    print('Defeat')
                    self.revealBombs()

                    self.playing = False
                    return
                else:
                    i = 0
                    while self.bombs[self.indexToXY(i)]:
                        i += 1

                        if i >= len(self.covers):
                            raise ValueError('All mines')

                    self.bombs[self.indexToXY(i)] = True
                    self.bombs[self.screenToView(x, y)] = False

            self.uncover(vx, vy)

            if self.numClicks == self.numSafe:
                print('Victory')  # TODO add victory condition
                self.revealBombs()
                self.playing = False
        elif button == 2:
            if cover.brush() == Window.COVERED:
                cover.setBrush(Window.FLAGGED)
            elif cover.brush() == Window.FLAGGED:
                cover.setBrush(Window.COVERED)

    def uncover(self, x, y):
        cover = self.covers[self.xyToIndex(x, y)]
        if cover.opacity() == 0:
            return

        cover.setOpacity(0)
        self.addNumber(x, y)
        self.numClicks += 1

        if self.getNumberAt(x, y) == 0:
            for dx in range(max(0, x - 1), min(self.boardShape[0], x + 2)):
                for dy in range(max(0, y - 1), min(self.boardShape[1], y + 2)):
                    if dx != x or dy != y:
                        self.uncover(dx, dy)

    def screenToView(self, x, y):
        return (x // self.tileSize, y // self.tileSize)

    def viewToScreen(self, x, y):
        return (x * self.tileSize, y * self.tileSize)

    def center(self):
        windowGeometery = self.frameGeometry()
        center = QtWidgets.QDesktopWidget().availableGeometry().center()
        windowGeometery.moveCenter(center)
        self.move(windowGeometery.topLeft())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Window('Minesweeper', 20)
    sys.exit(app.exec_())

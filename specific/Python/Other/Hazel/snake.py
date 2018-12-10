import sys

from PyQt5 import QtWidgets, QtGui, QtCore

from collections import deque
import random


class Window(QtWidgets.QWidget):
    EMPTY = QtGui.QBrush(QtGui.QColor(20, 20, 20))
    DEAD = QtGui.QBrush(QtGui.QColor(200, 20, 20))
    SNAKE = QtGui.QBrush(QtGui.QColor(200, 200, 20))
    FOOD = QtGui.QBrush(QtGui.QColor(20, 200, 20))

    DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def __init__(self, title, shape, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = title
        self.shape = shape

        self.speed = 200
        self.step = 1

        self.scene = QtWidgets.QGraphicsScene()

        self.view = QtWidgets.QGraphicsView(self.scene)

        sceneRect = QtCore.QRectF(0, 0, shape[0] * 15, shape[1] * 15)

        self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.view.setFixedSize(shape[0] * 15 + 2, shape[1] * 15 + 2)
        self.view.setSceneRect(sceneRect)

        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum,
                           QtWidgets.QSizePolicy.Minimum)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.view, 0, 0)

        self.initGame()

        self.setLayout(layout)

        self.setWindowTitle(title)

        self.resize(self.shape[0] * 15 + 30, self.shape[0] * 15 + 20)

        self.setFixedSize(self.size())

        self.center()

        self.view.viewport().installEventFilter(self)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(self.speed)

        self.show()

    def die(self):
        self.timer.stop()

        for part in self.snake:
            self.setDead(*part)

    def spawnFood(self):
        x, y = random.randrange(self.shape[0]), random.randrange(self.shape[1])

        while (x, y) in self.snake:
            x, y = random.randrange(
                self.shape[0]), random.randrange(self.shape[1])

        self.setFood(x, y)

    def setupGame(self):
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                self.setEmpty(x, y)

        self.speed = 200

        self.direction = 0
        self.currentDirection = 0
        self.directionQueue = deque()
        self.snake = deque([(1, 1)])
        self.head = (1, 1)

        self.length = 1

        self.setSnake(1, 1)

        self.spawnFood()

        self.timer.start(self.speed)

    def initGame(self):
        self.tiles = []
        for y in range(self.shape[1]):
            row = []
            for x in range(self.shape[0]):
                rect = self.scene.addRect(QtCore.QRectF(x * 15, y * 15, 15, 15),
                                          brush=Window.EMPTY)
                row.append(rect)
            self.tiles.append(row)

        self.direction = 0
        self.currentDirection = 0
        self.directionQueue = deque()
        self.snake = deque([(1, 1)])
        self.head = (1, 1)

        self.length = 1

        self.setSnake(1, 1)

        self.spawnFood()

    def eventFilter(self, obj, event):
        if obj == self.view.viewport() and event.type() == QtCore.QEvent.Wheel:
            return True

        return False

    def setFood(self, x, y):
        self.getTile(x, y).setBrush(Window.FOOD)

    def setEmpty(self, x, y):
        self.getTile(x, y).setBrush(Window.EMPTY)

    def setSnake(self, x, y):
        self.getTile(x, y).setBrush(Window.SNAKE)

    def setDead(self, x, y):
        self.getTile(x, y).setBrush(Window.DEAD)

    def isFood(self, x, y):
        return self.getTile(x, y).brush() == Window.FOOD

    def getTile(self, x, y):
        return self.tiles[y][x]

    def setDirection(self, d):
        if (d + 2) % 4 == self.currentDirection:
            return

        self.directionQueue.append(d)

    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_D:
            self.setDirection(0)
        if key == QtCore.Qt.Key_W:
            self.setDirection(1)
        if key == QtCore.Qt.Key_A:
            self.setDirection(2)
        if key == QtCore.Qt.Key_S:
            self.setDirection(3)

    def outOfBounds(self, p):
        x, y = p

        return x < 0 or x >= self.shape[0] or y < 0 or y >= self.shape[1]

    def tick(self):
        if len(self.directionQueue) > 0:
            d = self.directionQueue.popleft()
        else:
            d = self.direction

        while len(self.directionQueue) > 0 and d == self.direction:
            d = self.directionQueue.popleft()

        self.direction = d

        delta = Window.DIRECTIONS[self.direction]
        newHead = tuple(a + b for a, b in zip(self.head, delta))

        if self.outOfBounds(newHead):
            print('Loss: %i length' % self.length)
            self.die()
            return

        if self.isFood(*newHead):
            self.length += self.step

            # self.speed /= 2
            # self.setSpeed(self.speed // 2)

            self.spawnFood()

        self.head = newHead

        if len(self.snake) >= self.length:
            tail = self.snake.popleft()

            self.setEmpty(*tail)

        if newHead in self.snake:
            print('Loss: %i length' % self.length)
            self.die()
            return

        self.snake.append(newHead)

        self.setSnake(*newHead)

        self.currentDirection = self.direction

    def setSpeed(self, speed):
        if speed < 1:
            speed = 1

        self.speed = speed

        print(speed)

        self.timer.stop()
        self.timer.start(self.speed)

    def center(self):
        windowGeometery = self.frameGeometry()
        center = QtWidgets.QDesktopWidget().availableGeometry().center()
        windowGeometery.moveCenter(center)
        self.move(windowGeometery.topLeft())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Window('Snake', (20, 20))
    sys.exit(app.exec_())

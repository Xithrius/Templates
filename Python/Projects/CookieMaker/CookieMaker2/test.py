from PyQt5.QtWidgets import *
app = QApplication([]) # creates qapplication
app.setStyle('Fusion')
app.setStyleSheet("addWidget { margin: 10ex; }")

window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_() # run until closed by user
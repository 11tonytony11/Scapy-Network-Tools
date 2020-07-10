import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QTabWidget, QLineEdit


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Init window
        self.setWindowTitle("NET UTILS By TonyM")
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Init Tab Widget
        tabwidget = QTabWidget()
        tabwidget.addTab(Tab(), "Ping")
        tabwidget.addTab(Tab(), "Traceroute")
        tabwidget.addTab(Tab(), "NSlookup")

        # Init exec button
        run = QtWidgets.QPushButton("Execute")
        run.clicked.connect(lambda: update_gui(tabwidget.currentIndex()))

        # Add all widgets to layout
        layout.addWidget(tabwidget)
        layout.addWidget(run)

class Tab(QWidget):
    def __init__(self):
        super().__init__()

        # Init Window
        dst = QLabel("URL/IP:")
        field = QLineEdit()

        # Init Layout
        layout = QVBoxLayout()
        self.setLayout((layout))

        # Add Widgets to layout
        layout.addWidget(dst)
        layout.addWidget(field)


def update_gui(option):
    print(option)

    # HOWTO Write: obj.layout().addWidget(QLabel("Hello DNS"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())
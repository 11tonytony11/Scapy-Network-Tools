import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QTabWidget, QLineEdit, QMenuBar, QAction

from ping import ping
from traceroute import trace
from nslookup import nslookup


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Init window
        self.setWindowTitle("NET UTILS By TonyM")
        self.menuBar = QMenuBar()
        self.resize(600, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Init menu bar
        file = self.menuBar.addMenu("File")
        help = self.menuBar.addMenu("Help")

        # Create buttons
        info = QAction("Useful Information", self)
        settings = QAction("Settings", self)
        about = QAction("about", self)
        quit = QAction("Quit", self)

        # Connect to backend
        quit.triggered.connect(lambda: sys.exit())
        settings.triggered.connect(lambda: print("Imaging settings work"))
        about.triggered.connect(lambda: print("Imaging you see data about the software"))
        info.triggered.connect(lambda: print("Imagine smart information about ping trace and nslookup"))

        # Init Tabs
        self.ping = Tab()
        self.trace = Tab()
        self.dns = Tab()

        # Init Tab Widget
        self.tabwidget = QTabWidget()
        self.tabwidget.addTab(self.ping, "Ping")
        self.tabwidget.addTab(self.trace, "Traceroute")
        self.tabwidget.addTab(self.dns, "NSLookup")

        # Init exec button
        run = QtWidgets.QPushButton("Execute")
        run.clicked.connect(lambda: update_gui(self.tabwidget.currentIndex(), self))
        run.setFixedSize(100, 30)

        # Add all widgets to layout
        layout.addWidget(self.menuBar, 0)
        layout.addWidget(self.tabwidget)
        file.addAction(settings)
        file.addAction(quit)
        help.addAction(info)
        help.addAction(about)
        layout.addWidget(run)

class Tab(QWidget):
    def __init__(self):
        super().__init__()

        # Init Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Init Window
        self.field = QLineEdit()
        self.field.setPlaceholderText("Enter URL/IP")
        self.tmp = QLabel("")  # Fix responsive issue
        
        # Add widgets to layout
        layout.addWidget(self.field, 0)
        layout.addWidget(QLabel(""))
        layout.addWidget(self.tmp)


def update_gui(option, obj):
    if option == 0:
        tmp = obj.ping.tmp.text() + "\n"
        obj.ping.tmp.setText(tmp + ping(obj.ping.field.text(), 4)[0])

    if option == 1:
        tmp = obj.trace.tmp.text() + "\n"
        obj.trace.tmp.setText(tmp + trace(obj.trace.field.text()))

    if option == 2:
        tmp = obj.dns.tmp.text() + "\n"
        obj.dns.tmp.setText(tmp + nslookup(obj.dns.field.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())
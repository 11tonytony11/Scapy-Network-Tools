import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QTabWidget, QLineEdit, QMenuBar, QAction, \
    QDialog, QGridLayout, QPushButton

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
        settings.triggered.connect(self.open_settings)
        about.triggered.connect(self.open_about)
        info.triggered.connect(self.open_information)

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

    def open_settings(self):

        # Init window
        settings = QDialog(self)
        settings.setWindowFlags(self.windowFlags() ^ Qt.WindowStaysOnTopHint)
        settings.setWindowTitle("Settings")
        settings.resize(230, 120)

        # Create layout
        layout = QGridLayout()
        settings.setLayout(layout)

        # Create all labels
        ping_iters  = QLabel('Ping Iterations:')
        ping_size   = QLabel('Ping data size:')
        record_type = QLabel('DNS Record type:')
        DNS_server  = QLabel('DNS Server:')

        # Create fields
        settings.lineEdit_ping_iters  = QLineEdit()
        settings.lineEdit_ping_size   = QLineEdit()
        settings.lineEdit_record_type = QLineEdit()
        settings.lineEdit_DNS_server  = QLineEdit()

        # Add fields to gui
        settings.layout().addWidget(ping_iters, 0, 0)
        settings.layout().addWidget(settings.lineEdit_ping_iters, 0, 1)
        settings.layout().addWidget(ping_size, 1, 0)
        settings.layout().addWidget(settings.lineEdit_ping_size, 1, 1)
        settings.layout().addWidget(record_type, 2, 0)
        settings.layout().addWidget(settings.lineEdit_record_type, 2, 1)
        settings.layout().addWidget(DNS_server, 3, 0)
        settings.layout().addWidget(settings.lineEdit_DNS_server, 3, 1)

        # Apply button
        apply_button = QPushButton('Apply')
        settings.layout().addWidget(apply_button, 4, 0, 1, 2)
        apply_button.clicked.connect(lambda: print("Imagine new settings were applied"))
        settings.show()

    def open_about(self):

        # Init window
        about = QDialog(self)
        about.setWindowFlags(self.windowFlags() ^ Qt.WindowStaysOnTopHint)
        about.setWindowTitle("About")
        about.resize(200, 200)

        # Create layout
        layout = QVBoxLayout()
        about.setLayout(layout)

        layout.addWidget(QLabel("This is an open source NET Utils software that is being developed by Tony Malinkovich."))
        about.show()

    def open_information(self):

        # Init window
        about = QDialog(self)
        about.setWindowFlags(self.windowFlags() ^ Qt.WindowStaysOnTopHint)
        about.setWindowTitle("About")
        about.resize(200, 200)

        # Create layout
        layout = QVBoxLayout()
        about.setLayout(layout)

        layout.addWidget(QLabel("Ping is a cat."))
        layout.addWidget(QLabel("traceroute is the internet's waze."))
        layout.addWidget(QLabel("NSlookup is the internet's tour guide."))
        about.show()

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


#For later: settings.lineEdit_xxxxxx.setPlaceholderText('text')
# Python StopWatch with PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00")
        self.start_button = QPushButton("Start", self)
        self.reset_button = QPushButton("Reset", self)
        self.stop_button = QPushButton("Stop", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("StopWatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.reset_button)
        hbox.addWidget(self.stop_button)
        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel {
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton {
                font-size: 50px;
            }
            QLabel {
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 10px;
            }
                
        """)
        

    def start(self):
        pass

    def stop(self):
        pass

    def reset(self):
        pass

    def format_time(self, time):
        pass

    def update_display(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stop_watch = StopWatch()
    stop_watch.show()
    sys.exit(app.exec_())
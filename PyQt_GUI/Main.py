import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QTime, QTimer


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the button and label
        self.button = QPushButton('Click me!', self)
        self.label = QLabel('Time will go here', self)

        # Set the button and label positions
        self.button.move(20, 20)
        self.label.move(130, 22)

        # Connect the button's clicked signal to the showTime method
        self.button.clicked.connect(self.showTime)

        # Set the window title and show the window
        self.setWindowTitle('PyQt5 Time App')
        self.show()

    def showTime(self):
        # Get the current time and set the label's text
        time = QTime.currentTime()
        self.label.setText(time.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())





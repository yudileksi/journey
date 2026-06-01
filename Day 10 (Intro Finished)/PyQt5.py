

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle()


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__PyQt5__":
    main()

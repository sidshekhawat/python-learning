#PyQt5 Images

import os
image_path = os.path.join(os.path.dirname(__file__), "profile_pic.jpg")

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 500, 500)

        self.label = QLabel(self)
        self.label.setGeometry(100, 100, 500, 500)

        pixmap = QPixmap(image_path)

        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        self.label.setGeometry((self.width()  - self.label.width()) // 2,
                               (self.height() - self.label.height()) // 2, 
                                self.label.width(),
                                self.label.height())

   
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
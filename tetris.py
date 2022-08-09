import sys

from PyQt5.QtWidgets import QApplication, QWidget

from tetrisform import TetrisForm


def main():
    app = QApplication(sys.argv)
    wnd = TetrisForm(None)
    wnd.show()
    app.exec()


if __name__ == "__main__":
    main()

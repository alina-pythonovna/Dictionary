
import sys
# from argparse import ArgumentParser  # TODO: maybe that will be needed

from PyQt5 import QtWidgets
from appUI import UiMainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

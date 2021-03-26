import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QStatusBar


def index_added_to_itself(my_list):
    for i in list(range(len(my_list))):
        my_list[i] = my_list[i] + i
    return my_list


class Window(QMainWindow):

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Homework')
        self.setGeometry(100, 100, 450, 650)
        self.move(150, 250)
        self._create_menu()
        self._populate_result()
        self._create_status_bar()

    def _create_menu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _populate_result(self):

        self.setCentralWidget(QLabel(f'Task {str(index_added_to_itself([0, 1, 3, 5]))}\n'))

    def _create_status_bar(self):
        status = QStatusBar()
        status.showMessage(str(index_added_to_itself([0, 1, 3, 5])))
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

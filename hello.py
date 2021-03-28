import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QStatusBar


def index_added_to_itself(my_list):
    for i in list(range(len(my_list))):
        my_list[i] = my_list[i] + i
    return my_list


def return_indices_of_all_occurrences(my_list, target):
    result = list()
    for i in list(range(len(my_list))):
        if my_list[i] == target:
            result.append(i)
    return result


def return_length_of_integer(val):
    i = 0
    string = val
    if type(val) != str:
        string = str(val)
    for _ in string:
        i += 1
    return i


def inverts_keys_and_values_of_dictionary(input_dict):
    """NOTE: input_dict.items() method extracts (key, value) pairs from previous dictionary.
    Function writes a new key/value pair into the new dictionary for each item via for loop"""
    return {val: key for key, val in input_dict.items()}


outputData = [str(index_added_to_itself([0, 1, 3, 5])),
              str(return_indices_of_all_occurrences([2, 6, 7, 8], 7)),
              str(return_length_of_integer({2: 3, 3: 2, 'r': 2})),
              str(inverts_keys_and_values_of_dictionary({'fruit': 'apple', 'meat': 'beef'}))
              ]


class Window(QMainWindow):

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Homework')
        self.setGeometry(100, 100, 800, 650)
        self.move(550, 250)
        self._create_menu()
        self._populate_result()
        self._create_status_bar()

    def _create_menu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _populate_result(self):
        str_text = ''
        for answer in outputData:
            idx = outputData.index(answer) + 1
            str_text += ' <b><span style="color: red; font-size: 20px"><b>Task: </b></span> ' \
                        + '<span style="font-size: 20px"><b>' + str(idx) + '</b></span><br>' \
                        + '<span style="color: green;">' \
                        + '<span style="font-size: 15px"><b>' + answer + '</b></span><br>' \
                        + '</span><br><br> '

        self.setCentralWidget(QLabel(f'<div>{str_text}\n</div>'))

    def _create_status_bar(self):
        status = QStatusBar()
        status.showMessage('End')
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

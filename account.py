import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit, QMessageBox, QInputDialog


class BankAccount:
    def __init__(self, user, pin, amount):
        self.user = user
        self.pin = pin
        self.amount = amount


class MainWindow(QMainWindow):  # inherit application's main window

    width = 850
    height = 500
    accounts = []

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.le = QLineEdit()
        self.setWindowTitle("Bank Account")
        self.resize(self.width, self.height)
        self.init_CreateAccountUI()
        self.init_ShowAccountUI()

    def store_BankAccounts(self, account):
        self.accounts.append(account)

    def init_CreateAccountUI(self):
        self.button_description_label("Click here to create a bank account: ", 35)
        self.button_config("Create", self.account_inputs, 35)

    def init_ShowAccountUI(self):
        self.button_description_label("Click here to view your bank account: ", 75)
        self.button_config("View", self.account_dashboard, 75)

    def account_inputs(self):
        name, name_ok = QInputDialog.getText(self, 'Account User Name: ', 'User Name: ', QLineEdit.Normal, "")
        pin, pin_ok = QInputDialog.getText(self, 'Account Pin Number: ', 'Pin Number: ', QLineEdit.Normal, "0000")
        amount, amount_ok = QInputDialog.getDouble(self, 'Account Start: ', 'Amount, $: ', 300.00, 0, 1000000, 2)
        if name_ok and pin_ok and amount_ok and len(name) > 5:
            new_account = BankAccount(name, pin, amount)
            self.store_BankAccounts({'name': name, 'pin': pin, 'amount': amount})
            print(new_account.user)
        else:
            if name_ok and pin_ok and amount_ok and len(name) == 0:
                self.info_dialog_box('Missing user name. Please, enter your name', 'Warning', 'critical')
            else:
                self.info_dialog_box('All inputs must be valid and confirmed!', 'Warning', 'critical')

    def info_dialog_box(self, text, title, category):
        msg = QMessageBox()
        if category == 'critical':
            msg.setIcon(QMessageBox.Critical)
        if category == 'information':
            msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()

    def button_description_label(self, text, position):
        label = QLabel(self)
        label.setText(text)
        label.setGeometry(200, position, 250, 40)
        label.show()

    def button_config(self, text, dialog, position):
        btn = QPushButton(self)
        btn.setText(text)
        btn.setGeometry(410, position, 100, 40)
        btn.show()
        btn.clicked.connect(dialog)

    def account_dashboard(self):
        pin, ok = QInputDialog.getText(self, 'Enter Pin Code: ', 'Pin Number: ', QLineEdit.Normal, "0000")
        if ok:
            acc = [elem for elem in self.accounts if elem['pin'] == pin]
            if len(acc) == 0:
                self.info_dialog_box('Cannot find account. Please, try again...', 'Warning', 'critical')
            else:
                name = str(acc[0]['name'])
                balance = str(acc[0]['amount'])
                text = '<span style="color: blue; font-size: 20px"><b>Your name: ' \
                       '</b></span><span style="color: red; font-size: 20px"><b>' \
                       + name + '</b></span><br>' \
                       + '<span style="color: blue; font-size: 20px"><b>Your current balance: ' \
                         '$</b><span style="color: red; font-size: 20px"><span><b>' \
                       + balance + '</b></span><br>'
                self.info_dialog_box(text, 'Account Profile', 'information')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

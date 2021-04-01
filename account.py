import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit, QMessageBox, QInputDialog

"""BankAccount Class"""


class BankAccount:
    def __init__(self, name, pin, amount):
        self.name = name
        self.pin = pin
        self.amount = amount


"""Main User Interface Window"""


class MainWindow(QMainWindow):  # inherit application's main window

    width = 850
    height = 500
    top_margin = 35
    accounts = []

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.le = QLineEdit()
        self.setWindowTitle("Bank Account")
        self.resize(self.width, self.height)
        self.init_CreateAccountUI()
        self.init_ShowAccountUI()
        self.init_DepositMoneyUI()
        self.init_WithdrawMoneyUI()

    def store_BankAccounts(self, account):
        self.accounts.append(account)

    """Main Window User Interface Functions:
        -Create Bank Account
        -Show Bank Account
        -Deposit Money to Bank Account
        -Withdraw Money from Bank Account
    """

    def init_CreateAccountUI(self):
        self.button_description_label("Click here to create a bank account: ", self.top_margin)
        self.button_config("Create", self.account_inputs, self.top_margin)

    def init_ShowAccountUI(self):
        self.button_description_label("Click here to view your bank account: ", self.top_margin + 40)
        self.button_config("View", self.account_dashboard, self.top_margin + 40)

    def init_DepositMoneyUI(self):
        self.button_description_label("Click here to deposit money to account: ", self.top_margin + 80)
        self.button_config("Deposit", self.deposit_cash, self.top_margin + 80)

    def init_WithdrawMoneyUI(self):
        self.button_description_label("Click here to withdraw money from account: ", self.top_margin + 120)
        self.button_config("Withdraw", self.withdraw_cash, self.top_margin + 120)

    """User Interface Items: Dialog Box, Button Label, Button Configs"""

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
        label.setGeometry(150, position, 250, 40)
        label.show()

    def button_config(self, text, dialog, position):
        btn = QPushButton(self)
        btn.setText(text)
        btn.setGeometry(410, position, 100, 40)
        btn.show()
        btn.clicked.connect(dialog)

    """ Main Window User Experience Functions: 
        -Create Bank Account
        -Show Bank Account
        -Deposit Money to Bank Account
        -Withdraw Money from Bank Account
    """

    def account_inputs(self):
        name, name_ok = QInputDialog.getText(self, 'Account User Name: ', 'User Name: ', QLineEdit.Normal, "")
        pin, pin_ok = QInputDialog.getText(self, 'Account Pin Number: ', 'Pin Number: ', QLineEdit.Normal, "0000")
        amount, amount_ok = QInputDialog.getDouble(self, 'Account Start: ', 'Amount, $: ', 10.00, 0, 1000000, 2)
        if name_ok and pin_ok and amount_ok and len(name) > 5:
            new_account = BankAccount(name, pin, amount)
            self.store_BankAccounts({'name': new_account.name, 'pin': new_account.pin, 'amount': new_account.amount})
        else:
            if name_ok and pin_ok and amount_ok and len(name) == 0:
                self.info_dialog_box('Missing user name. Please, enter your name', 'Warning', 'critical')
            else:
                self.info_dialog_box('All inputs must be valid and confirmed!', 'Warning', 'critical')

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
        else:
            self.info_dialog_box('Your request must be confirmed', 'Warning', 'critical')

    def deposit_cash(self):
        pin, pin_ok = QInputDialog.getText(self, 'Enter Pin Code: ', 'Pin Number: ', QLineEdit.Normal, "0000")
        deposit, deposit_ok = QInputDialog.getDouble(self, 'Deposit Cash: ', 'Deposit $: ', 000.00, 0, 1000000, 2)
        if pin_ok and deposit_ok:
            acc = [elem for elem in self.accounts if elem['pin'] == pin]
            if len(acc) > 0:
                acc[0]['amount'] += deposit
                self.info_dialog_box('Your current balance is $' + str('{:.2f}'.format(acc[0]['amount']))
                                     + ' now.', 'Warning', 'information')
            else:
                self.info_dialog_box('Account is not found. Please, try again...', 'Warning', 'critical')
        else:
            self.info_dialog_box('Your request must be confirmed', 'Warning', 'critical')

    def withdraw_cash(self):
        pin, pin_ok = QInputDialog.getText(self, 'Enter Pin Code: ', 'Pin Number: ', QLineEdit.Normal, "0000")
        deposit, deposit_ok = QInputDialog.getDouble(self, 'Withdraw Cash: ', 'Withdraw $: ', 000.00, 0, 1000000, 2)
        if pin_ok and deposit_ok:
            acc = [elem for elem in self.accounts if elem['pin'] == pin]
            if len(acc) > 0:
                if acc[0]['amount'] < deposit:
                    msg = 'Insufficient funds. You have only $' + str(acc[0]['amount']) + ' available. Please, try ' \
                                                                                          'again... '
                    self.info_dialog_box(msg, 'Warning', 'critical')
                else:
                    acc[0]['amount'] -= deposit
                    self.info_dialog_box('Your current balance is $' + str('{:.2f}'.format(acc[0]['amount']))
                                         + ' now.', 'Warning', 'information')
            else:
                self.info_dialog_box('Account is not found. Please, try again...', 'Warning', 'critical')
        else:
            self.info_dialog_box('Your request must be confirmed', 'Warning', 'critical')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

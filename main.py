from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys
import sqlite3


class Expresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.setWindowTitle('Программа Максима Алябьева')

    def run(self):
        self.statusbar.showMessage('')
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        data = cur.execute("""SELECT NameOfSort, StepenObjarki, ground, description, price, obem FROM Coffee
         WHERE id = ?""", (self.spinBox.value(),)).fetchone()
        if data is None:
            self.statusbar.showMessage('Предмета с таким id нет, попробуйте 1')
        else:
            self.coftype.setText(data[0])
            self.stepobj.setText(data[1])
            if data[2] == 1:
                self.ground.setText('Молотый')
            else:
                self.ground.setText('В зёрнах')
            self.flavdiscr.setText(data[3])
            self.price.setText(str(data[4]))
            self.obem.setText(str(data[5]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Expresso()
    form.show()
    sys.exit(app.exec())

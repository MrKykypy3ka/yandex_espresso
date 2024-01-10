from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QHBoxLayout,
                             QVBoxLayout, QPushButton, QHeaderView, QTableWidgetItem)
from PyQt5 import uic
import sys
import sqlite3 as sq


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.cur = None
        self.db = None
        uic.loadUi('MainForm.ui', self)
        self.initDB()
        self.initUI()

    def initUI(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.pushButton.clicked.connect(self.view)

    def view(self):
        try:
            result = self.cur.execute(f"SELECT * FROM Coffee").fetchall()
            result = [[elem[0]] + [elem[1]] + [elem[2]]
                      + [elem[3]] + [elem[4]] + [elem[5]] + [elem[6]] for elem in result]
            for i, row in enumerate(result):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        except sq.Error as e:
            print(e)

    def initDB(self):
        self.db = sq.connect('coffee.sqlite')
        self.cur = self.db.cursor()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки',
                                                    'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])


def main():
    app = QApplication([])
    win = MyClass()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

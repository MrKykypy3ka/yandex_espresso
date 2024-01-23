from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView, QTableWidgetItem
from PyQt5 import uic
import sys
import sqlite3 as sq


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.cur = None
        self.db = None
        uic.loadUi('MainForm.ui', self)
        self.initDB()
        self.initUI()
        self.view()

    def initUI(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки',
                                                    'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.addButton.clicked.connect(self.show_data_form)
        self.editButton.clicked.connect(self.show_data_form)

    def view(self):
        try:
            result = self.cur.execute(f"SELECT * FROM Coffee").fetchall()
            result = [[elem[0]] + [elem[1]] + [elem[2]]
                      + [elem[3]] + [elem[4]] + [elem[5]] + [elem[6]] for elem in result]
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(result):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        except sq.Error as e:
            print(e)

    def write(self, data):
        try:
            sqlite_insert_query = """INSERT INTO Coffee (id_coffee, name, roasting, shape, taste, price, volume)
                                     VALUES (?, ?, ?, ?, ?, ?, ?);"""
            self.cur.execute(sqlite_insert_query, data)
            self.db.commit()
            self.view()
        except sq.Error as e:
            print(e)

    def edit(self, data):
        try:
            sqlite_insert_query = """UPDATE Coffee 
                                     SET name = ?, roasting = ?, shape = ?, taste = ?,
                                     price = ?, volume = ? WHERE id_coffee = ?;"""
            self.cur.execute(sqlite_insert_query, (*data[1:], data[0]))
            self.db.commit()
            self.view()
        except sq.Error as e:
            print(e)

    def get_row(self):
        selected_items = self.tableWidget.selectedItems()
        if len(selected_items) > 0:
            selected_row = selected_items[0].row()
            row_data = [self.tableWidget.item(selected_row, col).text() for col in range(self.tableWidget.columnCount())]
            return row_data

    def show_data_form(self):
        data = [max(map(int, [self.tableWidget.item(row, 0).text()
                             for row in range(self.tableWidget.rowCount())
                             if self.tableWidget.item(row, 0) is not None ]))+1]
        if self.sender().text() == 'Изменить':
            data = self.get_row()
        if data is not None:
            self.data_win = DataWin(data)
            if len(data) == 1:
                self.data_win.new_data.connect(self.write)
            else:
                self.data_win.new_data.connect(self.edit)
            self.data_win.show()



    def initDB(self):
        self.db = sq.connect('coffee.sqlite')
        self.cur = self.db.cursor()


class DataWin(QWidget):
    new_data = pyqtSignal(list)
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.cur = None
        self.db = None
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.initUI()

    def initUI(self):
        if len(self.data) > 1:
            self.lineName.setText(self.data[1])
            self.lineRoastics.setText(self.data[2])
            self.comboShape.setCurrentText(self.data[3])
            self.lineTaste.setText(self.data[4])
            self.linePrice.setText(self.data[5])
            self.lineValue.setText(self.data[6])
        self.writeButton.clicked.connect(self.return_data)

    def return_data(self):
        self.data = self.data[:1]
        self.data.append(self.lineName.text())
        self.data.append(self.lineRoastics.text())
        self.data.append(self.comboShape.currentText())
        self.data.append(self.lineTaste.text())
        self.data.append(self.linePrice.text())
        self.data.append(self.lineValue.text())
        self.new_data.emit(self.data)
        self.close()


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    sys.exit(app.exec_())


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))


sys.excepthook = excepthook


if __name__ == "__main__":
    main()

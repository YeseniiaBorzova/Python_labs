from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QAbstractItemView, QMainWindow, QApplication, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt5 import QtWidgets, uic
import sys
from Seller_Qt import Seller_Window
from Product_Qt import Product_Window
from Sale_Qt import Sales_Window


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_form.ui", self)
        self.prodBtn.clicked.connect(self.switch_product)
        self.sellerBtn.clicked.connect(self.switch_seller)
        self.saleBtn.clicked.connect(self.switch_sales)

    def switch_product(self):
        self.window1 = Product_Window()
        self.window1.show()

    def switch_seller(self):
        self.window2 = Seller_Window()
        self.window2.show()

    def switch_sales(self):
        self.window3 = Sales_Window()
        self.window3.show()

app = QApplication(sys.argv)
w = Main_Window()
w.show()
app.exec_()

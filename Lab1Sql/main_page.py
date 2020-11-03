from tkinter import *
from Product_page import ProductPage
from Seller_page import SellerPage
from Sales_page import SalesPage

window = Tk()
window.title("Shop Application")
window.geometry("500x200")
lbl = Label(window, text="Choose what you want to work with:\n", font=("Times New Roman", 16))
lbl.pack(side="top")
btn_product = Button(window, text="Product", font=("Times New Roman", 12), width=10, command=ProductPage)
btn_seller = Button(window, text="Seller", font=("Times New Roman", 12), width=10, command=SellerPage)
btn_sales = Button(window, text="Sales", font=("Times New Roman", 12), width=10, command=SalesPage)
btn_product.pack(side="top")
btn_seller.pack(side="top")
btn_sales.pack(side="top")
window.mainloop()


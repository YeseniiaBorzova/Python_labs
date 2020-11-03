import sqlite3
from datetime import datetime


class Sales:

    def init_sale(self):
        if len(self.arr_prod) != len(self.arr_amount):
            return
        else:
            con = sqlite3.connect("shop.db")
            cur = con.cursor()
            cur.execute("""INSERT INTO Sales(seller_id, date)
                            VALUES(?,?)""", (self.seller_id, self.date))
            con.commit()
            cur.execute("""SELECT Sales.sale_id FROM SALES WHERE seller_id = ? AND date = ?""", (self.seller_id, self.date))
            sale_id = cur.fetchall()
            for i in range(len(self.arr_prod)):
                cur.execute("""INSERT INTO Sold_product(product_id, amount, sale_id) 
                   VALUES((SELECT product_id from Product WHERE Product.name = ?),?,?)""",
                            (self.arr_prod[i], self.arr_amount[i], int(sale_id[-1][0])))
            con.commit()
            con.close()

    def __init__(self, seller_id, arr_prod, arr_amount):
        sell_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.seller_id = seller_id
        self.date = sell_time
        self.arr_prod = arr_prod
        self.arr_amount = arr_amount
        #self.init_sale(arr_prod, arr_amount)

    @staticmethod
    def find_sale_by_date(date):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT sale_id, seller_id, date FROM Sales
                            WHERE date LIKE ?""", (date+'%',))
        arr = cur.fetchall()
        res = ""
        for sale in arr:
            res += "-Id " + str(sale[0]) + ", Seller_id " + str(sale[1]) + ", date: " + str(sale[2])
        con.commit()
        con.close()
        return res

    @staticmethod
    def delete_sale_by_id(id):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM Sales WHERE sale_id = ?""", (id,))
        con.commit()
        cur.execute("""DELETE FROM Sold_product WHERE sale_id = ?""", (id,))
        con.close()

    @staticmethod
    def find_sale_by_id(id):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT sale_id, seller_id, date FROM Sales
                        WHERE sale_id = ?""", (id,))
        arr = cur.fetchall()
        res = ""
        for sale in arr:
            res += "-Id "+str(sale[0])+", Seller_id "+str(sale[1])+", date: "+str(sale[2])
        con.commit()
        con.close()
        return res

    @staticmethod
    def show_all_sales():
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Sales")
        res = ""
        arr_sales = cur.fetchall()
        for sale in arr_sales:
            res += "Id: "+str(sale[0])+", seller id: "+str(sale[1])+", datetime: "+sale[2]+"\n"
        return res

    def to_string(self):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT sale_id, seller_id, date FROM Sales
                        WHERE seller_id = ?""", (self.seller_id,))
        arr = cur.fetchall()
        res = ""
        for sale in arr:
            res += "-Id " + str(sale[0]) + ", Seller_id " + str(sale[1]) + ", date: " + str(sale[2])+"\n"
        con.commit()
        con.close()
        return res


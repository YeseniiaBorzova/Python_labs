import sqlite3


class Seller:

    def insert_seller(self):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""INSERT INTO Seller(name, surname, middle_name, income_percent)
           VALUES(?,?,?,?)""", (self.name, self.surname, self.middle_name, self.income_percent))
        con.commit()
        con.close()

    def __init__(self, name, surname, middle_name, income_percent):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.income_percent = income_percent
        #self.insert_seller()

    def delete_seller_by_name(self):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM Seller WHERE name = ? AND surname = ?""", (self.name, self.surname))
        con.commit()
        con.close()

    @staticmethod
    def find_seller_id_by_surname(surname):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT seller_id FROM Seller WHERE surname = ?""",
                    (surname,))
        seller_id = cur.fetchall()
        con.commit()
        con.close()
        return seller_id[0][0]

    def find_seller_id(self):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT seller_id FROM Seller WHERE name = ? AND surname = ? AND middle_name = ?""",
                    (self.name, self.surname, self.middle_name))
        seller_id = cur.fetchall()
        con.commit()
        con.close()
        return seller_id[0][0]

    @staticmethod
    def update_percent(surname, percent):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""UPDATE Seller SET income_percent = ? WHERE surname = ?""", (percent, surname))
        con.commit()
        con.close()

    @staticmethod
    def show_all_sellers():
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT * FROM Seller""")
        arr_seller = cur.fetchall()
        res = ""
        for seller in arr_seller:
            res += "Id: "+str(seller[0])+", Name: "+str(seller[1])+" "+str(seller[2])+" "+str(seller[3])+\
                   ", comission percent: "+str(seller[4])+"% \n"
        return res

    @staticmethod
    def find_seller_by_surname(surname):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT seller_id, name, surname, middle_name, income_percent FROM Seller
                WHERE surname = ?""", (surname,))
        arr = cur.fetchall()
        con.commit()
        con.close()
        return "ID: "+str(arr[0][0])+", Full name: "+arr[0][1]+' '+arr[0][2]+' '+arr[0][3]+\
               ", comission percent - "+str(arr[0][4])+"%"

    def seller_income(self):
        income = 0
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT Sales.sale_id FROM Sales WHERE seller_id = ?""", (self.find_seller_id(),))
        sales_arr = cur.fetchall()
        for i in sales_arr:
            cur.execute("""SELECT Sold_product.amount, Product.sell_price, Seller.income_percent, Sales.sale_id
            FROM Sold_product, Product, Seller, Sales WHERE Sold_product.sale_id = ? AND Sales.sale_id = ? AND Seller.seller_id = ?
            AND Sales.seller_id = ? AND Product.product_id = Sold_product.product_id""", (i[0], i[0], self.find_seller_id(), self.find_seller_id()))
            arr = cur.fetchall()
            for prod in arr:
                income += prod[0]*prod[1]*prod[2]
        con.close()
        return str(income)+"$"

    @staticmethod
    def seller_income_by_surname(sel_surname):
        income = 0
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT Sales.sale_id FROM Sales WHERE seller_id = (SELECT seller_id FROM Seller WHERE surname = ?)""", (sel_surname,))
        sales_arr = cur.fetchall()
        for i in sales_arr:
            cur.execute("""SELECT Sold_product.amount, Product.sell_price, Seller.income_percent, Sales.sale_id
            FROM Sold_product, Product, Seller, Sales WHERE Sold_product.sale_id = ? AND Sales.sale_id = ? AND Seller.surname = ?
            AND Sales.seller_id = Seller.seller_id AND Product.product_id = Sold_product.product_id""", (i[0], i[0], sel_surname))
            arr = cur.fetchall()
            for prod in arr:
                income += prod[0]*prod[1]*prod[2]
        con.close()
        return str(income)+"$"

    def to_string(self):
        return self.name+" "+self.middle_name+" "+self.surname+" comission percent - "+str(self.income_percent)+"%"


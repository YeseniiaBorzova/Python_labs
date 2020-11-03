import sqlite3


class Product:
    def __init__(self, name, measurment_unit, purchase_price, sell_price):
        self.name = name
        self.measurment_unit = measurment_unit
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        #self.insert_product()

    def insert_product(self):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT product_id FROM Product WHERE name = ?""", (self.name,))
        res = cur.fetchall()
        if len(res) != 0:
            return "Such product already exists!"
        else:
            cur.execute("""INSERT INTO Product(name, measurment_unit, purchase_price, sell_price)
            VALUES(?,?,?,?)""",  (self.name, self.measurment_unit, self.purchase_price, self.sell_price))
            con.commit()
            con.close()

    @staticmethod
    def show_all_the_products():
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Product")
        arr_prod = cur.fetchall()
        res = ""
        for prod in arr_prod:
            res += "Id: " + str(prod[0]) + ", name: " + prod[1] + "; measurment unit: "+prod[2] + ", purchase price: " + str(prod[3])\
                   + "$, sell price:" + str(prod[4])+"$"+"\n"
        return res

    def delete_product_by_name(self):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM Product WHERE name = ?""", (self.name,))
        con.commit()
        con.close()

    @staticmethod
    def find_product_id(name):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT product_id FROM Product WHERE name = ?""", (name,))
        prod_id = cur.fetchall()
        con.commit()
        con.close()
        return prod_id[0][0]

    @staticmethod
    def delete_product_by_name(name):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM Product WHERE name = ?""", (name,))
        con.commit()
        con.close()

    @staticmethod
    def update_sell_price(name, price):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""UPDATE Product SET sell_price = ? WHERE name = ?""", (price, name))
        con.commit()
        con.close()

    @staticmethod
    def update_purchase_price(name, price):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""UPDATE Product SET purchase_price = ? WHERE name = ?""", (price, name))
        con.commit()
        con.close()

    # def update_name(self, name):
    #     con = sqlite3.connect("shop.db")
    #     cur = con.cursor()
    #     cur.execute("""UPDATE Product SET name = ? WHERE name = ? """, (name, self.name))
    #     con.commit()
    #     con.close()

    @staticmethod
    def update_product_name(old_name, new_name):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""UPDATE Product SET name = ? WHERE name = ? """, (new_name, old_name))
        con.commit()
        con.close()

    @staticmethod
    def find_product_by_name(name):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT product_id, name, measurment_unit, purchase_price, sell_price FROM Product
        WHERE name = ?""", (name,))
        arr = cur.fetchall()
        return "ID:"+str(arr[0][0])+", name: "+arr[0][1]+", purchase_price: " + str(arr[0][3])+"$" + " per "+arr[0][2]+","\
               + " (sell_price: "+str(arr[0][4])+"$)"
        con.commit()
        con.close()

    @staticmethod
    def income_by_product(product_name):
        con = sqlite3.connect("shop.db")
        cur = con.cursor()
        cur.execute("""SELECT (SUM(Sold_product.amount)*(Product.sell_price-Product.purchase_price))
        AS income FROM Sold_product, Product 
        WHERE Sold_product.product_id = Product.product_id AND Product.name = ? """, (product_name,))
        income = cur.fetchall()
        con.commit()
        con.close()
        return "Income from - "+product_name+' = '+str(income[0][0])

    def to_string(self):
        return "Name: "+self.name+", Sell price: "+str(self.sell_price)+" per one "+self.measurment_unit



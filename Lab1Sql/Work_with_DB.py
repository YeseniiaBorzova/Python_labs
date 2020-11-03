import sqlite3
from Product import Product
from Sales import Sales
from Seller import Seller


def first_menu():
    while True:
        print("Select what you want to do: \n"
            "1. Work with Products \n"
            "2. Work with Sales \n"
            "3. Work with Sellers \n"
            "4. Show all products \n"
            "5. Show all sales \n"
            "6. Show all sellers \n"
            "-1 to quite \n")
        n = int(input("Enter your number:"))
        try:
            if n == -1:
                return
            elif n == 1:
                work_with_product()
            elif n == 2:
                work_with_sales()
            elif n == 3:
                work_with_seller()
            elif n == 4:
                print(Product.show_all_the_products())
            elif n == 5:
                print(Sales.show_all_sales())
            elif n == 6:
                print(Seller.show_all_sellers())
        except:
            print("Wrong input!")


def work_with_product():
    while True:
        print("Select what you want to do: \n"
              "1. Insert product \n"
              "2. Find income by some product \n"
              "3. Rename some product \n"
              "4. Update sell price \n"
              "5. Update purchase price \n"
              "6. Find product id \n"
              "7. Delete product by id \n"
              "8. Find product by name \n"
              "-1 to quite \n")
        n = int(input("Enter your number:"))
        try:
            if n == -1:
                return
            elif n == 1:
                name = input("Enter product`s name: ")
                measurment_unit = input("Enter product`s measurment unit: ")
                sell_price = float(input("Enter sell price: "))
                purchase_price = float(input("Enter purchase price: "))
                new_product = Product(name,measurment_unit,purchase_price,sell_price)
                new_product.insert_product()
                print(new_product.to_string(),"was inserted.")
            elif n == 2:
                name = input("Enter product name: ")
                print(Product.income_by_product(name))
            elif n == 3:
                old_name = input("Enter product old name: ")
                new_name = input("Enter product new name: ")
                Product.update_product_name(old_name,new_name)
            elif n == 4:
                price = float(input("Enter new sell price: "))
                name = input("Enter product`s name: ")
                Product.update_sell_price(name,price)
            elif n == 5:
                price = float(input("Enter new purchase price: "))
                name = input("Enter product`s name: ")
                Product.update_purchase_price(name, price)
            elif n == 6:
                name = input("Enter product name: ")
                print(Product.find_product_id(name)," - id")
            elif n == 7:
                prod_id = int(input("Enter product`s id: "))
                Product.delete_product_by_id(prod_id)
            elif n == 8:
                name = input("Enter product`s name: ")
                print(Product.find_product_by_name(name))
        except:
            print("Wrong input!")


def work_with_sales():
    while True:
        print("Select what you want to do: \n"
              "1. Insert sale \n"
              "2. Find sale by id \n"
              "-1 to quite \n")
        n = int(input("Enter your number:"))
        try:
            if n == -1:
                return
            elif n == 1:
                seller_id = int(input("Enter seller`s id: "))
                arr_prod = input("Enter list of products splited by coma:").split(",")
                arr_amount = list(map(float, input("Enter list of amounts splited by coma: ").split(",")))
                new_sale = Sales(seller_id, arr_prod, arr_amount)
                new_sale.init_sale()
            elif n == 2:
                id = int(input("Enter sale`s id: "))
                print(Sales.find_sale_by_id(id))
        except:
            print("Wrong input!")


def work_with_seller():
    while True:
        print("Select what you want to do: \n"
              "1. Insert seller \n"
              "2. Find seller by surname \n"
              "3. Find seller id \n"
              "4. Update comission percent \n"
              "5. Find seller income \n"
              "-1 to quite \n")
        n = int(input("Enter your number:"))
        try:
            if n == -1:
                return
            elif n == 1:
                name = input("Enter seller`s name: ")
                surname = input("Enter seller`s surname: ")
                middle_name = input("Enter seller`s middle name ")
                income_percent = float(input("Enter comission percent: "))
                new_seller = Seller(name,surname,middle_name,income_percent)
                new_seller.insert_seller()
                print(new_seller.to_string(),"was inserted.")
            elif n == 2:
                surname = input("Enter seller`s surname: ")
                print(Seller.find_seller_by_surname(surname))
            elif n == 3:
                surname = input("Enter seller`s surname: ")
                print(Seller.find_seller_id_by_surname(surname))
            elif n == 4:
                percent = float(input("Enter new comission percent: "))
                surname = input("Enter seller`s surname: ")
                Seller.update_percent(surname, percent)
            elif n == 5:
                surname = input("Enter seller`s surname: ")
                print(Seller.seller_income_by_surname(surname))
        except:
            print("wrong output!")



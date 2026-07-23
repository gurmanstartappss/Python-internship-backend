import csv
from logger_config import logger

PRODUCT_FILE = "products.csv"
CART_FILE = "cart.csv"
ORDER_FILE = "orders.csv"


def initialize_files():
    try:
        with open(CART_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Username", "ProductID", "Product", "Price", "Quantity"]
            )
    except FileExistsError:
        pass

    try:
        with open(ORDER_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Username", "Product", "Price", "Quantity", "Total"]
            )
    except FileExistsError:
        pass


initialize_files()
def view_products():

    with open(PRODUCT_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        print("\nID\tProduct\tPrice\tQty")

        for row in reader:

            print(f'{row["ID"]}\t{row["Product"]}\t₹{row["Price"]}\t{row["Quantity"]}')

def search_product():

    name = input("Enter Product Name : ").lower()

    with open(PRODUCT_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        found = False

        for row in reader:

            if name in row["Product"].lower():

                found = True

                print(f'{row["ID"]}\t{row["Product"]}\t₹{row["Price"]}')

        if not found:

            print("Product Not Found")


def add_to_cart(username):

    pid = input("Enter Product ID : ")

    qty = int(input("Enter Quantity : "))

    with open(PRODUCT_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["ID"] == pid:

                if qty > int(row["Quantity"]):

                    print("Not Enough Stock")
                    return

                with open(CART_FILE, "a", newline="") as cart:

                    writer = csv.writer(cart)

                    writer.writerow([
                        username,
                        pid,
                        row["Product"],
                        row["Price"],
                        qty
                    ])

                print("Product Added Successfully")
                return

    print("Product Not Found")


def view_cart(username):

    total = 0

    with open(CART_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        found = False

        print("\nProduct\tPrice\tQty")

        for row in reader:

            if row["Username"] == username:

                found = True

                subtotal = float(row["Price"]) * int(row["Quantity"])

                total += subtotal

                print(
                    f'{row["Product"]}\t₹{row["Price"]}\t{row["Quantity"]}'
                )

        if found:

            print("----------------------")
            print("Total =", total)

        else:

            print("Cart Empty")

def remove_cart(username):

    pid = input("Enter Product ID : ")

    rows = []

    removed = False

    with open(CART_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Username"] == username and row["ProductID"] == pid:

                removed = True
                continue

            rows.append(row)

    with open(CART_FILE, "w", newline="") as file:

        fieldnames = [
            "Username",
            "ProductID",
            "Product",
            "Price",
            "Quantity"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(rows)

    if removed:

        print("Removed Successfully")

    else:

        print("Product Not In Cart")


def place_order(username):

    cart_items = []

    with open(CART_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Username"] == username:

                cart_items.append(row)

    if not cart_items:

        print("Cart Empty")
        return

    products = []

    with open(PRODUCT_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        products = list(reader)

    for item in cart_items:

        total = float(item["Price"]) * int(item["Quantity"])

        with open(ORDER_FILE, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                username,
                item["Product"],
                item["Price"],
                item["Quantity"],
                total
            ])

        for product in products:

            if product["ID"] == item["ProductID"]:

                product["Quantity"] = str(
                    int(product["Quantity"]) -
                    int(item["Quantity"])
                )

    with open(PRODUCT_FILE, "w", newline="") as file:

        fieldnames = [
            "ID",
            "Seller",
            "Product",
            "Price",
            "Quantity"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(products)

    rows = []

    with open(CART_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Username"] != username:

                rows.append(row)

    with open(CART_FILE, "w", newline="") as file:

        fieldnames = [
            "Username",
            "ProductID",
            "Product",
            "Price",
            "Quantity"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(rows)

    print("Order Placed Successfully")
    logger.info(f"{username} placed an order")



def view_orders(username):

    with open(ORDER_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        found = False

        print("\nProduct\tQty\tTotal")

        for row in reader:

            if row["Username"] == username:

                found = True

                print(
                    f'{row["Product"]}\t{row["Quantity"]}\t₹{row["Total"]}'
                )

        if not found:

            print("No Orders Found")
            
def browse_products(username):

    while True:

        print("\n1. View Products")
        print("2. Search Product")
        print("3. Add To Cart")
        print("4. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            view_products()

        elif choice == "2":

            search_product()

        elif choice == "3":

            add_to_cart(username)

        elif choice == "4":

            break

        else:

            print("Invalid Choice")

def cart_menu(username):

    while True:

        print("\n1. View Cart")
        print("2. Remove Product")
        print("3. Place Order")
        print("4. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            view_cart(username)

        elif choice == "2":

            remove_cart(username)

        elif choice == "3":

            place_order(username)

        elif choice == "4":

            break

        else:

            print("Invalid Choice")
            
            
def Cus(username):

    while True:

        print("\n========== CUSTOMER ==========")
        print("1. Products")
        print("2. Cart")
        print("3. Orders")
        print("4. Logout")

        choice = input("Enter Choice : ")

        if choice == "1":

            browse_products(username)

        elif choice == "2":

            cart_menu(username)

        elif choice == "3":

            view_orders(username)

        elif choice == "4":

            print("Logged Out")
            break

        else:

            print("Invalid Choice")
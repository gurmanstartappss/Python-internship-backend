import csv
from logger_config import logger

PRODUCT_FILE = "products.csv"


def initialize_file():
    try:
        with open(PRODUCT_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Seller", "Product", "Price", "Quantity"])
    except FileExistsError:
        pass


initialize_file()


def add_product(username):
    product = input("Enter Product Name : ")
    price = float(input("Enter Price : "))
    quantity = int(input("Enter Quantity : "))

    product_id = 1

    with open(PRODUCT_FILE, "r", newline="") as file:
        reader = list(csv.DictReader(file))
        if reader:
            product_id = int(reader[-1]["ID"]) + 1

    with open(PRODUCT_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product_id, username, product, price, quantity])

    print("Product Added Successfully")
    logger.info(f"{username} added product {product}")


def view_products():
    with open(PRODUCT_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n-------------------------------")
        print("ID\tProduct\tPrice\tQty\tSeller")
        print("-------------------------------")

        found = False
        for row in reader:
            found = True
            print(
                f'{row["ID"]}\t{row["Product"]}\t₹{row["Price"]}\t{row["Quantity"]}\t{row["Seller"]}'
            )

        if not found:
            print("No Products Available")


def update_product(username):
    pid = input("Enter Product ID : ")

    rows = []
    updated = False

    with open(PRODUCT_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row["ID"] == pid and row["Seller"] == username:

                row["Product"] = input("New Product Name : ")
                row["Price"] = input("New Price : ")
                row["Quantity"] = input("New Quantity : ")

                updated = True

            rows.append(row)

    if updated:

        with open(PRODUCT_FILE, "w", newline="") as file:

            fieldnames = ["ID", "Seller", "Product", "Price", "Quantity"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(rows)

        print("Product Updated Successfully")
        logger.info(f"{username} updated product {pid}")

    else:
        print("Product Not Found")


def delete_product(username):
    pid = input("Enter Product ID : ")

    rows = []
    deleted = False

    with open(PRODUCT_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row["ID"] == pid and row["Seller"] == username:
                deleted = True
                continue

            rows.append(row)

    if deleted:

        with open(PRODUCT_FILE, "w", newline="") as file:

            fieldnames = ["ID", "Seller", "Product", "Price", "Quantity"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(rows)

        print("Product Deleted Successfully")
        logger.info(f"{username} deleted product {pid}")

    else:
        print("Product Not Found")


def Sel(username):
    while True:

        print("\n========= SELLER MENU =========")

        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Logout")

        choice = input("Enter Choice : ")

        if choice == "1":
            add_product(username)

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_product(username)

        elif choice == "4":
            delete_product(username)

        elif choice == "5":
            print("Logged Out Successfully")
            break

        else:
            print("Invalid Choice")
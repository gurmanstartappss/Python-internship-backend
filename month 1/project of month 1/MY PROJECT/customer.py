import csv

def Cus():
    while True:
        print("\n----- CUSTOMER MENU -----")
        print("1. View Products")
        print("2. Search Product")
        print("3. Add to Cart")
        print("4. Remove from Cart")
        print("5. View Cart")
        print("6. Place Order")
        print("7. View Orders")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            def view_products(): 
                pass

        elif choice== "2":
            def search_product():
                pass

        elif choice == "3":
            def add_to_cart():
                pass

        elif choice == "4":
            def remove_from_cart():
                pass

        elif choice == "5":
            def view_cart():
                pass

        elif choice == "6":
            def place_order():
                pass

        elif choice == "7":
            def view_orders():
                pass

        elif choice == "8":
            print("Logged Out Successfully")
            break

        else:
            print("Invalid Choice")
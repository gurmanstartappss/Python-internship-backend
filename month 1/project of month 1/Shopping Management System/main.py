from auth import AuthenticationService

auth = AuthenticationService()


def admin_dashboard(admin):

    while True:
        admin.show_menu()
        choice = input("\nEnter Choice : ")

        if choice == "1":
            auth.register_seller()
        elif choice == "2":
            admin.remove_seller()
        elif choice == "3":
            admin.view_all_sellers()
        elif choice == "4":
            admin.view_all_customers()
        elif choice == "5":
            admin.view_all_products()
        elif choice == "6":
            admin.view_all_orders()
        elif choice == "7":
            admin.generate_sales_report()
        elif choice == "8":
            admin.search_product()
        elif choice == "9":
            admin.display_statistics()
        elif choice == "0":
            auth.logout()
            break
        else:
            print("Invalid Choice")


def seller_dashboard(seller):

    while True:

        seller.show_menu()

        choice = input("\nEnter Choice : ")

        if choice == "1":
            seller.add_product()
        elif choice == "2":
            seller.update_product()
        elif choice == "3":
            seller.delete_product()
        elif choice == "4":
            seller.view_products()
        elif choice == "5":
            seller.view_orders()
        elif choice == "0":
            auth.logout()
            break
        else:
            print("Invalid Choice")



def customer_dashboard(customer):

    while True:

        customer.show_menu()

        choice = input("\nEnter Choice : ")
        if choice == "1":
            customer.browse_products()
        elif choice == "2":
            customer.add_to_cart()
        elif choice == "3":
            customer.place_order()
        elif choice == "0":
            auth.logout()
            break
        else:
            print("Invalid Choice")


while True:

    print("\n===================================")
    print(" ONLINE SHOPPING MANAGEMENT SYSTEM ")
    print("===================================")

    print("1. Admin Portal")
    print("2. Seller Portal")
    print("3. Customer Portal")
    print("0. Exit")

    choice = input("\nEnter Choice : ")


    if choice == "1":
        admin = auth.login("admin")
        if admin:
            admin_dashboard(admin)

    elif choice == "2":

        while True:
            print("\n------ SELLER PORTAL ------")
            print("1. Register")
            print("2. Login")
            print("0. Back")

            seller_choice = input("Enter Choice : ")
            if seller_choice == "1":
                auth.register_seller()
            elif seller_choice == "2":
                seller = auth.login("seller")
                if seller:
                    seller_dashboard(seller)
            elif seller_choice == "0":
                break
            else:
                print("Invalid Choice")



    elif choice == "3":

        while True:

            print("\n------ CUSTOMER PORTAL ------")
            print("1. Register")
            print("2. Login")
            print("0. Back")
            customer_choice = input("Enter Choice : ")
            
            if customer_choice == "1":
                auth.register_customer()
            elif customer_choice == "2":
                customer = auth.login("customer")
                if customer:
                    customer_dashboard(customer)
            elif customer_choice == "0":
                break
            else:
                print("Invalid Choice")
                
    elif choice == "0":
        print("\nThank You For Using Shopping Management System.")
        break
    else:
        print("Invalid Choice")
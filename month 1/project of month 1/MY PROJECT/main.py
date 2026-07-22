import auth
import seller
import customer
from logger_config import logger


def get_choice(msg):

    while True:

        try:

            return int(input(msg))

        except ValueError:

            print("Enter Numbers Only")


while True:

    print("\n========== ONLINE SHOPPING SYSTEM ==========")

    print("1. Seller")

    print("2. Customer")

    print("3. Exit")

    choice = get_choice("Enter Choice : ")

    if choice == 1:

        while True:

            print("\n1.Register")

            print("2.Login")

            print("3.Back")

            ch = get_choice("Enter Choice : ")

            if ch == 1:

                auth.registration("SELLER")

            elif ch == 2:

                username = auth.login("SELLER")

                if username:

                    seller.Sel(username)

            elif ch == 3:

                break

            else:

                print("Invalid Choice")

    elif choice == 2:

        while True:

            print("\n1.Register")

            print("2.Login")

            print("3.Back")

            ch = get_choice("Enter Choice : ")

            if ch == 1:

                auth.registration("CUSTOMER")

            elif ch == 2:

                username = auth.login("CUSTOMER")

                if username:

                    customer.Cus(username)

            elif ch == 3:

                break

            else:

                print("Invalid Choice")

    elif choice == 3:

        logger.info("Application Closed")

        print("Thank You")

        break

    else:

        print("Invalid Choice")
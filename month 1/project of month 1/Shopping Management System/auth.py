
import hashlib
from admin import Admin
from seller import Seller
from customer import Customer
from csv_manager import CSVManager
from logger_config import logger
from exceptions import (DuplicateEmailError,DuplicateUsernameError,AuthenticationError)


class AuthenticationService:

    def __init__(self):
        self.csv_manager = CSVManager()
        self.users_file = self.csv_manager.users_file
        self.create_default_admin()
    # ----------------------------------------
    # Helper Input
    # ----------------------------------------

    def get_input(self, message):
        while True:
            value = input(message).strip()
            if value == "0":
                return None
            if value == "":
                print("Input cannot be empty.")
                continue
            return value

    # ----------------------------------------
    # Password Hashing
    # ----------------------------------------

    def hash_password(self, password):
        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    # ----------------------------------------
    # Generate User ID
    # ----------------------------------------

    def generate_user_id(self):
        users = self.csv_manager.read_all(
            self.users_file
        )
        if not users:
            return 1001
        return int(
            users[-1]["user_id"]
        ) + 1

    # ----------------------------------------
    # Duplicate Username
    # ----------------------------------------

    def username_exists(self, username):
        users = self.csv_manager.read_all(
            self.users_file
        )

        for user in users:
            if user["username"] == username:
                raise DuplicateUsernameError(
                    "Username already exists."
                )
        return False

    # ----------------------------------------
    # Duplicate Email
    # ----------------------------------------

    def email_exists(self, email):
        users = self.csv_manager.read_all(
            self.users_file
        )
        for user in users:
            if user["email"] == email:
                raise DuplicateEmailError(
                    "Email already exists."
                )
        return False

    # ----------------------------------------
    # Create Default Admin
    # ----------------------------------------

    def create_default_admin(self):
        users = self.csv_manager.read_all(
            self.users_file
        )
        for user in users:
            if user["role"] == "admin":
                return
        password_hash = self.hash_password(
            "admin123")
        admin = Admin(1000,"admin","System Admin","admin@gmail.com",password_hash,"admin")

        self.csv_manager.append_row(
            self.users_file,
            [admin.user_id,admin.username,admin.name,admin.email,password_hash,admin.role])
        logger.info("Default Admin Created.")
        
    """part 2:---registration"""
        # ----------------------------------------
    # Register Customer
    # ----------------------------------------

    def register_customer(self):

        while True:
            try:
                print("\n========== CUSTOMER REGISTRATION ==========")
                print("(Enter 0 at any time to go back)\n")

                username = self.get_input("Username : ")

                if username is None:
                    return

                name = self.get_input("Name : ")

                if name is None:
                    return

                email = self.get_input("Email : ")

                if email is None:
                    return

                password = self.get_input("Password : ")

                if password is None:
                    return

                self.username_exists(username)
                self.email_exists(email)
                if len(password) < 6:
                    raise ValueError(
                        "Password must contain at least 6 characters.")

                password_hash = self.hash_password(password)
                user_id = self.generate_user_id()
                customer = Customer(user_id,username,name,email,password_hash,"customer")

                self.csv_manager.append_row(self.users_file,[customer.user_id,customer.username,customer.name,customer.email,password_hash,customer.role])

                logger.info(f"Customer Registered : {username}")
                print("\nRegistration Successful.")
                return

            except DuplicateUsernameError as e:
                logger.warning(e)
                print(e)
                
            except DuplicateEmailError as e:
                logger.warning(e)
                print(e)

            except ValueError as e:
                logger.warning(e)
                print(e)

            except Exception as e:
                logger.exception(e)
                print("Registration Failed.")

            choice = input("\n1. Try Again\n0. Back\nChoice : ")
            if choice == "0":
                return

    # ----------------------------------------
    # Register Seller
    # ----------------------------------------

    def register_seller(self):

        while True:

            try:

                print("\n========== SELLER REGISTRATION ==========")
                print("(Enter 0 at any time to go back)\n")

                username = self.get_input("Username : ")

                if username is None:
                    return

                name = self.get_input("Name : ")

                if name is None:
                    return

                email = self.get_input("Email : ")

                if email is None:
                    return

                password = self.get_input("Password : ")

                if password is None:
                    return

                self.username_exists(username)

                self.email_exists(email)

                if len(password) < 6:

                    raise ValueError(
                        "Password must contain at least 6 characters."
                    )

                password_hash = self.hash_password(password)
                user_id = self.generate_user_id()
                seller = Seller(user_id,username,name,email,password_hash,"seller")

                self.csv_manager.append_row(
                    self.users_file,
                    [
                        seller.user_id,
                        seller.username,
                        seller.name,
                        seller.email,
                        password_hash,
                        seller.role])

                logger.info(f"Seller Registered : {username}")

                print("\nSeller Registered Successfully.")
                return

            except DuplicateUsernameError as e:
                logger.warning(e)
                print(e)

            except DuplicateEmailError as e:
                logger.warning(e)
                print(e)

            except ValueError as e:
                logger.warning(e)
                print(e)

            except Exception as e:
                logger.exception(e)
                print("Registration Failed.")

            choice = input("\n1. Try Again\n0. Back\nChoice : ")

            if choice == "0":
                return
            
    """part 3:-login and logouts"""
        # ----------------------------------------
    # Login
    # ----------------------------------------

    def login(self, expected_role):
        while True:
            try:

                print("\n========== LOGIN ==========")
                print("(Enter 0 at any time to go back)\n")

                username = self.get_input("Username : ")

                if username is None:
                    return None

                password = self.get_input("Password : ")

                if password is None:
                    return None

                password_hash = self.hash_password(password)

                users = self.csv_manager.read_all(self.users_file)

                for user in users:
                    if (user["username"] == username and user["password_hash"] == password_hash):

                        if user["role"] != expected_role:
                            raise AuthenticationError(f"This account is not a {expected_role} account.")

                        logger.info(f"{username} logged in successfully.")

                        print(f"\nWelcome {user['name']}\n")

                        if expected_role == "admin":

                            return Admin(int(user["user_id"]),user["username"],user["name"],user["email"],user["password_hash"],user["role"])

                        elif expected_role == "seller":

                            return Seller(int(user["user_id"]),user["username"],user["name"],user["email"],user["password_hash"],user["role"])

                        elif expected_role == "customer":

                            return Customer(int(user["user_id"]),user["username"],user["name"],user["email"],user["password_hash"],user["role"])

                raise AuthenticationError(
                    "Invalid Username or Password."
                )

            except AuthenticationError as e:
                logger.warning(e)
                print(e)

            except Exception as e:
                logger.exception(e)
                print("Login Failed.")
            choice = input(
                "\n1. Try Again\n0. Back\nChoice : " )

            if choice == "0":
                return None
    # ----------------------------------------
    # Logout
    # ----------------------------------------

    def logout(self):
        logger.info("User Logged Out.")
        print("\nLogged Out Successfully.\n")

from user import User
from logger_config import logger


class Seller(User):

    def __init__(self,user_id,username,name,email,password_hash,role="seller"):

        super().__init__(user_id,username,name,email,password_hash,role)

    def show_menu(self):

        print("\n========== SELLER MENU ==========")

        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Products")
        print("5. View Orders")
        print("6. Logout")

    def add_product(self):
        logger.info(f"{self.username} selected Add Product.")
        print("Add Product Function")

    def update_product(self):
        logger.info(f"{self.username} selected Update Product.")
        print("Update Product Function")

    def delete_product(self):
        logger.info(f"{self.username} selected Delete Product.")
        print("Delete Product Function")

    def view_products(self):
        logger.info(f"{self.username} viewed products.")
        print("View Products Function")

    def view_orders(self):
        logger.info(f"{self.username} viewed received orders.")
        print("View Orders Function")


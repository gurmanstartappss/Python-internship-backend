"""
admin.py

Admin Class
"""

from user import User
from logger_config import logger


class Admin(User):

    def __init__(
        self,
        user_id,
        username,
        name,
        email,
        password_hash,
        role="admin"
    ):

        super().__init__(
            user_id,
            username,
            name,
            email,
            password_hash,
            role
        )

    def show_menu(self):

        print("\n========== ADMIN MENU ==========")
        print("1. Add Seller")
        print("2. Remove Seller")
        print("3. View All Sellers")
        print("4. View All Customers")
        print("5. View All Products")
        print("6. Search Product")
        print("0. Logout")

    def add_seller(self):
        logger.info(f"{self.username} selected Add Seller.")

    def remove_seller(self):
        logger.info(f"{self.username} selected Remove Seller.")

    def view_all_sellers(self):
        logger.info(f"{self.username} viewed sellers.")

    def view_all_customers(self):
        logger.info(f"{self.username} viewed customers.")

    def view_all_products(self):
        logger.info(f"{self.username} viewed products.")

    def search_product(self):
        logger.info(f"{self.username} searched products.")

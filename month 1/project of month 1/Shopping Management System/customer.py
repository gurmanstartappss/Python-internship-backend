from user import User
from logger_config import logger


class Customer(User):

    def __init__(
        self,
        user_id,
        username,
        name,
        email,
        password_hash,
        role="customer"
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

        print("\n========== CUSTOMER MENU ==========")
        print("1. Browse Products")
        print("2. Add To Cart")
        print("3. Place Order")
        print("0. Logout")

    def browse_products(self):
        logger.info(f"{self.username} browsed products.")

    def add_to_cart(self):
        logger.info(f"{self.username} added product to cart.")
        
    def place_order(self):
        logger.info(f"{self.username} placed order.")


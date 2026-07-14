import csv
import os

from logger_config import logger
from exceptions import CSVFileError
import os

print("Current Directory:", os.getcwd())

class CSVManager:

    def __init__(self):

        os.makedirs("data", exist_ok=True)

        self.users_file = "data/users.csv"
        self.products_file = "data/products.csv"
        self.orders_file = "data/orders.csv"
        self.cart_file = "data/cart.csv"

        self.create_files()

    def create_files(self):

        files = {

            self.users_file: [
                "user_id",
                "username",
                "name",
                "email",
                "password_hash",
                "role"
            ],

            self.products_file: [
                "product_id",
                "seller_id",
                "product_name",
                "category",
                "price",
                "stock"
            ],

            self.orders_file: [
                "order_id",
                "customer_id",
                "product_id",
                "quantity",
                "total"
            ],

            self.cart_file: [
                "customer_id",
                "product_id",
                "quantity"
            ]

        }

        try:

            for file, header in files.items():

                if not os.path.exists(file):

                    with open(file, "w", newline="") as f:

                        writer = csv.writer(f)

                        writer.writerow(header)

            logger.info("CSV Files Created")

        except Exception as e:

            logger.exception(e)

            raise CSVFileError("Unable to create CSV files.")

    def read_all(self, filename):

        try:

            with open(filename, "r", newline="") as f:

                reader = csv.DictReader(f)

                return list(reader)

        except Exception as e:

            logger.exception(e)

            raise CSVFileError("Unable to read CSV.")

    def append_row(self, filename, row):

        try:

            with open(filename, "a", newline="") as f:

                writer = csv.writer(f)

                writer.writerow(row)

        except Exception as e:

            logger.exception(e)

            raise CSVFileError("Unable to write CSV.")

    def overwrite(self, filename, headers, rows):

        try:

            with open(filename, "w", newline="") as f:

                writer = csv.DictWriter(
                    f,
                    fieldnames=headers
                )

                writer.writeheader()

                writer.writerows(rows)

        except Exception as e:

            logger.exception(e)

            raise CSVFileError("Unable to overwrite CSV.")
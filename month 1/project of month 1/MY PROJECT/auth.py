import csv
import hashlib
from logger_config import logger
import pwinput

USER_FILE = "users.csv"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def registration(role):

    username = input("Enter Username : ").strip()

    password = pwinput.pwinput(prompt="Enter Password : ", mask="*")

    with open(USER_FILE, "a+", newline="") as file:

        file.seek(0)

        reader = csv.DictReader(file)

        for row in reader:

            if row["Username"] == username:

                print("User Already Exists")

                logger.warning("Duplicate Username")

                return

        fieldnames = ["Role", "Username", "Password"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:

            writer.writeheader()

        writer.writerow({
            "Role": role,
            "Username": username,
            "Password": hash_password(password)
        })

    logger.info(f"{username} Registered")

    print("Registration Successful")


def login(role):

    username = input("Enter Username : ")

    password = pwinput.pwinput(prompt="Enter Password : ", mask="*")

    with open(USER_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if (row["Role"] == role and
                    row["Username"] == username and
                    row["Password"] == hash_password(password)):

                logger.info(f"{username} Logged In")

                print("Login Successful")

                return username

    print("Invalid Username or Password")

    logger.warning("Login Failed")

    return None
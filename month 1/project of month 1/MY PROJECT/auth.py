import csv
import hashlib
import os
import pwinput
from logger_config import logger

USER_FILE = "users.csv"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def registration(role):
    username = input("Enter Username: ").strip()

    password = pwinput.pwinput(
        prompt="Enter Password: ",
        mask="*"
    )

    fieldnames = ["Role", "Username", "Password"]

    try:
        # Create file with header if it doesn't exist or is empty
        if not os.path.exists(USER_FILE) or os.path.getsize(USER_FILE) == 0:
            with open(USER_FILE, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

        # Check if username already exists
        with open(USER_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Username"].lower() == username.lower():
                    print("User Already Exists.")
                    logger.warning(f"Duplicate username: {username}")
                    return

        # Save new user
        with open(USER_FILE, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writerow({
                "Role": role,
                "Username": username,
                "Password": hash_password(password)
            })

        print("Registration Successful.")
        logger.info(f"{username} registered as {role}")

    except Exception as e:
        print("Registration Failed.")
        logger.exception(e)


def login(role):
    username = input("Enter Username: ").strip()

    password = pwinput.pwinput(
        prompt="Enter Password: ",
        mask="*"
    )

    try:
        if not os.path.exists(USER_FILE):
            print("No users registered.")
            return None

        with open(USER_FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if (
                    row["Role"] == role
                    and row["Username"] == username
                    and row["Password"] == hash_password(password)
                ):

                    print("Login Successful.")
                    logger.info(f"{username} logged in.")

                    return username

        print("Invalid Username or Password.")
        logger.warning(f"Failed login attempt for {username}")

        return None

    except Exception as e:
        print("Login Failed.")
        logger.exception(e)
        return None
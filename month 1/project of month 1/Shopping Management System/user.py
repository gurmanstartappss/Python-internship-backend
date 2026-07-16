"""
user.py

Base User Class
"""

from abc import ABC, abstractmethod
import hashlib

from exceptions import (
    InvalidEmailError,
    InvalidPasswordError,
    InvalidRoleError
)

from logger_config import logger


class User(ABC):

    __slots__ = (
        "_user_id",
        "_username",
        "_name",
        "_email",
        "__password_hash",
        "_role"
    )

    def __init__(
        self,
        user_id,
        username,
        name,
        email,
        password_hash,
        role
    ):

        self._user_id = user_id
        self.username = username
        self.name = name
        self.email = email
        self.role = role

        self.__password_hash = password_hash


    @property
    def user_id(self):
        return self._user_id


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):

        value = value.strip()

        if value == "":
            raise ValueError("Username cannot be empty.")

        self._username = value


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        value = value.strip()

        if value == "":
            raise ValueError("Name cannot be empty.")

        self._name = value


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):

        value = value.strip()

        if (
            value == ""
            or
            "@" not in value
            or
            "." not in value
        ):
            raise InvalidEmailError(
                "Invalid Email."
            )

        self._email = value



    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):

        value = value.lower()

        if value not in (
            "admin",
            "seller",
            "customer"
        ):
            raise InvalidRoleError(
                "Invalid Role."
            )

        self._role = value



    def verify_password(self, entered_hash):

        return (
            entered_hash
            ==
            self.__password_hash
        )

    def change_password(
        self,
        old_password,
        new_password
    ):

        old_hash = hashlib.sha256(
            old_password.encode()
        ).hexdigest()

        if not self.verify_password(old_hash):

            raise InvalidPasswordError(
                "Old password is incorrect."
            )

        if len(new_password) < 6:

            raise InvalidPasswordError(
                "Password must contain at least 6 characters."
            )

        self.__password_hash = hashlib.sha256(
            new_password.encode()
        ).hexdigest()

        logger.info(
            f"{self.username} changed password."
        )


    def display_profile(self):

        print("\n========== PROFILE ==========")

        print("User ID :", self.user_id)
        print("Username :", self.username)
        print("Name :", self.name)
        print("Email :", self.email)
        print("Role :", self.role)

        print("=============================\n")



    def __str__(self):

        return (
            f"{self.user_id} | "
            f"{self.username} | "
            f"{self.name} | "
            f"{self.role}"
        )

    def __repr__(self):

        return (
            f"User("
            f"{self.user_id}, "
            f"{self.username}, "
            f"{self.email})"
        )

    def __eq__(self, other):

        if not isinstance(other, User):
            return False

        return self.user_id == other.user_id



    @abstractmethod
    def show_menu(self):
        pass
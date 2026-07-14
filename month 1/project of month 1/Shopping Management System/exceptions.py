"""
exceptions.py

Contains all custom exceptions used in
Online Shopping System.
"""


class ShoppingSystemError(Exception):
    """Base Exception for Shopping System"""
    pass


class InvalidEmailError(ShoppingSystemError):
    pass


class InvalidPasswordError(ShoppingSystemError):
    pass


class InvalidRoleError(ShoppingSystemError):
    pass


class DuplicateEmailError(ShoppingSystemError):
    pass


class DuplicateUsernameError(ShoppingSystemError):
    pass


class AuthenticationError(ShoppingSystemError):
    pass


class UserNotFoundError(ShoppingSystemError):
    pass


class ProductNotFoundError(ShoppingSystemError):
    pass


class OutOfStockError(ShoppingSystemError):
    pass


class EmptyCartError(ShoppingSystemError):
    pass


class CSVFileError(ShoppingSystemError):
    pass
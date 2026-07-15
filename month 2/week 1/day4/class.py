# # advanced exception handling 

# class InvalidAgeError(Exception):
#     pass
# try:
#     age =int(input("enter age "))
#     if age<0:
#         raise InvalidAgeError("enter positive age")
#     print("age is positive")
# except Exception as e:
#     print (e)


# class InvalidMarksException(Exception):
#     pass
# try:
#     marks=int(input("enter marks "))
#     if marks<=0 or marks>100:
#         raise InvalidMarksException("invalid marks")
#     print("marks are correct")
# except Exception as e:
#     print(e)
    
"""chain exceptions(chaining)--means linking one exception to another so that the original cause is preserved(used for debugging)"""

# try:
#     code for exception 
# except someException as e:
#     raise NewException ("custom message") from e

# class InvalidAgeError():
#     pass
# try:
#     with

#     print("age is positive")
#     result = int("python")

# except InvalidAgeError as e:
#     print("accept only positive age", e)

# except ValueError as e:
#     raise Exception("Failed to convert string into integer") from e

#Logging Exceptions: means recording errors in a
# log file instead of only displaying them on the screen.
# logs help developers analyze ,debug for deployment

# import logging
# logging.basicConfig(
#     filename="classlog.py",
#     level=logging.ERROR,
# )
# parameter:filename,level(DEBUG,INFO,WARNING,ERROR,CRITICAL)

# DEBUG: Detailed debugging information
# INFO: general application events
# WARNING: something unexpected but application continues
# ERROR : an error occurred
# CRITICAL : very serious error, application may stop

import logging

logging.basicConfig(
    filename="file.log",
    level=logging.DEBUG,
    format="%(asctime)s- %(levelname)s-%(message)s"
)
logging.debug("Debugging application")
logging.info("")
logging.warning("insuffient space")
logging.debug("Debugging application")
logging.error("program error")
logging.critical("server crashed")

try:
    result = 100/0

except ZeroDivisionError:
    logging.exception("Unable to read")#logging exceptions--logs the error message plus the complete traceback
    
try:
    with open("students.txt", "r") as file:
        print(file.read())

except FileNotFoundError as e:
    logging.error(e)# logging error-logs only error message
    
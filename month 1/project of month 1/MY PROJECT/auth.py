from logger_config import logger
import logging
import hashlib
import csv

def registration(role):
    value = False
    fieldname=["Role","Username","Password"]
    user=input("enter your username ")
    password=input("enter your password ")
    hash_password=hashlib.sha256(password.encode()).hexdigest()
    with open("admin.csv","a+",newline="") as file:
        write=csv.DictWriter(file,fieldnames=fieldname)
        file.seek(0)
        reader=csv.DictReader(file)
        for row in reader:
            if row["Username"]==user:
                print("User Already Exists ")
                logging.info("User Already Exists")  
                value = True
                break
        if not value:
            if file.tell()==0:
                write.writeheader()
            write.writerow({"Role":role,"Username":user,"Password":hash_password})
            print("Registration Successful")
            logging.info("Registration Successful")
            
def login(role):
    user=input("enter your username ")
    password=input("enter your password ")
    hash_password=hashlib.sha256(password.encode()).hexdigest()
    with open("admin.csv","r",newline="") as file:
        read=csv.DictReader(file)
        for row in read:
            if row["Role"]==role and row["Username"]==user and row["Password"]==hash_password:
                print("Logged in Successfully")
                logging.info("user logged in successfully")
                return True
        else:
            print("login Unsuccessful")
            logging.error("login Unsuccessful")
            return False
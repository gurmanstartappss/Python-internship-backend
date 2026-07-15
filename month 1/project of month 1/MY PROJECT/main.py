import auth
import customer
import seller
import logger_config
import logging

print("======================Welcome to Student Management System=========================")
while True:
    print("Who are you? \n1) SELLER \n2) CUSTOMER \n3) EXIT")
    while True:
        try:
            n=int(input("enter your choice "))
            break
        except Exception as e:
            print("Enter Only Numbers ")
            logging.error(e)
    if n==1:
        while True:
            print("Do you want to:- \n1) Register \n2) Login \n3) EXIT ")
            while True:
                try:
                    y=int(input("enter your choice "))
                    break
                except Exception as e:
                    print("Enter Only Numbers ")
                    logging.error(e)
            if y==1:
                auth.registration("SELLER")
            elif y==2:
                if auth.login("SELLER"):
                    seller.Sel()
            elif y==3:
                print("App Exited")
                logging.info("App Exited")
                break
            else:
                print("enter valid choice")                    

    elif n==2:
        while True:
            print("Do you want to:- \n1) Register \n2) Login \n3) EXIT ")
            while True:
                try:
                    y=int(input("enter your choice "))
                    break
                except Exception as e:
                    print("Enter Only Numbers ")
                    logging.error(e)
            if y==1:
                auth.registration("CUSTOMER")
            elif y==2:
                if auth.login("CUSTOMER"):
                    customer.Cus()
            elif y==3:
                print("App Exited")
                logging.info("App Exited")
                break
            else:
                print("enter valid choice")   
    elif n==3:
        print("App Exited")
        logging.info("App Exited")
        break
    else:
        print("enter valid choice")
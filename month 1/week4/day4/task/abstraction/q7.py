
from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass

class GoogleLogin(Authentication):
    def login(self):
        print("Login with Google")

class EmailLogin(Authentication):
    def login(self):
        print("Login with Email")

class FacebookLogin(Authentication):
    def login(self):
        print("Login with Facebook")

g = GoogleLogin()
e = EmailLogin()
f = FacebookLogin()

g.login()
e.login()
f.login()

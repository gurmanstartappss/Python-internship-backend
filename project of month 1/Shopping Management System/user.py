class User():
    def __init__(self,user_id,name,email,password_hash,role):
        self._user_id=user_id
        self.name=name
        self.email=email
        self.__password_hash=password_hash 
        self._role=role

    def display_profile(self):
        print("============DISPLAY INFO===============")
        print("User ID is",self._user_id)
        print("User name is",self.name)
        print("User email is",self._email)
        print("User role is",self._role)
        print("=======================================")
        print(" ")

    # getter and setter of name
    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self,new_name):
        if new_name.strip()=="":
            raise ValueError("empty name field")
        else:
            self._name=new_name
            
    # getter and setter of email
    @property
    def email(self):
        return self._email
    
    @email.setter 
    def email(self,new_email):       
        if new_email.strip()!="" and "@" in new_email and ".com" in new_email:
            self._email=new_email
        else:
            raise ValueError("invalid email")
        
    #getter and setter of role
    @property
    def role(self):
        return self._role
    
    @role.setter 
    def role(self,new_role):       
        if new_role.strip()!="" and "@" in new_role and ".com" in new_role:
            self._role=new_role
        else:
            raise ValueError("invalid email")
    
    
    def verify_password(self,entered_hash):
        if entered_hash==self.__password_hash:
            return True
        else:
            return False
        4
        
        
        
        
        
        
        
        
        
        
x=User(101,"gurman","gg@gmail.com","ggg","hahahah")
x.display_profile()
x.name="avantika"
x.display_profile()

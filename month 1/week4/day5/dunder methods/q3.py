class Cart():
    def __init__(self,products):
        self.products=products
        
    def __len__(self):
        return len(self.products)
    
catu=Cart(["pencil","pen","razer"])

for i in catu.products:
    
    print(len(i))
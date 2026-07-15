from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    product_name: str
    price: float
    quantity: int


p1 = Product(101, "Laptop", 50000, 2)

print(p1)

total = p1.price * p1.quantity
print("Total Price:", total)
from product import Product
from product_manager import ProductManager
from cart import Cart
manager = ProductManager()

manager.add_product(Product("Laptop", 3500, 10))
manager.add_product(Product("Mouse", 150, 50))
manager.add_product(Product("Tastatura", 300, 30))

cart = Cart()
cart.add_product(manager.products[0])
cart.add_product(manager.products[1])
cart.add_product(manager.products[2])

cart.display_cart()
cart.total_cart_value()
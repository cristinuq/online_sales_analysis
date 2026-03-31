from product import Product
from product_manager import ProductManager
from cart import Cart
manager = ProductManager()

manager.add_product(Product("Laptop Ultra", 3500, 5))
manager.add_product(Product("Mouse Bluetooth", 200, 40))
manager.add_product(Product("Tastatura Gaming", 500, 15))

cart = Cart()
cart.add_product(manager.products[0])
cart.add_product(manager.products[1])
cart.add_product(manager.products[2])

cart.display_cart()
cart.total_cart_value()

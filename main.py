from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Laptop", 3500, 10))
manager.add_product(Product("Mouse", 150, 50))
manager.add_product(Product("Tastatura", 300, 30))

manager.display_products()
manager.total_inventory_value()

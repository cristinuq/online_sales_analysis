from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Laptop Ultra", 3500, 5))
manager.add_product(Product("Mouse Bluetooth", 200, 40))
manager.add_product(Product("Tastatura Gaming", 500, 15))


from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Produsul '{product.name}' a fost adăugat.")

    def display_products(self):
        print("\n--- Lista produse ---")
        for product in self.products:
            product.display()

    def total_inventory_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        print(f"\nValoarea totală a inventarului: {total} lei")
        return total
    
    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Produsul '{name}' a fost eliminat.")
                return
        print(f"Produsul '{name}' nu a fost găsit.")    
        
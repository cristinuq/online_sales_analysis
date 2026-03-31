class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)
        print(f"'{product.name}' a fost adăugat în coș.")

    def total_cart_value(self):
        total = sum(p.price * p.quantity for p in self.cart_items)
        print(f"\nTotal de plată: {total} lei")
        return total

    def display_cart(self):
        print("\n--- Conținut coș ---")
        for product in self.cart_items:
            product.display()
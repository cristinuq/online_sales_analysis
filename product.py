class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"Produs: {self.name} | Preț: {self.price} lei | Cantitate: {self.quantity}")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Cantitatea pentru '{self.name}' a fost actualizată la {self.quantity}.")
        
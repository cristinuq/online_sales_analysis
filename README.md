# Online Sales Analysis

## Descriere
Proiect Python pentru analiza vânzărilor unui magazin online.
Permite gestionarea produselor și a coșului de cumpărături.

## Clase

### `Product` (product.py)
Reprezintă un produs din magazin.
- **Atribute:** `name`, `price`, `quantity`
- **Metode:** `display()`, `update_quantity(new_quantity)`

### `ProductManager` (product_manager.py)
Gestionează lista de produse disponibile.
- **Metode:** `add_product()`, `display_products()`, `total_inventory_value()`, `remove_product(name)`

### `Cart` (cart.py)
Gestionează coșul de cumpărături al clientului.
- **Metode:** `add_product()`, `display_cart()`, `total_cart_value()`

## Utilizare
```bash
python main.py
```

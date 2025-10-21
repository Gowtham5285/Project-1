class Product:
    """Represents a single product in the store."""
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price


class CartItem:
    """Represents an item in the shopping cart."""
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        """Calculate subtotal for this item."""
        return self.product.price * self.quantity


class ShoppingCart:
    """Manages all cart operations."""
    MAX_ITEMS = 8  # limit as per requirements

    def __init__(self):
        self.cart_items = []

    def add_item(self, product, quantity):
        """Add a product to the cart or update quantity if it already exists."""
        if len(self.cart_items) >= ShoppingCart.MAX_ITEMS:
            print("\n⚠️ Cart is full! You can only add up to 8 items.\n")
            return

        for item in self.cart_items:
            if item.product.id == product.id:
                item.quantity += quantity
                print(f"\n✅ Updated {product.name} quantity to {item.quantity}.\n")
                return

        self.cart_items.append(CartItem(product, quantity))
        print(f"\n🛒 Added {product.name} (x{quantity}) to cart.\n")

    def view_cart(self):
        """Display all items in the cart."""
        if not self.cart_items:
            print("\n🛍️ Your cart is empty.\n")
            return

        print("\n===== Your Cart =====")
        total = 0
        for item in self.cart_items:
            subtotal = item.subtotal()
            total += subtotal
            print(f"ID: {item.product.id} | {item.product.name} | ₹{item.product.price} x {item.quantity} = ₹{subtotal}")
        print(f"--------------------------\nTotal Amount: ₹{total}\n")

    def update_item(self, product_id, quantity):
        """Update the quantity of a product in the cart."""
        for item in self.cart_items:
            if item.product.id == product_id:
                item.quantity = quantity
                print(f"\n✏️ Updated {item.product.name} quantity to {quantity}.\n")
                return
        print("\n⚠️ Product not found in cart.\n")

    def remove_item(self, product_id):
        """Remove a product from the cart."""
        for item in self.cart_items:
            if item.product.id == product_id:
                self.cart_items.remove(item)
                print(f"\n🗑️ Removed {item.product.name} from cart.\n")
                return
        print("\n⚠️ Product not found in cart.\n")

    def checkout(self):
        """Display final bill and clear the cart."""
        if not self.cart_items:
            print("\n🛒 Your cart is empty. Nothing to checkout.\n")
            return

        print("\n===== Checkout =====")
        total = 0
        for item in self.cart_items:
            subtotal = item.subtotal()
            total += subtotal
            print(f"{item.product.name} x {item.quantity} = ₹{subtotal}")
        print(f"--------------------------\nTotal Bill: ₹{total}")
        print("\n🎉 Thank you for shopping with us!\n")

        self.cart_items.clear()


class Shop:
    """Main store with products and menu interface."""
    def __init__(self):
        self.products = [
            Product(1, "Laptop", 45000),
            Product(2, "Smartphone", 15000),
            Product(3, "Headphones", 2000),
            Product(4, "Keyboard", 1200),
            Product(5, "Mouse", 800),
            Product(6, "Charger", 500),
            Product(7, "USB Cable", 300),
            Product(8, "Backpack", 2500)
        ]
        self.cart = ShoppingCart()

    def view_products(self):
        """Display all available products."""
        print("\n===== Available Products =====")
        for p in self.products:
            print(f"ID: {p.id} | {p.name} | Price: ₹{p.price}")
        print()

    def get_product_by_id(self, product_id):
        """Find a product by ID."""
        for p in self.products:
            if p.id == product_id:
                return p
        return None

    def menu(self):
        """Display the shopping menu."""
        while True:
            print("===== Shopping Cart =====")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. View Cart")
            print("4. Update Cart")
            print("5. Remove from Cart")
            print("6. Checkout")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == '7':
                print("\n👋 Thank you for visiting! Goodbye!\n")
                break

            if choice == '1':
                self.view_products()

            elif choice == '2':
                try:
                    self.view_products()
                    pid = int(input("Enter Product ID to add: "))
                    qty = int(input("Enter quantity: "))
                    product = self.get_product_by_id(pid)
                    if product:
                        self.cart.add_item(product, qty)
                    else:
                        print("\n⚠️ Invalid Product ID.\n")
                except ValueError:
                    print("\n⚠️ Invalid input. Please enter numeric values.\n")

            elif choice == '3':
                self.cart.view_cart()

            elif choice == '4':
                try:
                    pid = int(input("Enter Product ID to update: "))
                    qty = int(input("Enter new quantity: "))
                    self.cart.update_item(pid, qty)
                except ValueError:
                    print("\n⚠️ Invalid input. Please enter numeric values.\n")

            elif choice == '5':
                try:
                    pid = int(input("Enter Product ID to remove: "))
                    self.cart.remove_item(pid)
                except ValueError:
                    print("\n⚠️ Invalid input. Please enter numeric values.\n")

            elif choice == '6':
                self.cart.checkout()

            else:
                print("\n⚠️ Invalid choice. Please select 1-7.\n")


# ---------- Main Program ----------
if __name__ == "__main__":
    shop = Shop()
    shop.menu()

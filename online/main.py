# main.py
from store import Store

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Please enter a valid number.")

def main():
    store = Store()

    # Add some sample products if empty
    if not store.products:
        sample_products = [
            Product("P001", "Laptop", 50000, 10),
            Product("P002", "Mouse", 500, 50),
            Product("P003", "Keyboard", 1200, 30),
        ]
        for p in sample_products:
            store.products[p.product_id] = p
        store.save_all_data()

    while True:
        print("\n ONLINE SHOPPING CART")
        if store.current_user:
            print(f" Logged in: {store.current_user.username}")
            print("1. Browse Products")
            print("2. Add to Cart")
            print("3. View Cart")
            print("4. Place Order")
            print("5. Logout")
        else:
            print("1. Register")
            print("2. Login")
            print("3. Browse Products (Guest)")
            print("4. Exit")

        choice = input("Choose: ").strip()

        if store.current_user:
            if choice == '1':
                store.browse_products()
            elif choice == '2':
                store.browse_products()
                pid = input("Enter Product ID: ").strip()
                qty = get_int_input("Quantity: ")
                try:
                    store.add_to_cart(pid, qty)
                except ValueError as e:
                    print(f" {e}")
            elif choice == '3':
                store.view_cart()
            elif choice == '4':
                try:
                    store.place_order()
                except ValueError as e:
                    print(f" {e}")
            elif choice == '5':
                store.logout()
            else:
                print(" Invalid option.")
        else:
            if choice == '1':
                print("\n REGISTER")
                username = input("Username: ").strip()
                password = input("Password (min 6 chars): ").strip()
                email = input("Email: ").strip()
                try:
                    store.register_user(username, password, email)
                except ValueError as e:
                    print(f" {e}")
            elif choice == '2':
                print("\n LOGIN")
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                store.login(username, password)
            elif choice == '3':
                store.browse_products()
            elif choice == '4':
                print(" Thank you for visiting!")
                break
            else:
                print(" Invalid option.")

if __name__ == "__main__":
    main()
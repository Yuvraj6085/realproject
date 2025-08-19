
import getpass
from atm import ATM

def get_float_input(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(" Invalid number. Please try again.")

def get_account_number_input(prompt: str) -> str:
    """Gets a non-empty account number from the user."""
    while True:
        acc_num = input(prompt).strip()
        if acc_num:
            return acc_num
        else:
            print(" Account number cannot be empty. Please try again.")

def get_pin_input(prompt: str) -> str:
    """Gets a 4-digit PIN from the user, hiding the input."""
    while True:
        pin = getpass.getpass(prompt).strip()
        if len(pin) == 4 and pin.isdigit():
            return pin
        else:
            print(" Invalid PIN. Must be a 4-digit number. Please try again.")

def main():
    atm = ATM()

    while True:
        print("\n" + "="*40)
        print(" WELCOME TO PYTHON ATM")
        print("="*40)
        print("""1. Login
2. Create New Account
3. Exit""")

        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            print("\n LOGIN")
            acc_num = get_account_number_input("Enter account number: ")
            pin = get_pin_input("Enter 4-digit PIN: ")

            if atm.authenticate(acc_num, pin):
                print(f" Login successful! Welcome, {acc_num}.")
                atm_menu(atm)
            else:
                print(" Invalid account number or PIN.")

        elif choice == '2':
            print("\n CREATE NEW ACCOUNT")
            acc_num = get_account_number_input("Choose account number: ")
            pin = get_pin_input("Set 4-digit PIN: ")
            initial = get_float_input("Initial deposit (₹): ")

            try:
                atm.create_account(acc_num, pin, initial)
            except ValueError as e:
                print(f" Account creation failed: {e}")

        elif choice == '3':
            print(" Thank you for using Python ATM. Goodbye!")
            break

        else:
            print(" Invalid choice. Please enter 1, 2, or 3.")

def atm_menu(atm: ATM):
    while True:
        print(f"\n ACCOUNT: {atm.current_account.account_number}")
        print("ATM MENU")
        print("""1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Logout""")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            print(f" Your balance: ₹{atm.check_balance():.2f}")

        elif choice == '2':
            amount = get_float_input("Enter deposit amount (₹): ")
            try:
                atm.deposit(amount)
                print(f" ₹{amount:.2f} deposited successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            amount = get_float_input("Enter withdrawal amount (₹): ")
            try:
                atm.withdraw(amount)
                print(f" ₹{amount:.2f} withdrawn successfully!")
            except ValueError as e:
                print(f" Error: {e}")

        elif choice == '4':
            history = atm.show_transaction_history()
            if not history:
                print(" No transactions yet.")
            else:
                print("\nTRANSACTION HISTORY:")
                print("-" * 60)
                for tx in history:
                    print(f"{tx['timestamp']} | {tx['type']} | ₹{tx['amount']:.2f} | Balance: ₹{tx['balance_after']:.2f}")
                print("-" * 60)

        elif choice == '5':
            atm.logout()
            print(" Logged out successfully.")
            break

        else:
            print(" Invalid option. Choose 1-5.")

if __name__ == "__main__":
    main()
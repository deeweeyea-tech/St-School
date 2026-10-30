class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        # Double underscore (__) makes these private (encapsulation)
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount. Enter a positive number.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance. Withdrawal not allowed.")
        elif amount <= 0:
            print("Invalid amount. Enter a positive number.")
        else:
            self.__balance = self.__balance - amount
            print("Amount withdrawn successfully.")

    def check_balance(self):
        print("Account Number:", self.__account_number)
        print("Account Holder:", self.__holder_name)
        print("Balance:", self.__balance)


# Create an account
account = BankAccount(1001, "Divya", 50000)

# Menu-driven program
while True:
    print()
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == 3:
        account.check_balance()
    elif choice == 4:
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid choice. Please try again.")
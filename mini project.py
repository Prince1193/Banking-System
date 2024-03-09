import os

class Account:
    def __init__(self, accno, acc_name, balance):
        self.accno = accno
        self.acc_name = acc_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def get_balance(self):
        return f"Account balance for {self.acc_name}: ${self.balance}"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, accno):
        for account in self.accounts:
            if account.accno == accno:
                return account
        return None

    def save_account(self, bank):
        with open('bank.txt', 'w') as file:
            for account in self.accounts:
                file.write(f"{account.accno},{account.acc_name},{account.balance}\n")

    def load_account(self, bank):
        if os.path.exists('bank.txt'):
            with open('bank.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    account_info = line.strip().split(',')
                    if len(account_info) == 3:
                        accno, acc_name, balance = account_info
                        account = Account(int(accno), acc_name, float(balance))
                        self.add_account(account)

if __name__ == '__main__':
    bank = Bank()

    bank.load_account('bank.txt')

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            accno = int(input("Enter Account Number: "))
            acc_name = input("Enter Account Holder Name: ")
            initial_balance = float(input("Enter Initial Balance: "))
            account = Account(accno, acc_name, initial_balance)
            bank.add_account(account)
        elif choice == '2':
            accno = int(input("Enter Account Number: "))
            account = bank.find_account(accno)
            if account:
                amount = float(input("Enter the deposit amount: "))
                print(account.deposit(amount))
            else:
                print("Account not found.")
        elif choice == '3':
            accno = int(input("Enter Account Number: "))
            account = bank.find_account(accno)
            if account:
                amount = float(input("Enter the withdrawal amount: "))
                print(account.withdraw(amount))
            else:
                print("Account not found.")
        elif choice == '4':
            accno = int(input("Enter Account Number: "))
            account = bank.find_account(accno)
            if account:
                print(account.get_balance())
            else:
                print("Account not found.")
        elif choice == '5':
            bank.save_account('bank.txt')
            print("Exiting the Banking System. Accounts data saved.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

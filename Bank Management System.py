class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.loans = {}

    def create_account(self, account_holder_name, initial_balance, account_type):
        account_number = len(self.accounts) + 1
        account = Account(account_number, account_holder_name, initial_balance, account_type)
        self.accounts[account_number] = account
        print(f'Account created successfully! Account number: {account_number}')

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f'Account {account_number} closed successfully.')
        else:
            print("Account not found.")
    
    def approve_loan(self, account_number, loan_amount, interest_rate):
        if account_number in self.accounts:
            loan = Loan(account_number, loan_amount, interest_rate)
            self.loans[account_number] = loan
            print("Loan approved successfully.")
        else:
            print("Account not found.")

class Account:
    def __init__(self, account_number, account_holder_name, initial_balance, account_type):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
        self.account_type = account_type
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance in account.")
    
    def check_balance(self):
        return self.balance
    
class Loan:
    def __init__(self, account_number, loan_amount, interest_rate):
        self.account_number = account_number
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.approval_status = False

    def approve_loan(self):
        self.approval_status = True

def main():
    bank_name = input("Enter bank name: ")
    bank = Bank(bank_name)
    while True:
        print("\nBank Management System Menu:")
        print("1. Create Account")
        print("2. Close Account")
        print("3. Approve Loan")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_holder_name = input("Enter the account holder name: ")
            initial_balance = float(input("Enter the initial balance: "))
            account_type = input("Enter account type: ")
            bank.create_account(account_holder_name, initial_balance, account_type)
        
        elif choice == "2":
            account_number = int(input("Enter account number to close: "))
            bank.close_account(account_number)

        elif choice == "3":
            account_number = int(input("Enter account number to approve the loan: "))
            loan_amount = float(input("Enter the amount you wish to loan: "))
            interest_rate = float(input("Enter the interest rate: "))
            bank.approve_loan(account_number, loan_amount, interest_rate)

        elif choice == "4":
            print("Exiting the program. Thank you!")
            break

if __name__ == "__main__":
    main()
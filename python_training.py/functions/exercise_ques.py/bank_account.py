# **Create a class BankAccount with the following attributes: account_number, owner, and balance. Implement methods to:

#  ~ Deposit money
#  ~ Withdraw money
#  ~ Display account details

class bank_account():                                                 #create a class bank_account
    def __init__(self, account_number, owner, balance=0):             #__init__ method initialize 
        self.account_number = account_number                          #attributes
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):                                        #method creation for deposit
        self.balance += amount                                        #self.balance = self.balance + amount
        print(f"Deposited {amount} --- New Balance is {self.balance}")

    def withdraw(self, amount):                                       #method creation for withdraw
        if amount > self.balance:
            print("Balance not sufficient")
        else:
            self.balance -= amount
            print(f"withdraw {amount} --- New balance is {self.balance}")

    def display(self):                                                 #method creation display account
        print(f"Account Number : {self.account_number} \n Owner : {self.owner} \n Balance : {self.balance}")


account = bank_account("123456", "RDJ")                                #creatting instance(object) for bank_account

while True:                                                            #while true is continous user iteraction , needs explicitly exit 
    action = input("What you will do \n deposit ~ withdraw ~ display ~ exit : ").lower()   # required action for choose user want what to do 

    if action == "deposit":                                            #condition to deposit
        amount = float(input("Enter the deposit amount : "))
        account.deposit(amount)

    elif action == "withdraw":                                         #condition to withdraw
        amount = float(input("Enter the withdraw amount : "))
        account.withdraw(amount)

    elif action == "display":                                          #condition to display
        account.display()

    elif action == "exit":                                             #condition to exit 
        print("Thank you.")
        break                                                          #apply break condition otherwise the loop will continue to again

    else :
        print("Invalid option")
class RBI:                                                       #parent class
    def __init__(self,deposit,withdraw):                         #initialisation with __init__()
        self.deposit = deposit
        self.withdraw = withdraw
    
    def display(self):                                            
        print(f"Deposit amount = {self.deposit}, Withdarwal amount = {self.withdraw}")

class SBI(RBI):                                                   #child class of parent class RBI
    def __init__(self ,deposit,withdraw):
        super().__init__(deposit,withdraw)
        print("This is data for SBI : ")

class BOI(RBI):                                                   #child class of parent class RBI
    def __init__(self,deposit,withdraw):
        super().__init__(deposit,withdraw)
        print("This is data for BOI : ")

class ICICI(RBI):                                                 #child class of parent class RBI
    def __init__(self,deposit,withdraw):
        super().__init__(deposit,withdraw)
        print("This is data for ICICI : ")

class PNB(RBI):                                                   #child class of parent class RBI
    def __init__(self,deposit,withdraw):
        super().__init__(deposit,withdraw)
        print("This is data for PNB :")

def choose_bank():
    bank_choice = input("Choose Bank for Operations : 'SBI' , 'BOI' , 'ICICI' , 'PNB'")

    deposit = float(input("Enter the deposit amount : "))
    withdraw = float(input("Enter the withdrawal amount : "))

    if bank_choice.upper() == "SBI":
        bank = SBI(deposit,withdraw)
    elif bank_choice.upper() == "BOI":
        bank = BOI(deposit,withdraw)
    elif bank_choice.upper() == "ICICI":
        bank = ICICI(deposit,withdraw)
    elif bank_choice.upper() == "PNB":
        bank = PNB(deposit,withdraw)
    else:
        print("Choose within the option only")
        return

    bank.display()

choose_bank()
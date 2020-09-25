class BankAccount:
    def ManageAccount():
        kontonummer = int(input("Ange kontonumer>: "))
        print("****KONTOMENY****")
        print("1. Ta ut pengar")
        print("2. Sätt in pengar")
        print("3. Visa saldo")
        print("4. Avsluta")
        selected = int(input("Ange menyval> "))
        if selected == "1":
            print(int(input("Ange belopp ")))
    
    def __init__(self, name, balance=0.00):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """make a deposit"""
        self.balance += amount

    def withdraw(self, amount):
        """make a withdraw"""
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def get_balance(self): #are accessor methods needed in Python?
        """check the balance"""
        return self.balance
    while True:
        print("****HUVUDMENY****")
        print("1. Skapa konto")
        print("2. Administrera konto")
        print("3. Avsluta")
        selected = int(input("Ange menyval> "))
        if(selected == 3):
            break;
        if(selected == 1):
            RegisterAccount()
            if(selected == 2):
                ManageAccount()
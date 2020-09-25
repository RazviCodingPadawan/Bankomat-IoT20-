konto={}

class BankAccount:
    def __init__(self):

    def deposit(self): 
        amount = float(input("Enter amount to be deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:", amount)

    def withdraw(self): 
        amount = float(input("Enter amount to be withdrawn: ")) 
        if self.balance >= amount: 
            self.balance -= amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 


def RegisterAccount():
  kontonummer = int(input("Ange kontonumer>: "))
  if kontonummer not in Konto:
    print("Felmeddelande")
  
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
    
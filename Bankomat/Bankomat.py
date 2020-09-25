class BankAccount:
  def __init__(self, saldo = 0):
    self.saldo = saldo
    self.withdraw = withdraw
    self.deposit = deposit

  def getSaldo(self):
    return self.saldo

  def withdraw(self, amount):
    self.saldo -= amount
  
  def deposit(self, amount):
    self.saldo += amount



def RegisterAccount():
  kontonummer = int(input("Ange kontonumer>: "))
  while kontonummer < 1000 or kontonummer > 9999:
      kontonummer = int(input("Invalid kontonummer.. Re-enter: "))
  
def ManageAccount():
  kontonummer = int(input("Ange kontonumer>: "))
  while kontonummer < 1000 or kontonummer > 9999:
      kontonummer = int(input("Invalid kontonummer.. Re-enter: "))
  print("****KONTOMENY****")
  print("1. Ta ut pengar")
  print("2. Sätt in pengar")
  print("3. Visa saldo")
  print("4. Avsluta")
  selected = int(input("Ange menyval> "))
  if selected == 1:
    amt = float(input("Ange belöpp> "))
                
  if selected == 2:
    amt = float(input("Ange belöpp> "))
    
  if selected == 3:
    print("asda")

  if selected == 4:
    print("Transaction is now complete.")
    print("Thanks for choosing us as your bank")
    
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
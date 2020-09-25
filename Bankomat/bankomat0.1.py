Konto = {}

def RegisterAccount():
  kontonummer = int(input("Ange kontonumer>: "))
  for kontonnumer in Konto:
    if kontonummer in Konto:
      print("Felmeddelande")
    else:
      pass
  
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
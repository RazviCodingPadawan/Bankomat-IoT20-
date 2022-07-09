konto = {}



def RegisterAccount():
    kontonummer_tmp = int(input("Ange kontonumer>: "))
    while kontonummer_tmp < 1000 or kontonummer_tmp > 9999 or kontonummer_tmp in konto:
        kontonummer_tmp = int(input("Invalid kontonummer.. Re-enter: "))
    konto[kontonummer_tmp] = 0


def ManageAccount():
    kontonummer_tmp = int(input("Ange kontonumer>: "))
    while kontonummer_tmp < 1000 or kontonummer_tmp > 9999 or kontonummer_tmp not in konto:
        kontonummer_tmp = int(input("Invalid kontonummer.. Re-enter: "))
    print("****KONTOMENY**** - konto:", kontonummer_tmp)
    print("1. Ta ut pengar")
    print("2. Sätt in pengar")
    print("3. Visa saldo")
    print("4. Avsluta")
    selected = int(input("Ange menyval> "))
    if selected == 1:
      summa = float(input("Ange belöpp> "))
      while summa > konto[kontonummer_tmp]:
        summa = float(input("eroare "))
      konto[kontonummer_tmp] -= summa

    if selected == 2:
        konto[kontonummer_tmp] += float(input("Ange belöpp> "))

    if selected == 3:
        print("Saldo: " + str(konto[kontonummer_tmp]))

    if selected == 4:
        print("Transaction is now complete.")
        print("Thanks for choosing us as your bank")


while True:
    print("****HUVUDMENY****")
    print("1. Skapa konto")
    print("2. Administrera konto")
    print("3. Visa alla konton")
    print("4. Avsluta")
    selected = int(input("Ange menyval> "))
    if(selected == 4):
        break
    if(selected == 1):
        RegisterAccount()
    if(selected == 2):
        ManageAccount()
    if(selected == 3):
        print(konto)


"""   Om redan taget "Felmeddelande"
      Om belopp > saldo "Felmeddelande"
      Meny B (i inloggad läge)
- kunna lista transaktioner
- dvs varje uttag och insättning skall sparas i transaktionslogg för aktuellt konto - konton, saldon, transaktioner ska sparas i FIL. Och läsas in vid uppstart av programmet
- en transaktion består av datum konto belopp typ (ins/uttag)
 """

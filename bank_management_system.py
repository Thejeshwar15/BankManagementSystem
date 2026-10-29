class BankAccount:
  def __init__(self, name, balance):
    self.name= name
    self.__balance= balance

  def deposit(self, amount):
    if amount>0:
      self.__balance+= amount
      return "Deposit successful!"
    return "Invalid amount"

  def withdraw(self, amount):
      if amount<0:
         return "Invalid amount" 
       
      if amount> self.__balance:
         return "Invalid balance."  
      
      self.__balance -= amount
      return "Withdraw successful!"

  def show_balance(self):
    return self.__balance
  
  def show_info(self):
     return (f"Account Holder: {self.name}\nBalance: {self.__balance}")
     

account = BankAccount("Kafi", 1000)


while True:
   
    print("\n Bank Account System")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Info")
    print("5. Exit")

    try:
     choice= int(input("Enter your choice:"))

     if choice == 1:
       try:
          ask= int(input("Enter your deposit:"))
          print(account.deposit(ask))
       except ValueError:
          print("Please enter a valid amount!")

     elif choice == 2:
       try:
          ask= int(input("Enter your withdraw:"))
          print(account.withdraw(ask))
       except ValueError:
          print("Please enter a valid amount!")

     elif choice == 3:
       print(f"Your Balance is:{account.show_balance()}")

     elif choice == 4:
       print(account.show_info()) 

     elif choice == 5:
       print("Exit")
       break
     
     else:
       print("Invalid choice!") 

    except ValueError:
       print("Please enter a number from 1-5.") 
       continue  
  

class SavingsAccount(BankAccount):
   def __init__(self,name,balance,interest_rate):
     super().__init__(name, balance)
     self.interest_rate= interest_rate

   def add_interest(self):
      interest_amount= (self.show_balance()*self.interest_rate)/100

      self.deposit(interest_amount)

      return "Interest amount is added!"

   def withdraw(self, amount):
      if amount<=0:
         print("Transaction rejected!")
      else:   
         result =super().withdraw(amount+50)
         if result == "Withdraw successful!":
            return  f"{amount+50} is deducted"
         return "Insufficient balance"
   

class CurrentAccount(BankAccount):
   pass

accounts= [SavingsAccount("Kafi", 2000, 5), CurrentAccount("John", 3000)]

for account in accounts:
   print(account.withdraw(500))
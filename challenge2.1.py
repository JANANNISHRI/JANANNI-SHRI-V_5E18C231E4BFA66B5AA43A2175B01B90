class BankAccount:
  def __init__(self, account_number, account_holder_name, account_balance):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = account_balance

  def deposit(self, amount):
      self.__account_balance += amount

  def withdraw(self, amount):
      if amount > self.__account_balance:
          print("Insufficient balance")
      else:
          self.__account_balance -= amount

  def display_balance(self):
      print("Account Balance: ", self.__account_balance)

# create a BankAccount object
my_account = BankAccount("123456789", "John Doe", 1000)

# deposit some money
my_account.deposit(500)

# withdraw some money
my_account.withdraw(200)

# display the current balance
my_account.display_balance()

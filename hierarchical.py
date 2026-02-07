class BankAccount:
  def __init__(self,account_holder):
    self.account_holder=account_holder
    self.balance=0
  def deposit(self,amount):
    self.balance+=amount
    

  def withdraw(self,amount):
    if self.balance>=amount:
      self.balance-=amount
      self.display_balance()
    else:
      print("Insufficient balance.")

  def display_balance(self):
    print("Current Balance:",self.balance)


class SavingsAccount(BankAccount):
  def __init__(self, interest_rate,name):
    temp_interest=interest_rate/100
    self.interest_rate=temp_interest
    super().__init__(name)
  def add_interest(self):
    self.balance=self.balance*(1+self.interest_rate)
    super().display_balance()


class CurrentAccount(BankAccount):
  def __init__(self,overdraft_limit,name):
    self.overdraft_limit=overdraft_limit
    super().__init__(name)
  def withdraw_with_overdraft(self,amount):
    if amount<self.balance+self.overdraft_limit:
      self.balance -= amount
      super().display_balance()
    else:
      print("Overdraft limit exceeded")

# savings = SavingsAccount(10000, "Rakshita")
# savings.deposit(100)
# savings.withdraw(30)
# savings.display_balance()

curr = CurrentAccount(5000,"Savita")
curr.deposit(500)
curr.withdraw_with_overdraft(590)

from datetime import date, timedelta
class BankAccount():
    def __init__(self, birthdate=date.today(), balance=0, salary=0):
        # private
        self.__balance = balance
        self.__birthdate = birthdate
        self.__salary = salary
        # protected
        self._history = []
        # public
        self.registered_date = date.today()

        self._history.append("Initialized account on %s with $%d" % (str(self.registered_date), self.__balance))

    # public method to access private attribute
    def salary(self):
        return self.__salary

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._history.append("Deposited %d" % amount)
        else: 
            print("Invalid amount")
        pass

    def withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount
            self._history.append("Withdrawn %d" % amount)
        else: 
            print("Invalid amount")
    
    def monthly_payment(self):
        self.deposit(self.__salary)

    def __get_age(self):
        return (date.today() - self.__birthdate)
    
    def _get_balance(self):
        print("Balance:", self.__balance)
    
    def get_history(self, slice=10):
        self._get_balance()
        
        print('-' * 10)
        print("Last %d items:" % slice)
        for item in self._history[-slice:]:
            print(item)
        print('-' * 10)

    def elderly_check(self):
        return (self.__get_age() >= timedelta(days = 65*365))

class HSBCAccount(BankAccount):
    def __init__(self, birthdate, balance, salary):
        super().__init__(birthdate, balance, salary)
        self.bank_name = "HSBC"

    # functions are set in parent BankAccount class
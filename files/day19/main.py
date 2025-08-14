from BankAccount import HSBCAccount

from datetime import date


try:
    
    account = HSBCAccount(birthdate=date(1900,1,1), balance=0, salary=20000)
    if account.elderly_check():
        print("Have you applied for $2 elderly transportation scheme?")
    # print(account.bank_name)
    for i in range(1, 12+1):
        account.monthly_payment()
        account.withdraw(6000)
        account.withdraw(2100)
        account.deposit(1000)
    """
        This caused exception AttributeError.
        Private attributes cannot be accessed publicly.
        Thus, to the current system, __balance does not exist
    """
    # print(account.__balance) 
    """
        This will not trigger exception.
        However this method is not recommended as protected attributes and methods should be kept within the class
    """
    # account._get_balance()
except Exception as e:
    print (f"Exception in action: {e}")
finally:
    account.get_history(5)
    exit(0)
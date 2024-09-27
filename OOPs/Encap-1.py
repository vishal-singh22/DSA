# Write a class BankAccount with private attributes account_number and balance. 
# Implement methods to deposit, withdraw, and display the balance, 
# ensuring that the balance cannot be accessed or modified directly

class BankAccount:
    def __init__(self,acc_No,bal = 0):
        self.__acc_NO = acc_No
        self.__bal = bal
        
    def deposit(self,amount):
        if amount > 0:    
            self.__bal += amount
            print(f"\nyour have credit {amount} total balance will {self.__bal}")
        else:
            print("\nenter the amount in postive value")
            
    def withdraw(self,amt):
        if amt > 0:
            if self.__bal >= amt:
                self.__bal -= amt
                print(f"\nyour account is debited {amt} your remainig balance in {self.__bal}")
            else:
                print("\nyour account have insufficent balance")
                
    def display(self):
        print(f"\nAccount number {self.__acc_NO} your remaining balance is {self.__bal}")
    
    
if __name__ == "__main__":
    
    pers = BankAccount(123456,570)
    
    pers.display()
    
    pers.deposit(500)
    
    pers.display()
    
    pers.withdraw(4500)
    
    pers.deposit(5000)
    
    pers.withdraw(4500)
    
    pers.display()
        
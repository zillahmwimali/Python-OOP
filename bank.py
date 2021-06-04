class Account:
    def __init__(self,name,phone,loan_limit):
    #     self.name=name
    #     self.number=number
    #     self.amount=amount
    # def send_money(self):
    #     return f"Hello {self.name}.Transaction successful,you have sent {self.amount} to Diana Jarenga."
    # def account_number(self):
    #     return f"Your account number is {self.number}"
        self.name=name
        self.phone=phone
        self.balance=0
        self.loan=0
        self.loan_limit=loan_limit
    def deposit(self,amount):
        if amount<=0:
            return f"The amount must be greater than 0"
        else:
            self.balance+=amount
            return f"Dear {self.name},you have deposited {amount} your new balance is {self.balance}"
    def show_balance(self):
        return self.balance
    def withdraw(self,amount2):
        if amount2<=0:
            return f"You can not withdraw!"
        elif amount2>self.balance:
            return f"Your account balance is insufficient to withdraw {amount2}"
        else:
            self.balance-=amount2
            return f"Withdarwal of {amount2} is successful.Your balance is {self.balance}"
    def borrow(self,amount3):
        if self.loan>0:
            return f"You have an existing loan"
        else :
            amount3<=self.loan_limit
            self.balance+=amount3 #balance after borrowing
            self.loan+=amount3 #current loan balance 
            return f"Loan request is successful.Your balance is {self.balance} and your loan balance is {self.loan}"



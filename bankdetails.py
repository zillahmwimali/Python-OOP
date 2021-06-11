from datetime import datetime, time
class Account:
    def __init__(self,name,phone,loan,loan_limit):
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
        self.loan=loan
        self.loan_limit=loan_limit
        self.transactions=[]
    def deposit(self,amount):
        try:
            1+amount
        except TypeError:
            return f"The amount must be in figures"
        if amount<=0:
            return f"The amount must be greater than 0"
        else:
            self.balance+=amount
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
            self.transactions.append(transaction)
            return f"Dear {self.name},you have deposited {amount} your new balance is {self.balance}"
    def show_balance(self):
        return self.balance
    def withdraw(self,amount2):
        try:
            1+amount2
        except TypeError:
            return f"The amount must be in figures"
        if amount2<=0:
            return f"You can not withdraw!"
        elif amount2>self.balance:
            return f"Your account balance is insufficient to withdraw {amount2}"
        else:
            self.balance-=amount2
            transaction={"amount":amount2,"balance":self.balance,"time":datetime.now(),"narration":"Withdraw"}
            self.transactions.append(transaction)
            return f"Withdrawal of {amount2} is successful.Your balance is {self.balance}"
    def borrow(self,amount3):
        try:
            1+amount3
        except TypeError:
            return f"The amount must be in figures"
        if self.loan>0:
            return f"You have an existing loan"
        else :
            amount3<=self.loan_limit
            self.balance+=amount3 #balance after borrowing
            self.loan+=amount3 #current loan balance 
            transaction={"amount":amount3,"balance":self.balance,"time":datetime.now(),"narration":"Loan"}
            self.transactions.append(transaction)
            return f"Loan request is successful.Your balance is {self.balance} and your loan balance is {self.loan}"
    def get_statement(self):
        for transaction in self.transactions:
            narration=transaction["narration"]
            amount=transaction["amount"]
            balance=transaction["balance"]
            time=transaction["time"].strftime("%D")
            print(f"{time},{narration} {amount} and your balance is{balance}")
    def repay_loan(self,amount):
        try:
            1+amount
        except TypeError:
            return "The amount must be in figures"
        if amount<0:
            return "Transaction failed!"
        elif amount<self.loan:
            self.loan-=amount
            return f"{amount} has been used to partially repay your loan.Existing loan balance is {self.loan} "
        else:
            self.loan=0
            extra=amount-self.loan
            self.balance+=extra
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Payments"}
            self.transactions.append(transaction)
            return f"Your loan has been fully paid.Your existing loan balance is {self.loan}Your account balance is {self.balance}"
    
    def transfer(self,amount,account):
        fee=amount*0.05
        try:
            1+amount
        except TypeError:
            return f"The amount should be in figures"
        if amount<0:
            return f"Transaction failed"
        elif amount+fee>self.balance:
            return f"You have insufficient balance. Your account  balance is {self.balance},you need {amount+fee} to make successful transaction"
        else:
            self.balance-=amount+fee
            account.deposit(amount)
            return f"Transaction successful!You have transferred {amount} to {account} at a fee of {fee}.Your account balance is {self.balance}"

class MobileMoneyAccount(Account):
    def __init__(self,name,phone,loan,loan_limit,service_provider):
        Account.__init__(self,name,phone,loan,loan_limit)
        self.service_provider=service_provider
        self.limit=300000      

    def buy_airtime(self,amount):
        try:
            1+amount
        except TypeError:
            return "The amount must be in figures"
        if amount<0:
            return f"Sorry,you can not buy"

        elif amount>self.balance:
            return f"You have insufficient balance to buy airtime "
        else:
            self.balance-=amount
            return f"Request successful,you have bought airtime worth {amount} and your balance is {self.balance}"
class Account:
    def __init__(self,name,number,amount):
        self.name=name
        self.number=number
        self.amount=amount
    def send_money(self):
        return f"Hello {self.name}.Transaction successful,you have sent {self.amount} to Diana Jarenga."
    def account_number(self):
        return f"Your account number is {self.number}"
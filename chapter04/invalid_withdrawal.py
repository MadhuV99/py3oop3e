# invalid_withdrawal.py

class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"account doesn't have ${amount}")
        self.amount = amount
        self.balance = balance
    def overage(self):
        return self.amount - self.balance

def main():
    try:
        raise InvalidWithdrawal(balance=25, amount=75)
    except InvalidWithdrawal as e:
        print("I'm sorry, but your withdrawal is "
              "more than your balance by "
              f"${e.overage()}")

if __name__ == '__main__':
    main() 


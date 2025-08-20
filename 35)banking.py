class account:
    def __init__(self, id , holdername):
        self.id = id
        self.holfername = holdername
        self._balance = 0 # encapsulation    

    def checkbalance(self):
        print(f"balance : {self._balance}")

    def deposit(self , amount):
        self._balance += amount
        print(f"deposit successful. updated balance: {self._balance}")    

    def withdrawl (self , amount):
        if self._balance >= amount:
            self._balance -= amount
            print(' ')
        else:
            print("balance is less than ask")



# class savingaccount(account):
    

# class currentaccount(account):
#     pass

# class bank:
#     pass
#encapsulation- (capsule,shield,protecting the data) that restrict access to certain program of an object.
#we use 
class Bankaccount:
    def __init__(self,accountno,balance):
        self._accountno=accountno    #protected member account
        self._balance=balance        #private member
    def get_balance(self):            #this is for encapsulation:
        return self._balance
account1=Bankaccount("1234",1000)
print(account1._accountno)     # accessing a protected member account
print(account1.get_balance())  #accessing a private member balance using a method
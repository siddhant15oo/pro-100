class Atm:
    def __init__(self,cardnumber,pinumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinumber

    def CashWithdrawl(self,amt ):

        newamount=5000-amt
        print(newamount)


    def Balanceinquiry(self):
        print('your balance is:5000$')

    
def main():
    cardno=int(input('Write your cardnumber here:'))
    pinno=int(input('write your pinnumber here:'))
    user1=Atm(cardno,pinno)
    print('if you want bank inquiry then type 1')
    print('if you want to withdraw cash type 2')
    q=int(input('what do you want to do:'))
    if (q==1):
        user1.Balanceinquiry()
    elif(q==2):
        money=int(input('how much money do you require max amt(5000):'))
        user1.CashWithdrawl(money)


if __name__=='__main__':
    main()
    

    

from ast import Pass
from datetime import datetime
attempts=0
class bankAccount:
    def __init__(self,username,password,initialAmount):
        self.username=username
        self.password=password
        self.Balance=initialAmount
        self.filename=self.username + ".txt"
        
        f=open(self.filename,"a")
        f.write(f"Hey {self.username} Welcome to your transaction history")
        f.close()
    
    def authenticate(self,passw):
        if passw==self.password:
            return True
        else:
            return "Password not correct"
    def deposit(self,password,Amount):
        try:
            assert password==self.password
        except AssertionError:
            global attempts
            attempts+=1
            if(attempts>2):
                return "Attempts exceeded"
            else:
                return "please try again"
        self.Balance+=Amount
        with open(self.filename,"a") as user:
            user.write(str(datetime.now())+f"the amount of rupees {Amount} is deposited   "+f"Current Balance is {self.Balance}\n")
        return "success"
    def withdrawl(self,password,Amount):
        try:
            assert password==self.password
        except AssertionError:
            global attempts
            attempts+=1
            if(attempts>2):
                return "Attempts exceeded"
            else:
                return "please try again"
        self.Balance-=Amount
        with open(self.filename,"a") as user:
            user.write(str(datetime.now())+f"the amount of rupees {Amount} is deposited   "+f"Current Balance is {self.Balance}\n")
        return "success"
    def bankStatement(self,password):
        try:
            assert password==self.password
        except AssertionError:
            global attempts
            attempts+=1
            if(attempts>2):
                return "Attempts exceeded"
            else:
                return "please try again"
        with open(self.filename,"r") as user:
            data=user.read()
            print(data)
            return "success"
print("                               ---------Wecome to bank of IIITD---------")
Username=input("Please enter your name : ")
Password=input("Please enter your password : ")
initialAmount=int(input("Your initial amount : "))
account=bankAccount(Username,Password,initialAmount)
choice="y"
while(choice=="y"):
    print("1. Deposit\n2. Withdrawl\n3. Transaction history 4. Exit")
    x=int(input("Please select the option : "))
    
    if(x==1):
        passw=input("Please enter your password : ")
        amount=int(input("enter amount to be deposited : "))
        x=account.deposit(passw,amount)
        while(x!="Attempts exceeded" and x!="success"):
            if(x=="success"):
                print("deposited successfully")
            elif(x=="please try again"):
                print(x)
                passw=input("Please enter your password : ")
                x=account.deposit(passw,amount)
            else:
                print(x)
            
        


    elif(x==2):
        passw=input("Please enter your password : ")
        amount=int(input("enter amount to be withdrawl : "))
        x=account.withdrawl(passw,amount)
        while(x!="Attempts exceeded" and x!="success"):
            if(x=="success"):
                print("deposited successfully")
            elif(x=="please try again"):
                print(x)
                passw=input("Please enter your password : ")
                x=account.withdrawl(passw,amount)
            else:
                print(x)
            
        
    elif(x==3):
        passw=input("Please enter your password : ")
        x=account.bankStatement(passw)
        while(x!="Attempts exceeded" and x!="success"):
            if(x=="success"):
                print("deposited successfully")
            elif(x=="please try again"):
                print(x)
                passw=input("Please enter your password : ")
                x=account.bankStatement(passw)
            else:
                print(x)

    else:
        choice="n"
print("Thankyou for using our bank ")
    










            
        

        

totalCustomers=0

class LaundryService:
    price={"cotton":50,"silk": 30,"woolen":90,"polyester":20}
    
    def __init__(self,customerName,customerContact,customerEmail,clothType,Branded,Season):
        global totalCustomers
        totalCustomers+=1
        self.id=totalCustomers
        self.customerName=customerName
        self.customerContact=customerContact
        self.customerEmail=customerEmail
        self.clothType=clothType
        self.Branded=bool(Branded)
        self.Season=Season
        
    def customerDetails(self):
        print("Customer Details are : ")
        print(f"1. ID : {self.id}")
        print(f"2. Name of Customer : {self.customerName}")
        print(f"3. Contact of customer : {self.customerContact}")
        print(f"4. Email of customer : {self.customerEmail}")
        print(f"5. Type of Cloth : {self.clothType}")
        print(f"6. Is branded  :  {self.Branded}")
    

    def calculateCharge(self):
        Normalcharge=self.price[self.clothType]
        charge=Normalcharge
        if(self.Branded==True):
            charge=1.5*(Normalcharge)
        if(self.Season=="Winter" or self.Season=="winter"):
            charge=0.5*(charge)
        else:
            charge=2*charge
        return charge
        
    def finalDetails(self):
        charge=self.calculateCharge()
        print("Your total charge is : " ,charge)
        if(charge>200):
            print("To be returned in 4 days ")
        else:
            print("To be returned in 7 days")
        print("Thankyou for using our services")

n=int(input("Please enter the no. of customers "))
for i in range(0,n):
    customerName=input("Please Enter your Name : ")
    customerContact=int(input("Please enter your mobile number :"))
    customerEmail=input("Please Enter your Email : ")
    clothType=input("Please Enter the cloth Type : ").lower()
    Branded=int(input("Is your cloth branded ?(0/1) : "))
    Season=input("Please Enter the season : ")
    customer=LaundryService(customerName,customerContact,customerEmail,clothType,Branded,Season)
    customer.customerDetails()
    customer.finalDetails()



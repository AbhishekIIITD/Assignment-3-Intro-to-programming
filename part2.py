class laundary:
    id=0
    def __init__(self,nc,cc,email,type,brand,season):
        self.nameofcustomers=nc
        self.contactofcustomers=cc
        self.email=email
        self.type=type
        self.brand=brand
        self.season=season
        laundary.id+=1
    def customerdetails(self):
        print("1.Customer id is ",self.id,"2. Customer name is ",self.nameofcustomers,"\n3. Customer contact is ",self.contactofcustomers,"\n4. Customer email : ",self.email,"\n5. Cloth type is ",self.type,"\n6. Is branded ",self.brand)
    def calculateCharge(self):
        charge=0
        if(self.type.lower()=='cotton'):
            charge=50
        elif(self.type.lower()=='silk'):
            charge=30
        elif(self.type.lower()=='woolen'):
            charge=90
        elif(self.type.lower()=='polyester'):
            charge=20
        if(self.brand==True):
            charge*=1.5

        if(self.season.lower()=='winter'):
            charge/=2
        else:
            charge*=2
        return charge
    def finaldetails(self):
        self.customerdetails()
        charge=self.calculateCharge()
        print("Total charge is ",charge)
        if(charge>200):
            print( "To be returned in 4 days ")
        else:
            print("To be returned in 7 days ") 

        
n=int(input("Enter the number of customers : "))
for i in range(0,n):
    name=input("Enter the name of customer : ")
    contact=int(input("Enter the contact no. of customer "))
    email=input("Enter the email of customer : ")
    type=input("Enter the type of cloth : ")
    branded=bool(input("Enter 1 if branded or 0 : "))
    season=input("Enter the season : ")

    obj=laundary(name,contact,email,type,branded,season)
    obj.finaldetails()


def sortbyattri(listofattri,listofperson):
    for i in range(0,len(listofattri)):
        for j in range(len(listofattri)-i-1):
            if(listofattri[i]>listofattri[i+1]):
                listofattri[i],listofattri[i+1]=listofattri[i+1],listofattri[i]
                listofperson[i],listofperson[i+1]=listofperson[i+1],listofperson[i]
    return listofperson

            

class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    def objectinfo(self):
        print(f"{self.firstname} {self.lastname} and {self.age}")



listofperson=[]
n=int(input("Enter the number of persons : "))
for i in range(0,n):
    firstname=input(f"Enter the firstname of {i+1} person : ")
    lastname=input(f"Enter the lastname of {i+1} person : ")
    age=int(input(f"Enter the age of {i+1} person : "))
    s=Person(firstname,lastname,age)
    listofperson.append(s)
query=int(input("Please enter number of queries : "))
for i in range(0,query):
    x=input("Enter the query : ")
    if(x=='firstname'):
        listofattri=[]
        for i in range(0,len(listofperson)):
            listofattri.append(listofperson[i].firstname)
        listofperson=sortbyattri(listofattri,listofperson)

    elif(x=='lastname'):
        listofattri=[]
        for i in range(0,len(listofperson)):
            listofattri.append(listofperson[i].lastname)
        listofperson=sortbyattri(listofattri,listofperson)
    elif(x=='age'):
        listofattri=[]
        for i in range(0,len(listofperson)):
            listofattri.append(listofperson[i].age)
        listofperson=sortbyattri(listofattri,listofperson)
    print("Order :")
    for i in listofperson:
        i.objectinfo()

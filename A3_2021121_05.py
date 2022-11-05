from sre_constants import BRANCH
from turtle import position


class company:
    def __init__(self,name,requiredcgpa,branches,positionOpen):
        self.name=name
        self.requiredcgpa=requiredcgpa
        self.branches=branches
        self.positionOpen=positionOpen
        self.appliedStudents=[]
        self.hired=[]
  
    def hireStudents(self):
        n=len(self.appliedStudents)
        self.appliedStudents.sort(key=lambda x:x.cgpa,reverse=True)
        if(n>self.positionOpen):
            n=n-self.positionOpen+1
              
        
        for i in range(0,n):
            self.appliedStudents[i].getsPlaced()
            self.hired.append(self.appliedStudents[i])
        self.closeApplication()
        
    def closeApplication(self):
        self.positionOpen=0
        print(self.name," has hired ",len(self.hired)," student given below : ")
        for i in self.hired:
            print(i.name)

        


class student:
    def __init__(self,name,cgpa,branch):
        self.name=name
        self.cgpa=cgpa
        self.branch=branch
        self.isPlaced=False

    def isEligible(self,company):
        if(self.cgpa>=company.requiredcgpa and (self.branch in company.branches) and not self.isPlaced):
            print(f"{self.name} is eligible for {company.name}")
            return True
        else:
            print(f"{self.name} is not eligible for {company.name}")
            return False
    def apply(self,company):
        company.appliedStudents.append(self)
    def getsPlaced(self):
        self.isPlaced=True
students=int(input("Enter the no. of students : "))
studentlist=[]
companieslist=[]
for i in range(0,students):
    name=input(f"Enter the name of student {i+1} : ")
    cgpa=float(input(f"Enter the cgpa of student {i+1} : "))
    assert (cgpa>=0 and cgpa<=10),"The cgpa is invalid , Kindly provide correct cgpa"
    branch=input(f"Enter the branch of student {i+1} : ")
    obj=student(name,cgpa,branch)
    studentlist.append(obj)
companies=int(input("Enter the number of companies : "))

for i in range(0,companies):
    name=input(f"Enter the name of company {i+1} : ")
    cgpa=float(input(f"Enter the required cgpa of company {i+1} : "))
    assert (cgpa>=0 and cgpa<=10),"Please enter right cgpa"
    branch=[i for i in input(f"Enter the branches allowed by comany {i+1} : ").split()]
    position=int(input("Enter the number of positions open : "))
    obj=company(name,cgpa,branch,position)
    companieslist.append(obj)
for i in companieslist:
    for j in studentlist:
        if(j.isEligible(i)):
            j.apply(i)
    i.hireStudents()



    


    

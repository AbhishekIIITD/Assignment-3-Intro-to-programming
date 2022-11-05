import math

from A2_2021121_2 import transformation

def test_matmul(a,b,true_x):
    matrix=transformation.matrixmul(b,a)
    assert matrix==true_x,"Test case failed"
    return matrix

def test_scale(x,y,z,sx,sy,sz,true_x,true_y,true_z):
        true_matrix=[true_x,true_y,true_z]
        normalmat=[x,y,z]
        matrix=transformation.Scaling(sx,sy,sz,normalmat)
        assert matrix==true_matrix,"Test case failed"
        return matrix


def test_translate(x,y,z,tx,ty,tz,true_x,true_y,true_Z):
        true_matrix=[true_x,true_y,true_Z]
        normalmat=[x,y,z]
        matrix=transformation.tranlating(tx,ty,tz,normalmat)
        assert matrix==true_matrix,"Test case failed"
        return matrix

def test_rotation(x,y,z,axis,angle,true_x,ture_y,true_z):
        true_matrix=[true_x,ture_y,true_z]
        normalmat=[x,y,z]
        matrix=transformation.rotation(angle,axis,normalmat)
        assert matrix==true_matrix,"Test case failed"
        return matrix


vertices=int(input("Enter the no. of vertices : "))

x=[float(i) for i in input().split()]
y=[float(i) for i in input().split()]
z=[float(i) for i in input().split()]
t=[1 for i in range(0,vertices)]

query=int(input("Enter the number of query : "))
for i in range(0,query):
    print("What you want to check :\n1. Matrix multiplication \n2. Scaling \n3. Translation \n4.Rotation ")
    q=int(input("Choose a option : "))
    if(q==1):
        print("enter the vertices of second matrix : ")
        row1=[float(i) for i in input().split()]
        row2=[float(i) for i in input().split()]
        row3=[float(i) for i in input().split()]

        a=[x,y,z]
        b=[row1,row2,row3]
        print("Please provide the true values of output : ")
        true_x=[float(i) for i in input("Enter the values for row1 : ").split()]
        true_y=[float(i) for i in input("Enter the values for row2 : ").split()]
        true_z=[float(i) for i in input("Enter the values for row3 : ").split()]
        true_matrix=[true_x,true_y,true_z]
        print(test_matmul(a,b,true_matrix))



        




    elif(q==2):
        sx,sy,sz=map(input("Please provide the values to which it should scale in each axis(space separated) : ").split())
        print("Please provide the true values of output : ")
        true_x=[float(i) for i in input("Enter the values for row2 : ").split()]
        true_y=[float(i) for i in input("Enter the values for row3 : ").split()]
        true_z=[float(i) for i in input("Enter the values for row4 : ").split()]
        print(test_scale(x,y,z,sx,sy,sz,true_x,true_y,true_z))


    elif(q==3):
        tx,ty,tz=map(int,input("Please provide the values to which it should translate in each axis(space separated) : ").split())

        print("Please provide the true values of output : ")
        true_x=[float(i) for i in input("Enter the values for row2 : ").split()]
        true_y=[float(i) for i in input("Enter the values for row3 : ").split()]
        true_z=[float(i) for i in input("Enter the values for row4 : ").split()]
        print(test_translate(x,y,z,tx,ty,tz,true_x,true_y,true_z))
    elif(q==4):
        axis=input("Enter the rotation axis : ")
        angle=float(input("Enter the angle to which you want to rotate it : "))
        print("Please provide the true values of output : ")
        true_x=[float(i) for i in input("Enter the values for row2 : ").split()]
        true_y=[float(i) for i in input("Enter the values for row3 : ").split()]
        true_z=[float(i) for i in input("Enter the values for row4 : ").split()]
        print(test_rotation(x,y,z,axis,angle,true_x,true_y,true_z))
    else:
        print("wrong input !")









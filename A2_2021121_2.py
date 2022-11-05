import math 
class transformation:
    
    def matrixmul(b,a):
        res=[]
        for i in range(0,len(a)):
            list=[]
            for j in range(len(b[i])):
                row=0
                col=0
                sum=0
                while(row<len(a)):
                    sum=sum+a[i][col]*b[row][j]
                    row+=1
                    col+=1
                list.append(sum)
            res.append(list)
        return res
                    
    def Scaling(self,sx,sy,sz,x):
        scalingmatrix=[[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
        return self.matrixmul(x,scalingmatrix)

    def tranlating(self,tx,ty,tz,x):
        transmatrix=[[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
        return self.matrixmul(x,transmatrix)

    def rotation(self,angle,dir,matrix):
        radian=(math.pi*angle)/180
        sin=math.sin(radian)
        cos=math.cos(radian)
        #none
        if(dir=="x"):
            rotationmatrix=[[1,0,0,0],[0,cos,-sin,0],[0,sin,cos,0],[0,0,0,1]]
        elif(dir=="y"):
            rotationmatrix=[[cos,0,sin,0],[0,1,0,0],[-sin,0,cos,0],[0,0,0,1]]
        elif(dir=="z"):
            rotationmatrix=[[cos,-sin,0,0],[sin,cos,0,0],[0,0,1,0],[0,0,0,1]]
        else:
            return "wrong direction"
        return self.matrixmul(matrix,rotationmatrix)
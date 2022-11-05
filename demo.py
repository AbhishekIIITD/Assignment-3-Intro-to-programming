def sortbyattri(listofattri,listofperson):
    for i in range(0,len(listofattri)):
        for j in range(len(listofattri)-i-1):
            if(listofattri[i]>listofattri[i+1]):
                listofattri[i],listofattri[i+1]=listofattri[i+1],listofattri[i]
                listofperson[i],listofperson[i+1]=listofperson[i+1],listofperson[i]
    return listofperson
l1=[3,1,5,2,7]
l2=[4,2,1,3,5]
print(sortbyattri(l1,l2)
)
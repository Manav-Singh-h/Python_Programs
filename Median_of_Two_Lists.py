L1=[]
L2=[]
A = int(input("How many elements do you want to enter in a list 1:"))
B = int(input("How many elements do you want to enter in a list 2:"))
for i in range(0,A):
    ele1 = int(input("Enter Element in list 1:"))
    L1.append(ele1)
for i in range(0,B):
    ele = int(input("Enter Element in list 2:"))
    L2.append(ele)

c = L1+L2   
c.sort()
x=len(c)
print(c)
if(x%2==0):
     median =(x//2)
     median1 = (x//2)+1 
     med = ( median+median1)/2
     print(med)
     
else:
    medi = (x+1)//2
    print(c[medi-1])
    

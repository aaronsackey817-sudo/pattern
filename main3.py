rowSize=int(input("enter row seize: "))
if rowSize%2==0:
    halfDiamondrow=int(rowSize/2)
else:
    halfDiamondrow=int(rowSize/2)+1
    space=halfDiamondrow-1
  
for i in range(1,halfDiamondrow+1):
    for j in range(i,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j  in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,halfDiamondrow):
    for j in range(1,space+1):
        print(end=" ")

    space=space+1
    num=1

    for j in range(1,2*(halfDiamondrow-i)):
        print(end=str(num))
        num=num+1
    print()

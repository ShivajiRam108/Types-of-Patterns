num = int(input("Enter a No.of rows: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        if i%2 == 1:
            if j % 2==1:
                print(1, end=" ")
            else:
                print(0,end=" ")
        else:
            if j % 2 ==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
    print()


#  Q - 2
num = int(input("Enter a no.of rows: "))
for i in range(1,num+1):
    print(" " *(2*(num-i)), end="") 
    rev,res="",""
    for j in range(1,i+1):
        res= res+str(j)+" "
        if j > 1:
            rev = str(j)+" "+rev
    print(rev+res)

#  Q - 3
num = int(input("enter a rows: "))
for i in range(1,num+1):
    print(" "*(num-i),end=" ")
    for j in range(1,i+1):
        if i ==num or j == 1 or i == j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
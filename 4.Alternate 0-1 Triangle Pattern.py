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
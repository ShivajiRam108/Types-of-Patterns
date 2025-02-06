#  simple way
num = int(input("Enter rows: "))
for i in range(num , 0, -1):
    print("* " *i)


#  By utilizing two loops (a nested loop structure).
num = int(input("Enter rows: "))
for i in range(num , 0, -1):
    for j in range(i):
        print("* " , end="")
    print()


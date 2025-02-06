#  simple way
num = int(input("Enter rows: "))
for i in range(1, num+1):
    print("* "*i)


#  By utilizing two loops (a nested loop structure).
num = int(input("Enter rows: "))
for i in range(1, num+1):
    for j in range(i):
        print("* " ,end="")
    print()
num = int(input("enter a rows: "))
for i in range(1,num+1):
    print(" "*(num-i),end=" ")
    for j in range(1,i+1):
        if i ==num or j == 1 or i == j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

# (Or)
# This is the ternary operator-optimized version of your pattern! 
num = int(input("Enter rows: "))

for i in range(1, num + 1):
    print(" " * (num - i) + "* " + ("  " * (i - 2) + "*" if 1 < i < num else "* " * (i - 1)))

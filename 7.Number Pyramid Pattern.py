num = int(input("Enter a rows: "))
for i in range(1, num+ 1):
    print(" " * (num - i) + " ".join(str(j) for j in range(1, i + 1)))


# # Simple Pyramid Pattern Using Stars
num = int(input("Enter a rows:  "))
for i in range(1,num+1):
    print(" "*(num-i)+ "* " *i)

#  reversed Pyramid Pattern Using
num = int(input("Enter a rows: "))
for i in range(num, 0, -1):
    print(" "* (num-i)+"* "*i)
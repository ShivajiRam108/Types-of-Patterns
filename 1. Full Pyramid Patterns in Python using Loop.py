num = int(input("Enter  rows: "))
# Upper half of the diamond
for i in range(1, num+1, 2):
    print(" " * ((num - i) // 2) + "*" * i)

# Lower half of the diamond
for i in range(num-2, 0, -2):
    print(" " * ((num - i) // 2) + "*" * i)


'''simple ways '''
num = int(input("Enter rows: "))
print("\num".join([(" " * ((num - i) // 2) + "*" * i) for i in range(1, num+1, 2)] +
                [(" " * ((num - i) // 2) + "*" * i) for i in range(num-2, 0, -2)]))

#  single line code 
num = int(input("Enter No of rows:"))
for i in range(1,2 *num):
    res = (num -i) * " " + "* " * i if i <=num else (i - num) * " " + "* " * (2 *num -i)
    print(res)
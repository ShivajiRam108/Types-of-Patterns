#  basic level of code:
num = int(input("Enter a no.of rows: "))
for i in range(1,num+1):
    print(" " *(2*(num-i)), end="") 
    rev,res="",""
    for j in range(1,i+1):
        res= res+str(j)+" "
        if j > 1:
            rev = str(j)+" "+rev
    print(rev+res)


# Another way to write this code is by using string formatting and a more concise approach:(advanced )
num = int(input("Enter the number of rows: "))
for i in range(1, num + 1):
    print(" " * (2 * (num - i)) + " ".join(map(str, list(range(i, 0, -1)) + list(range(2, i + 1)))))

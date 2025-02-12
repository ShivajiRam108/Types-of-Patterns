# 1. Using String Concatenation
num = int(input("Enter: "))
for i in range(1, num+1):
    print("  " * (num - i), end=" ")  # Fixed spacing here
    res, rev = "", ""
    for j in range(1, i+1):
        res = res + str(j) + " "
        if j > 1:
            rev = str(j) + " " + rev
    print(rev + res)  # Fixed spacing in final output


# 2. Using List and Join Method

num = int(input("Enter: "))
for i in range(1, num+1):
    print("  " * (num - i), end=" ")
    left_part = [str(j) for j in range(1, i+1)]
    right_part = left_part[-2::-1]  # Reverse except the last element
    print(" ".join(left_part + right_part))

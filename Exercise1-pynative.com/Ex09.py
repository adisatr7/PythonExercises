# Question 9: Reverse a given number and return true if
# it is the same as the original number

given_num = input("Original number: ")

print("The original and reversed number is ", end="")
print("the same!") if given_num[0] is given_num[-1] else print("not the same!")

# Question 1: Given a two integer numbers return their product and
# if the product is greater than 1000, then return their sum

num1 = float(input("Input 1: "))
num2 = float(input("Input 2: "))
isSum = num1 * num2 > 1000
print("Result:", num1+num2) if isSum else print("Result:", num1*num2)

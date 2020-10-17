# Question 15: Write a function called exponent(base, exp)
# that returns an int value of base raises to the power of exp

def exponent(base, exp):
    result = 1
    for lap in range(exp):
        result = result * base
    return result


base = int(input("Input base number: "))
exp = int(input("Input an exponent: "))
print("Result:", str(exponent(base, exp)))

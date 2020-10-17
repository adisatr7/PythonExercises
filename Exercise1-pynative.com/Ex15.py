def exponent(base, exp):
    result = 1
    for lap in range(exp):
        result = result * base
    return result


base = int(input("Input base number: "))
exp = int(input("Input an exponent: "))
print("Result:", str(exponent(base, exp)))

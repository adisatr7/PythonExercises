# Sorta given up lol

income = int(input("Taxable income: "))

if income <= 10000:
    final_tax = 0

elif income <= 20000:
    final_tax = (income - 10000) * (10/100)

else:
    final_tax = 10000 * (10/100) + (income - 20000) * (20/100)

# Prints out result
print("Tax: $" + str(final_tax))

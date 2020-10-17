def remove_chars(s, n):
    return s[n:]


string = input("Input a string: ")
num = int(input("How many chars should be removed: "))
isValid = num >= 0 or num <= len(string)

print("Result:", remove_chars(string, num)) if isValid else print("Error!")
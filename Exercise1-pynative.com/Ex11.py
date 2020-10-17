# Question 11: Write a code to extract each digit
# from an integer, in the reverse order

def reverse_string(string):
    new_string = ""
    for i in range(len(string)-1, -1, -1):
        new_string += string[i]
    return new_string


def int_extractor(integer):
    str_int = str(integer)
    for i in reverse_string(str_int):
        print(i, end=" ")


given_int = int(input("Given int: "))
int_extractor(given_int)

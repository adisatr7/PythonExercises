# ======================================================================
#  Problem 3: Caesar Cipher Redux
# ----------------------------------------------------------------------
#  For the third practice problem, you’ll solve the Caesar cipher
#  again, but this time you’ll do it without using .translate()
# ======================================================================

def cipher(input_string, key):

    # List of alphabets
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    # String to store the result for later
    result = str()

    for index in range(len(input_string)):

        # If the currently checked character inside the string is not an alphabet
        if input_string[index].lower() not in alphabets:

            # Just print out as it is
            result += input_string[index]

        # If the currently checked character is indeed an alphabet
        else:

            # Get the index in which the same character as the
            # currently checked character is found in 'alphabets'
            alphabet_index = alphabets.find(input_string[index].lower())

            # To loop the alphabet so that 'z + 1 = a'
            while alphabet_index + key >= len(alphabets):
                alphabet_index -= len(alphabets)

            # If the character is in lower case
            if input_string[index].islower():
                result += alphabets[alphabet_index + key]

            # If the character is in upper case
            else:
                result += alphabets[alphabet_index + key].upper()

    # Prints out the result
    return result


# User is asked to input a plain text
plain_text = input("Input a string: ")

# User is asked to input the shift number
shifter = int(input("Input a shift number: "))

# Prints out the result
print("Result:", cipher(plain_text, shifter))
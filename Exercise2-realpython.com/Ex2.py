# ======================================================================
#  Problem 2: Caesar Cipher
# ----------------------------------------------------------------------
#  A Caesar cipher is a simple substitution cipher in which each letter of the
#  plain text is substituted with a letter found by moving n places down the
#  alphabet. For example, assume the input plain text is the following:
#
#      abcd xyz
#
#  If the shift value, n, is 4, then the encrypted text would be the following:
#
#      efgh bcd
#
#  You are to write a function that accepts two arguments, a plain-text
#  message and a number of letters to shift in the cipher. The function will
#  return an encrypted string with all letters transformed and all
#  punctuation and whitespace remaining unchanged.
#
#  Note: You can assume the plain text is all lowercase ASCII except for
#  whitespace and punctuation.
# ======================================================================

# --Given up--

import string


def caesar(input_string, shift_number):
    letters = string.ascii_lowercase
    mask = letters[shift_number:] + letters[:shift_number]
    translate = str.maketrans(letters, mask)
    return input_string.translate(translate)


plain_text = input("Input a text: ")
shift_num = int(input("Input a shift number: "))
print("Result: " + caesar(plain_text, shift_num))
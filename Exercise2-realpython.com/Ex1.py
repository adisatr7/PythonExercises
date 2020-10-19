# ======================================================================
#  Problem 1: Sum of a Range of Integers
# ----------------------------------------------------------------------
#  Write a function, add_it_up(), that takes a single integer as input
#  and returns the sum of the integers from zero to the input parameter.
#  The function should return 0 if a non-integer is passed in.
# ======================================================================

def add_it_up(n):
    result = 0
    try:
        for i in range(n):
            result += i
        return result
    except ValueError:
        return 0


n = int(input("Input a number: "))
print("Result:", str(add_it_up(n)))

# Question 10: Given a two list of numbers create a new list such
# that new list should contain only odd numbers from the first list
# and even numbers from the second list

def get_odd_elements(checked_list):
    result = []
    for checker in checked_list:
        if checker % 2 != 0:
            result.append(checker)
    return result


def get_even_elements(checked_list):
    result = []
    for checker in checked_list:
        if checker % 2 == 0:
            result.append(checker)
    return result


list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

result_list = get_odd_elements(list1) + get_even_elements(list2)

print("First list:", str(list1))
print("Second list:", str(list2))
print("Result list:", str(result_list))

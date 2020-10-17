# Question 5: Given a list of numbers,
# return True if first and last number of a list is same

def check_list(list):
    return True if list[0] == list[-1] else False


list1 = [10, 20, 30, 40, 10]
list2 = [10, 20, 30, 40, 50]

print(list1)
print("Result is", check_list(list1))
print(list2)
print("Result is", check_list(list2))
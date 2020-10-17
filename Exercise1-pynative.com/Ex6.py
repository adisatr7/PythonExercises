def find_divisible_5(checked_list):
    for checker in checked_list:
        if checker % 5 == 0:
            print(checker)


main_list = [10, 20, 33, 36, 55]
print(main_list)
print("Divisible by 5 in the list")
find_divisible_5(main_list)
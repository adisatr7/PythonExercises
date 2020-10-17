string = input("Original string is ")

print("Printing only even index chars")
for i in range(len(string)):
    if i % 2 == 0:
        print(string[i])
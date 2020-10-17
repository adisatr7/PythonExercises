# Question 2: Given a range of first 10 numbers, Iterate from start number to
# the end number and print the sum of the current number and previous number

prev = 0
for current in range(10):
    print("Current number:", str(current), "Previous number:", str(prev), "Sum:", str(current+prev))
    prev = current

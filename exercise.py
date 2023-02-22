"""
write a program that repeatedly reads numbers until the user enters "done". Once "done" is entered,
print out the total, count, and average of the numbers. If the user enters anything other than a number,
detect their mistake using try and except and print an error message and skip to the next number.
"""

total = 0
count = 0
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = float(num)
    except:
        print("Invalid input")
        continue
    total = total + num
    count = count + 1
print("Total is ", total)
print("Count is ", count)
print("Average is ", total/count)

def find_largest(numbers):
    largest = None
    # convert numbers into absolute values
    for number in numbers:
        if largest is None or number > largest:
            largest = number
    return largest


numbers = [-1, -2, -3, -4]
number1 = [-1, -2, -3, 4]
print(find_largest(numbers))





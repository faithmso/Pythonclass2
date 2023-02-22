def compute_pay(hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    return pay


print(compute_pay(45, 10))

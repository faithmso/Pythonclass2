# for loop

fruits = ['apples', 'bananas', 'oranges', 'pears']
for fruit in fruits:
    if fruit == 'bananas':
        print('No bananas left!')
    else:
        print(f"{fruit} for sale!")

for x in "banana":
    print(x)

for x in range(2,20,3):
    print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(y, x)

count = 0
total = 0
for itevar in [3, 41, 12, 9, 74, 15]:
    total = total + itevar
    count = count + 1
print('Count: ', count)
print('Total: ', total)
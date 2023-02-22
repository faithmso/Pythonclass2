# while loop

while True:
    print('Type your name.')
    name = input()
    if name != 'joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

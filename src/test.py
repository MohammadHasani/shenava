# Type your code here
number = input('enter the number')
number = int(number)
s = number
while s >= 1:
    si = number
    while si >= 1:
        if si != 1:
            print('*', end='')
        else:
            print('*')
        si -= 1
    s -= 1

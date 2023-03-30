a = int(input('Input first element: '))
d = int(input('Input d: '))
number = int(input('Input quantity of elements: '))

for i in range(1, number + 1):
    print(a + (i - 1) * d, end = ' ')
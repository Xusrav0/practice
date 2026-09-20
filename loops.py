''' LOOP operators
(1) for
(2) break/else
(3) while
'''

print('===== for operator =====')
# iterate (takrorlanish) objects => string dict tuple list range map filter
text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)  # [0,5)

for letter in text:
    print(f'the letter: {letter}')

print('-'*10)
for number in numbs:
    print(f'the number: {number}')

print('-'*10)
for x in range_obj:
    print(f'the number: {x}')

print('-'*10)
for key in car_obj:
    print(f'the key: {key} => value: {car_obj.get(key)}')

print('-'*10)       # 5 bu yerda step bo'ladi
for x in range(1, 20, 5):  # 1 6 11 16
    print(f'the x: {x}')

print('===== break/else =====')

for x in range(1, 20, 5):
    print(f'the x: {x}')
    if x > 10:
        print('Reached break')
        break
else:
    print('Executed successfully')

print('===== while =====')

numb = 40
while numb > 0:
    numb -= 10
    print(f'the number equals: {numb}')

print('-'*10)
count = 0
while True:
    count += 1
    x = int(input('Find the number: '))

    if x == 41:
        print(f'You found the number in {count} steps')
        break
    else:
        print('Wrong, please try again')

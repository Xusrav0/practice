''' List
(1) Working with lists
(2) List methods
(3) Lambda function
(4) enumerate, map and filter
'''

print('======= Working with lists =======')
# Java/PHP/NodeJS array => Pythin list

# literal
person = {'name': 'Justin', 'age': 25}  # dictionary
people = ('Andrew', 'John', "Michael")  # tuple
groups = ['MIT', 'FLEXY', "DEVEX", 'MG']
for team in groups:
    print(f'the team: {team}')

# constructor
letters = list("Hello World!")
print(f'the letters: {letters} and size: {len(letters)}')

print('----------')
fruits = ['apple', 'orange', 'lemon', 'kiwi']
a = fruits[0]
b = fruits[0:2]  # [0,2)
c = fruits[::3]  # boshlang'ich qiymatni oladi va 3 qadam sakraydi
d = fruits[::-1]  # teskari qilib beradi

print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)

print('======= List methods =======')
# methods > mutable => append() insert() pop() remove() clear() sort()
# immutable => index() sorted function

letters = ['a', 'b', 'd']

# append
letters.append('c')  # add end
print('the append result:', letters)

# insert
letters.insert(0, 'z')  # oldidan qo'shib beradi
print('the insert result:', letters)

# pop
size = len(letters) - 1
result1 = letters.pop(size)  # pop end
print(f'the pop result: {result1} and letters: {letters}')

result2 = letters.pop(0)  # pop front
print(f'the pop result: {result2} and letters: {letters}')

print('----------')
animals = ['dog', 'cat', 'capybara', 'fish', 'lion']
print('animals', animals)

# remove
animals.remove('lion')
print('animals remove:', animals)

# delete
del animals[2:4]
print('animals delete:', animals)

# index
exist = animals.index('cat')
print('cat exist:', exist)

# clear
animals.clear()
print('clear:', animals)

# exist2 = animals.index('cat')
# print('cat exist2:', exist2)

# index error handling (cat value yuq)
if 'cat' in animals:
    print('index of cat', animals.index('cat'))
else:
    print('cat does not exist')

# sort
print('--------')
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print('sort default:', numbers)

# reverse sort
numbers.sort(reverse=True)
print('sort reverse:', numbers)

# immutable > sorted function
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f'the sorted numbs: {numbs} and new_numbs: {new_numbs}')


print('======= Lambda function =======')
# Lambda is samll anonymous function!
def calculate(x, y): return x * y


result = calculate(3, 5)
print('result:', result)

people = [
    ('Robert', 20),
    ("Steve", 91),
    ('Joseph', 35),
    ("Michael", 30)
]

people.sort()
print('paeople1:', people)

# sort age with lambda

people.sort(key=lambda person: person[1])
print('paeople2:', people)

print('======= enumerate, map and filter =======')
# enumerate for index & value
animals = ['dog', 'cat', 'fish']
for ele in enumerate(animals):
    print('ele', ele)

for (index, value) in enumerate(animals):
    print(f'the index: {index} and value: {value}')

print('--------')

# similar in dictionary
car_obj = dict(brand="Ferrari", year=2025)
result = car_obj.items()  # tuple qilib yoyib beradi
for (key, value) in result:
    print(f'the key: {key} and value: {value}')

print('----------')
# map()
cars = [
    ('Ferrari', 78),
    ('Tayota', 87),
    ('Audi', 116),
    ('BMW', 109),
    ('Pagani', 33)
]

# new_cars = []
# for car in cars:
#     new_cars.append(car[0])
# print(new_cars) // result ['Ferrari', 'Tayota', 'Audi', 'BMW', 'Pagani']


new_cars = []
for car in cars:
    new_cars.append(car[0])
print('new car(1):', new_cars)

result_map = map(lambda car: car[0], cars)
print(f'the result_map: {result_map} and type: {type(result_map)}')
new_cars = list(result_map)
print('new_cars(2):', new_cars)

# filter

result_filter = filter(lambda car: car[1] > 80, cars)
print(f'the result_map: {result_map} and type: {type(result_map)}')
print(list(result_filter))

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
# immutable => index()

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

# immutable sorted
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f'the sorted numbs: {numbs} and new_numbs: {new_numbs}')

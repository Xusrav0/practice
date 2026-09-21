''' Tuples
(1) What is tuple: tuple vs list
(2) Unpacking arguments
(3) zip
'''

print('======= What is tuple: tuple vs list =======')
# JAVA/PHP/NodeJS array = Python list


# literal
numbs = [3, 5, 1, 2]
print(numbs)
car_dic = {'brand': 'Ferrari', 'year': 1995}

# constructor
letters = list('Hello World!')
print(letters)
person_dic = dict(name="Martin", age=35)

fruits = ['apple', 'lemon', "banana", 'kiwi']
print('before list:', fruits)

fruits[2] = 'melon'
print('after list:', fruits)


# Tuple ni ichida turgan listni uzgartirib bumidi

animals = ('dog', "cat", 'fish', "lion")
tuple_obj = ('MIT', 100, True, None)

print(animals[0])
# animals[0] = 'bird'  error beradi chunki tuple qiymatini o'zgartirmaydi

# try avoid these
people = 'Andrew', 'John'
animals1 = 'dog',

print('======= Unpacking arguments =======')

groups = ['MIT', 'FLEXY', 'DEVEX', 'MG']
# (x, y, z, a) = groups
(x, y, *z) = groups
print(f'the x: {x} and y: {y}')
print("z:", z)  # list


# *args > tuple
def calculate(*args):
    print('args:', args)
    total = 1
    for x in args:
        total *= x
    print(f'the type(args) value: {type(args)}')
    print(f'the total value: {total}')
    return total


# CAll
calculate(1, 7, 2, 3)
print('------')
calculate(0, 2, 300)
print('------')

calculate(5, 7)


# **kwargs > dictionary
def introduce(**kwargs):
    print(f'the type(**kwargs) value: {type(kwargs)}')
    print(f'Hi, I am {kwargs['name']} and I am {kwargs['age']} years old')


# call
introduce(name='Justin', age=25)
introduce(name='Shawn', age=30, single=True)


print('======= ZIP =======')


def greeting(*args, **kwargs):
    print('*args:', args)
    print('*kwargs:', kwargs)


# call
#       (    tuple     ) (    dictionary    )
greeting('hi', True, 10, name='John', age=22)

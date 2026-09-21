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

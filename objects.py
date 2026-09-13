''' OBJECTS
(1) What is object
(2) Iterable objects & Range
(3) Dictionary
(4) Error handling system
'''

print('===== What is object =====')
# An object has state and method properties.
# Everything is object in Python!


import array # package/module
import math
from math import ceil, asin


print(type('Hello world!'))
print(type('number'))
print(type(True))
print(type(array))
print(type(math))

# Paradigm (uslubiyat) => OOP and Functional Programming
# OOP 4 Concepts => Abstaction | Encapsulation | Inheritance | Polymorphism
result1 = math.ceil(97.7) # yaxlitlab beradi
print("result1:", result1)
result2 = math.asin(0.3)
print(result2)

result3 = ceil(98.8)
print("result3:", result3)
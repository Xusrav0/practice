''' OPERATORS AND CONDITIONS
(1) Operators
(2) Conditions
(3) Logical Operators
'''

print('===== Operators =====')
# + - > >= < <= == is * /   // % += **

a = 19
b = 5

print(a/b)
result = a // b  # bo'lgandan keyin butun qismini olib beradi
left = a % b  # bo'lgandan keyin qoldiqni olib beradi
print(f'the result: {result} and left {left}')

# a = a + 100
a += 100
print(a)

print('b*b', b**2)  # darajaga ko'paytirish bning kvadrati
print('b*b*b', b**3)

print('=====')
print('='*5)

c = dict(name='Martin', age=35)
d = dict(name='Martin', age=35)
e = c
print('c == d', c == d)  # qiymatni solishtiryapti
print(id(c), id(d), id(e))

# is reference solishtiradi

print('c is d', c is d)
print('c is e', c is e)

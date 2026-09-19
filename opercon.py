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
print('c == d', c == d)  # value solishtiryapti
print(id(c), id(d), id(e))

# is reference solishtiradi

print('c is d', c is d)
print('c is e', c is e)


print('===== Conditions =====')

x = 15

if x > 50:
    print("case 1")
elif x > 10:
    print('case B')
else:
    print('case C')


print('===== Logical operators =====')

age = 20
# person = None
# if age > 18:
#     person = 'adult'
# else:
#     person = 'child'
# print('person:', person)

# Ternary operator

person = 'adult' if age > 18 else 'minor'
print('person:', person)

# not and or
is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:  # not bo'lmasa
    print('Welcome here, do you want to be a student')
elif is_admin:
    print('Please go to this office')
# elif is_guest and is_parent:
elif is_parent or is_guest:  # or bitta True bo'lsa hammasi True boladi, and bitta False bo'lsa false bo'ladi
    print('Waiting room is over there!')
else:
    print('ETC')

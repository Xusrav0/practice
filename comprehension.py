''' Comprehension
(1) What is comprehension?
(2) set and dictionary comprehension
'''

print("===== What is comprehension? =====")

# Comprehension acts like spread operator.

'''Comprehension
  a) *iteranble
  b) <expression> for item in iterable
  c) <expression> for item in iterable <condition>
'''

# list comprehension
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version
print(" list_numbers:", list_numbers)
print(numbers is list_numbers)  # False
print(id(numbers), id(list_numbers))

print('------------------')
people = [('Robert', 20), ('Steve', 19), ('Joseph', 25)]
list_people = [person[1] for person in people]  # b version
print("list_people:", list_people)

cars = [
    ('Ferrari', 78),
    ('Tayota', 87),
    ('Audi', 116),
    ('BMW', 109),
    ('Pagani', 33)
]

list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)

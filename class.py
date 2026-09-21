''' CLASS
(1) What is Class
(2) ordinary vs static properties
(3) special methods
'''

import datetime
print("===== What is Class =====")
# class - blueprint for object creation!
# structure > state constructor method


class Person():
    # state
    message = "class state property"
    # constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do? ")

    def say_age(self):
        print(f"{self.name} says he/she is {self.age}")

    @classmethod
    def explain(cls):
        print('Static method property executed!')


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 28)

# ordinary state property
name = person1.name
print("person1.name", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print("===== ordinary vs static properties =====")
# statis state (class bilan keladigan state)
new_message = Person.message
print('new_message:', new_message)

# static method
Person.explain()

print("===== special methods =====")
# Python's most common special methods
# __init__ __new__ __str__ __call__ __getitem__ __len__ ...


class Car():
    # state
    description = 'This class makes cars'

    # constructor
    def __new__(cls, *args):
        print('*__new__*')
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"the {self.name} started the engine")

    def stop_engine(self):
        print(f"the {self.name} stopped the engine")

    def __str__(self):

        # print(your_car)
        return f'the Car name: {self.name} was produced in {self.year}'

    def __call__(self):
        print("Object called as function")
        return True


my_car = Car('Ferrari', 2025)
my_car.start_engine()
my_car.stop_engine()

print('-----')
your_car = Car('Tayota', 2026)
print(your_car)
your_car()  # Call # look like function
response = your_car()
print('response:', response)

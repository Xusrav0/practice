''' CLASS
(1) What is Class
(2) ordinary vs static properties
(3) special methods
'''

print("===== What is Class =====")
# class - blueprint for object creation!
# structure > state constructor method

class Person():
    #state
    message = "class state property"
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #method
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
print('new_message:',new_message)

# static method
Person.explain()
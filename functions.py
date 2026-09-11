''' FUNCTIONS
(1) DEFINE AND CALL
(2) Parametr and Argument
(3) Keyword and default arguments
(4) Scope
'''

print("===== DEFINE (paramentr) vs CALL (argument) =====")
# build in function > print() type()
# Function - reusable block of code
# Instead of block {} in Java, JS, Python uses indentation!


# Define - paramentr
def greet(a):
    pass  # hech narsa qilmasdan functiondan o'tib ketadi


def greet(a):
    print(f"How do you do?, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute (argument)
greet("Martin")
result1 = greet("Martin")
print("result1:", result1)  # Void function None qaytaradi

result2 = greeting("Justin")
print("result2:", result2)  # return


print("===== Keyword and default arguments =====")
# Define


def give_great(name, age=22):  # default argument
    print("give_great is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL

# Keyword argument (buning maqsadi o'qilishini osonlashtirish uchun)
result3 = give_great(name="Justin", age=28)
print('result3:', result3)

result4 = give_great("John")
print('result4:', result4)

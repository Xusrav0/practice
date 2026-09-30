''' Packages and Debugging
(1) Python packages & Core Packages
(2) Package Manager & External Package
(3) Debugging
'''

import turtle
print("===== Python packages & Core Packages =====")
''' Python Packages/Modules: Core, File and External Packages'''
# Core Packages: https://docs.python.org/3/library

#  Core package
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(150)

# turtle.done()

print('------------------')
# open file and read content
my_file = open("message.txt", "r")
try:
    content = my_file.read()
    print(" content:", content)
finally:
    my_file.close()

# with - Context Manager
with open("message.txt", "r") as your_file:
    your_content = your_file.read()
    print(" content:", your_content)
print('Done')

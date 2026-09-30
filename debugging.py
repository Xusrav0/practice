''' Packages and Debugging
(1) Python packages & Core Packages
(2) Package Manager & External Package
(3) Debugging
'''

from PIL import Image
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
my_file = open("materials/message.txt", "r")
try:
    content = my_file.read()
    print(" content:", content)
finally:
    my_file.close()

# with - Context Manager
with open("materials/message.txt", "r") as your_file:
    your_content = your_file.read()
    print(" content:", your_content)
print('Done')

print("===== Package Manager & External Package =====")
'''Package Managers
 Python > pip pipenv
 Node > npm yarn
 PHP > composer
 Mac > brew
 '''
# External Package: https://pypi.org/

with Image.open("materials/FSD.jpg") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("materials/sample.png")



# class Student:

#     def __init__(self, name, age, gpa):
#         self.__name = name
#         self.__age = age
#         self.__gpa = gpa

#     def get_info(self):
#         print(f"Name:{self.__name}\n"
#               f"Age:{self.__age}\n"
#               f"Gpa:{self.__gpa}")

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, value):
#         if value == "":
#             print("Name cannot be empty")
#             return

#         self.__name = value


# student = Student("Mark", 27, 4.2)

# student.get_info()

# student.name = "Martin"

# print(student.name)

# student.get_info()


class Student:

    def __init__(self, name, age, gpa):
        self.__name = name
        self.__age = age
        self.__gpa = gpa

    def get_info(self):
        print(f"Name:{self.__name}")
        print(f"Age:{self.__age}")
        print(f"Gpa:{self.__gpa}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == "":
            print("Please fill the line!")
        else:
            self.__name = name


student = Student("Aaron", 27, 4.2)

student.get_info()

student.set_name("Jason")

student.get_info()

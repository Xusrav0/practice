print('==== number ====')

# in Java => variable is the name of storage location
# in Python => variable is the named reference (reference storage locationga qaratilgan)

count = 100
count_type = type(count)
# print("count:", count, count_type)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print('==== string ====')
# Method: upper() lower() title() find() replace() - bu methodlar variableni uzini qiymatiga tasir ko'rsatmidi

course = "AI Python Fullstack"
result3 = type(course)
print(f"the result (1): {result3}")
result = course.title()
print(f"the result (2): {result}")

result = course.upper()
print(f"the result (3): {result}")


result = course.replace("Fullstack", "MasterClass")
print(f"the result (4): {result}")


# course = course.replace("Fullstack", "MasterClass")
# print(f"the result (4): {result}")
# uziga tenglaganda shunda course qiymati uzgaradi

print('==== boolean ====')
# functions => type() input() bool() int() str()

y = input("Give your value for y:")
print(y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

# Truthy vs Falsy value

# TRUTHY > True 100 -100 "MIT"
# FALSY > False 0 "" None


test_falsy = "" or False or None or 0
# agar or 100 qo'yilsa natija True bo'ladi
print("The FALSY:", bool(test_falsy))

test_truthy = "MIT"
print("test_truthy:", bool(test_truthy))

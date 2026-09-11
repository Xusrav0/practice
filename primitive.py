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

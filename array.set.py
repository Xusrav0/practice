''' Array & Set
(1) Array
(2) Set
(3) Specific operators with set
'''

from array import array
print('====== Array ======')

# i - int, f - float dan iborat bo'ladi array
# Juda ko'p bo'lgan sonlar ketmaketligida ishlatamiz/ katta data bilan ishlatamiz
numbers = array('i', [1, 4, 5, 7, 8, 41])
print('numbers(1)', numbers)
numbers.append(100)
numbers.insert(0, 14)
print('numbers(2)', numbers)

numbers.remove(5)
numbers.pop()
print('numbers(3)', numbers)

del numbers[0:2]   # [0;2)
print('numbers(4)', numbers)

print('====== Set ======')
# set of unique collection without keeping order! (takroriy sonlarni bir marta qabul qiladi)
new_numbers = array('i', [1, 4, 7, 5, 7, 5, 4, 7, 8, 41])
numbs_set = set(new_numbers)

print('numbers_set:', numbs_set)
print(f'the numbers_set: {numbs_set} and type: {type(numbs_set)}')

numbs_set.add(200)
print('numbers_set(1):', numbs_set)

numbs_set.add(7)
print('numbers_set(2):', numbs_set)  # uzgarmaydi output 7 bor

print('====== Specific operators with set ======')
# | & - ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union
result2 = a & b  # intersection => ham a va b to'plamida bo'lganni oladi
result3 = a - b  # difference
# symmetric difference (to'plamda bir birida qatnashmaganni oladi)
result4 = a ^ b

print('result1:', result1)
print('result2:', result2)
print('result3:', result3)
print('result4:', result4)

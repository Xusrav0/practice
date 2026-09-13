print('===== Iterable objects & Range =====')
# iterate (takrorlanish) objects => string dict tuple list range map filter


text = "MIT"
for letter in text:
    print(f"the letter: {letter}")

range_obj = range(3) # [0:3)
print("range_obj", range_obj)

for ele in range_obj:
    print(f"the element: {ele}")


print('===== Dictionary =====')

# Dictionary is JSON object!
person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Justin", age=25, single=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# Valuesini ko'rmoqchi bo'lsak
name = person_obj['name']
print("name:", name)

# Error beradi chunki hobby yo'q
#name2 = person_obj['hobby']
#print("name2:", name2)

# method: get
name2 = person_obj.get('name')
hobby = person_obj.get("hobby")
balance = person_obj.get("balance:", 0)
print(f"the name: {name}, hobby: {hobby} and balance: {balance}") # hobby None chiqadi

# del oper
del person_obj['single'] # single state o'chiriladi

for key in person_obj:
    print(f"the key: {key} => value {person_obj[key]} ") # yoki {person_obj.get(key)} bir xil


names = [
    "Fred",
    "Jim",
    "Sheila"
]  # list is builtin (arrays are a library)
print(names)
print(type(names))
print(names[0])
names[0] = "Frederick"
print(names)

# slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:5])
print(numbers[2:8:3])
print(numbers[2:28:3])
print(numbers[::-1])
print(numbers[-2:])

numbers[3:6] = [-1, -2, -3, -4, -5]
print(numbers)
print(f"list contains 1? {1 in numbers}")

print(f"first + second is {numbers[0] + numbers[1]}")

numbers[0] = "hello"
print(numbers)
# print(f"first + second is {numbers[0] + numbers[1]}")

print("---------------------------")
n = [
    3,
    1,
    2,
    0,
]
print(n)

print("---------------------------")
print(n)

for v in n:
    print(f"> {v}")

print("---------------------------")
letters = {"A":["AA", "AAA"]}
print(letters)
print(letters["A"])

print("---------------------------")
names = {"Fred": "Staff", "Jim": "Manager", "Sheila": "Director"}
print(names)
print(type(names))
print(names["Fred"])
# print(names["Frederick"])

is_found = "Frederick" in names  # bool literals are True False
print(is_found)
print(type(is_found))
names["Fred"] = "Supervisor"
print()
print(names)

# for v in names:
# for v in names.keys():
# for v in names.values():
for v in names.items():
    print(v)

print(v)
print(type(v))
print(v[0])
print(v[1])

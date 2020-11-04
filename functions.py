
# Zeller's congurence dow 0->Saturday 6->Friday, for day, month, year

# NO OVERLOADING
# def day_of_week(day, month):
#     return 100

def day_of_week(day, month, year=2000):
    # if month < 3:
    #     m = month + 12
    #     y = year - 1
    m, y = (month, year) if month > 2 else (month + 12, year - 1)
    return (day + (13 * (month + 1) // 5) + year + year // 4 - year // 100 + year // 400) % 7
# % in python is MATH mod, not "remainder"

dow = day_of_week(1, 1, 2000)
print(f"jan 1 2000 is {dow}")

print(day_of_week(1,1))
print(day_of_week(4, 12, 2000)) # "positional"
print(day_of_week(month=12, year=2000, day=4))
print(day_of_week(day=4, month=12, year=2000))
print(day_of_week(day=4, month=12))

print('-------------------------------------')

def many_args(*args):
    # args is a sequence, iterable
    for v in args:
        print(f"{v}, ", end="")
    print()

many_args(1, 3, 5, 7, 9)
many_args("hello", 5, "goodbye")

names = ["Fred", "Jim", "Sheila"]
many_args(*names)

date_parts = [1, 3, 2000]
print(day_of_week(*date_parts))


print('-------------------------------------')
def more_args(a, b, *args, **kwargs):
    print(f"a is {a}")
    print(f"b is {b}")
    # args is a sequence, iterable
    for v in args:
        print(f"{v}, ", end="")
    print()
    for item in kwargs.items():
        print(f"key={item[0]} value={item[1]}")

more_args(4, 5, 6, 7, 8, 9, fred="Manager", albert="Trainer")

print('-------------------------------------')
add = lambda x, y: x + y

def sum(a, b):
    return a + b

add2 = sum

print(add(1, 3))
print(add2(1, 3))
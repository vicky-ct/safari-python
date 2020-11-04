 # no declaration, simply assign
x = 99
print(x)
print(type(x))
x = 3.14
print(x)
print(type(x))
x = '"Hello\''
print(x)
print(type(x))

a = 99
b = 9
b += 90
print(a is b)
print(a == b)
# print(99 is 99)

print("========================")
a = "Hello"
b = "Hel"
b += "lo"  # equivalent to b = b + "lo"
print(a is b)
print(a == b)  # might depend on object providing __eq__ method
print(a)
print(b)

print("========================")
print("hello " + "world")  # string concatenation
print("hello ", "world", sep="+-+-", end="")  # print is varargs
print("it's a nice day")

s = f"The value of a is {a} and a plus b is {a + b}"
print(s.upper())
print(s)

print("========================")
x = 1E+308  # IEEE 754 64 bit floating point
print(x)
x = 10
x = x ** 500  # int type is bounded by memory, ** raise to power
print(x)
x = 10
y = 3
print(x / y)  # "normal" division (single /) create float result
print(x // y)

print("========================")
print("hello " + str(99))
# x = "99 hello"
x = "99"
y = 100
z = float(x) + y
print(z)

print("========================")
x = "Hello"
print(bool(x))
if x:
    print("That's True!")
else:
    print("That's False")
print("========================")
print(f"bool(0) {bool(0)}")
print(f"bool(100) {bool(100)}")
print(f"bool('') {bool('')}")
print(f"bool('goodbye') {bool('goodbye')}")
print(f"bool([1,2,]) {bool([1,2,])}")
print(f"bool([]) {bool([])}")



# from __future__ import braces

names = ["Fred", "Jim", "Sheila"]

for name in names:  # indentation controls meaning!!!
    print(name)
    # print("That broke")  # indentation must be consistent (and four spaces :)

print("------------------------------")
x = 0
# while x < names.__len__():  # Internal **don't do this!!!**
while x < len(names):  # Internal **don't do this!!!**
    x += 1
    if x == 2:
        # continue
        break
    print(names[x-1])

print("-------------------")
x = 1
while x < 10:
    if x == 5:
        # pass
        break
        # x += 1
        # continue
    x += 1
    print(x)
else:  # if we broke, fine. if we didn't else
    print("in the else")

print("-------------------")
x = 10
for n in range(2, x - 1):
    if x / n % 1 == 0:
        break
else:
    print(f"{x} is prime")

print("-------------------")
from random import random as r
print(r())
x = r()
# if x < 0.3:
#     print(f"it's small {x}")
# else:
#     if x > 0.6:
#         print(f"really big {x}")
#     else:
#         print(f"medium {x}")

if x < 0.3:
    print(f"it's small {x}")
elif x > 0.6:
    print(f"really big {x}")
else:
    print(f"medium {x}")

# python does not have case/switch ...
# some folks use dict to fake it.



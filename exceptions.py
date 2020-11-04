import random

try:
    print("hello")
    if random.random() > 0.5:
        raise ValueError("That's too big")
    x = 99
    y = 0
    print(x / y)
    print("Do you like that")
# except:  Catches *everything* including stuff you likely didn't mean
except ZeroDivisionError as ex:
    print(f"that caused: {ex}")
except ValueError as ve:
    print(f"got a value error {ve}")
finally:
    print("Still going")

print("finished that chunk")

with open("data.txt", "w") as file:
    file.write("Hello, I'm some text")

file.write("really?")


class Date:
    # don't declare fields.. we stuff the object with them
    def __init__(self, day, month, year):
        print("initilizing Date part...")
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"Date with day={self.day} month={self.month} year={self.year}"

    def __repr__(self):
        return str(self)

class Named:
    def __init__(self, n):
        print(f"init with {n}")

class Holiday(Date, Named):  # multiple (Date, Named)
    def __init__(self, day, month, year, name):
        super().__init__(day, month, year)
        super(Date, self).__init__(name)
        self.name = name

x = Date(1, 2, 2020)

print(x)
print(type(x))
print(isinstance(x, Date))

l = [Date(1, 2, 2020), Date(1, 2, 2020)]
print(l)

print("--------------------")
h = Holiday(1, 1, 2021, "New Year's Day")

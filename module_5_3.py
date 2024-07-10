class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        x = 0
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            while x < new_floor:
                x += 1
                print(x)

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}."

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        isinstance(other, int)
        return self.number_of_floors == other

    def __lt__(self, other):
        isinstance(other, int)
        return self.number_of_floors < other

    def __le__(self, other):
        isinstance(other, int)
        return self.number_of_floors <= other

    def __gt__(self, other):
        isinstance(other, int)
        return self.number_of_floors > other

    def __ge__(self, other):
        isinstance(other, int)
        return self.number_of_floors >= other

    def __ne__(self, other):
        isinstance(other, int)
        return self.number_of_floors != other

    def __add__(self, value):
        self.number_of_floors += value
        return self.number_of_floors

    def __radd__(self, value):
        self.number_of_floors += value
        return self.number_of_floors

    def __iadd__(self, value):
        self.number_of_floors += value
        return self.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1.__eq__(h2))

h1.__add__(10)
print(h1)
print(h1.__eq__(h2))

h1.__iadd__(10)
print(h1)

h2.__radd__(10)
print(h2)

print(h1.__gt__(h2))
print(h1.__ge__(h2))
print(h1.__lt__(h2))
print(h1.__le__(h2))
print(h1.__ne__(h2))

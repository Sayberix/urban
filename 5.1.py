class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, к-во этажей: {str(self.number_of_floor)}'

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor

    def __add__(self, other):
        new_name = ''
        new_number_of_floor = 0
        if isinstance(other, House):
            new_name = f'{self.name} + {other.name}'
            new_number_of_floor = self.number_of_floor + other.number_of_floor
        elif isinstance(other, int):
            new_name = self.name
            new_number_of_floor = self.number_of_floor + other
        else:
            print("Невозможно сложить объекты типа!")

        return House(new_name, new_number_of_floor)

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
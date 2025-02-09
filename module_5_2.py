# Домашняя работа по уроку
# "Специальные методы классов"
# Задача "Магические здания"



class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor < 1 or self.new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for self.new_floor in range(1, new_floor + 1):
                print(self.new_floor)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f'Название: {self.name}, Кол-во этажей: {self.number_of_floors}')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor + 1):
                if i == 0:
                    continue
                print(i)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
One = House('ЖК Эльбрус', 30)
Two = House('ЖК Палермо', 20)
Three = House('ЖК Эстрада', 10)
print(One)
print(Two)
print(Three)
print(len(One))
print(len(Two))
print(len(Three))

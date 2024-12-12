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
One = House('ЖК Эльбрус', 30)
Two = House('ЖК Палермо', 20)
Three = House('ЖК Эстрада', 10)
One.go_to(30)
Two.go_to(4)
Three.go_to(30)

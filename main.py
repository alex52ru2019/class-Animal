# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Нельзя вызвать метод на прямую")

    def eat(self):
        print(f"{self.name} кушает.")

# Подклассы Bird, Mammal, и Reptile
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирик чирик ")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} ля ля ля ")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} пшшш пшшш пшшш")

# Полиморфизм: функция для вызова звуков животных
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Классы сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Класс Zoo, использующий композицию
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} был добавлен в zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member.name} был добавлен в zoo.")

# Пример использования
if __name__ == "__main__":
    # Создаем животных
    bird = Bird("Калибри", 200, " 2 метра ")
    mammal = Mammal("Лев", 5, "золотой мех")
    reptile = Reptile("Змея", 3, "Гладкая")

    # Создаем сотрудников
    keeper = ZooKeeper("Браконьер Вася")
    vet = Veterinarian("Айболит")

    # Создаем зоопарк
    zoo = Zoo()

    # Добавляем животных и сотрудников в зоопарк
    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрируем полиморфизм
    animal_sound(zoo.animals)

    # Демонстрируем методы сотрудников
    keeper.feed_animal(bird)
    vet.heal_animal(mammal)
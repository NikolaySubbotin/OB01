class Warrior():

  def __init__ (self, name, power, endurance, hair_color):
    self.name = name
    self.power = power
    self.endurance = endurance
    self.hair_color = hair_color

  def sleep (self):
    print(f"{self.name} лег спать")
    self.endurance += 2

  def eat (self):
    print(f"{self.name} кушает")
    self.power += 1

  def attack (self):
    print(f"{self.name} нанес удар")
    self.endurance -= 6

  def walk(self):
    print(f"{self.name} идет")

  def info(self):
    print(f"Имя: {self.name}")
    print(f"Сила: {self.power}")
    print(f"Выносливость: {self.endurance}")
    print(f"Цвет волос: {self.hair_color}")


war1 = Warrior("Александр", 87, 54, "коричневый")
war2 = Warrior("Коля", 96, 42, "Зеленый")

print(war1.endurance)
war1.sleep()
print(war1.endurance)
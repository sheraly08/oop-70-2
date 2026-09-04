import random
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    def greet(self):
        return f"Приветствую, я {self.name}"
    def attack(self):
        return f"{self.name} наносит удар"
    def rest(self):
        self.health += 5
        return f"{self.name} отдыхает и восстанавливает {self.health}"


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina
    def attack(self):
        return f"{self.name} атакует мечом! "

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        return f"{self.name} кастует заклинание! "

class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        return f"{self.name} атакует из-под тишка! "

warrior = Warrior('Warrior', 5, 100, 78, 80)
mage = Mage("Mage", 9, 50, 77, 5)
assassin = Assassin("Assassin", 10, 100, 100, 95)

heroes = [warrior, mage, assassin]

while True:
    opponent = random.choice(heroes)
    choice = input('Выберите героя: Warrior/Mage/Assassin ').lower()
    if choice == 'стоп':
        break
    if choice == warrior.name.lower():
        if opponent.name == "Assassin":
            print('Вы выбрали: Warrior \n Противник: Assassin \n Warrior победил! ')
        elif opponent.name == "Mage":
            print('Вы выбрали: Warrior \n Противник: Mage \n Mage победил!')
        elif opponent.name == "Warrior":
            print('Вы выбрали: Warrior \n Противник: Warrior \n Ничья! ')
    if choice == mage.name.lower():
        if opponent.name == "Assassin":
            print('Вы выбрали: Mage \n Противник: Assassin \n Assassin победил! ')
        elif opponent.name == "Warrior":
            print('Вы выбрали: Mage \n Противник: Warrior \n Mage победил! ')
        elif opponent.name == "Mage":
            print('Вы выбрали: Mage \n Противник: Mage \n Ничья! ')
    if choice == assassin.name.lower():
        if opponent.name == "Warrior":
            print('Вы выбрали: Assassin \n Противник: Warrior \n Warrior победил! ')
        elif opponent.name == "Mage":
            print('Вы выбрали: Assassin \n Противник: Mage \n Assassin победил! ')
        elif opponent.name == "Assassin":
            print('Вы выбрали: Assassin \n Противник: Assassin \n Ничья! ')
















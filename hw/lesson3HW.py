from abc import ABC, abstractmethod




class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength
    def greet(self):
        return f"Привет, я {self.name}, мой уровень {self.level}"
    def rest(self):
        self.__health += 1
        return f"{self.name} отдыхает, здоровье: {self.__health}"
    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    def attack(self):
        return f"{self.name} атакует мечом"

class Mage(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    def attack(self):
        return f"{self.name} использует магию"

class Assassin(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    def attack(self):
        return f"{self.name} атакует из-под тишка"

warrior = Warrior('Warrior', 10, 80, 80)
mage = Mage("Mage", 7, 99, 70)
assassin = Assassin("Assassin", 9, 60, 85)


print(warrior.greet())
print(warrior.rest())
print(warrior.attack())

print('')


print(mage.greet())
print(mage.rest())
print(mage.attack())

print('')


print(assassin.greet())
print(assassin.rest())
print(assassin.attack())

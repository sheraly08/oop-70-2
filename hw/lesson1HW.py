
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        return f"Привет, я {self.name}, мой уровень {self.level}"

    def attack(self):
        self.strength -= 1
        return f"{self.name} наносит удар!"

    def rest(self):
        self.health += 1
        return f"{self.name} отдыхает"


hugo = Hero("Hugo", 10, 100, 100)
loki = Hero("Loki", 8, 100, 100)

print("Hugo")
print(f"До действий: здоровье={hugo.health}, сила={hugo.strength}")
print(hugo.greet())
print(hugo.attack())
print(hugo.rest())
print(f"После действий: здоровье={hugo.health}, сила={hugo.strength}")

print()

print("Loki")
print(f"До действий: здоровье={loki.health}, сила={loki.strength}")
print(loki.greet())
print(loki.attack())
print(loki.rest())
print(f"После действий: здоровье={loki.health}, сила={loki.strength}")
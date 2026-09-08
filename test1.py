class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f"{self.name} готов к бою"


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp ):
        super().__init__(name, lvl, hp, mp)
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"



class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name
    def login(self, password):
        if self.__password == password:
            return f"Вход выполнен"
        else:
            return f"Ошибка"
    def full_info(self):
        return f"{self.hero.name}: баланс: {self._balance} "
    def get_bank_name(self):
        return self.bank_name
    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"
    def __add__(self, other):
        if type(self.hero) != type(other.hero):
            return f"Ошибка: Нельзя сложить счета героев разных классов!"
        else:
            return self._balance + other._balance

    def __eq__(self, other):
        return type(self.hero) == type(other.hero) and self.hero.lvl == other.hero.lvl


merlin = MageHero("Merlin", 50, 100, 150)
conan = WarriorHero("Conan", 50, 100, 150)
merlin2 = MageHero("Merlin", 50, 100, 150)

acc1 = BankAccount(merlin, 5000, 3234, "Simba")
acc2 = BankAccount(merlin2, 3000, 34113, "Simba")
acc3 = BankAccount(conan, 1000, 535642, "Simba")

print(merlin.action())
print(conan.action())
print(acc1)
print(acc2)
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

print()
## --- Магические методы: __add__ ---

print("=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)
print(acc1 + acc3)

print()
# --- Магический метод: __eq__ ---

print("=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

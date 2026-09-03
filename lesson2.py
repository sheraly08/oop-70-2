# Родительский\Супер класс
class Hero:
    # Конструктор класса
    def __init__(self, name, lvl=1, hp=100):
        #Атрибуты экземпляра\объекта класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    # Метод класса
    def base_action(self):
        return f"{self.name} this my base action!!"
    def method_1(self):
        return "i'm method_1"

# Дочерний класс
class MageHero(Hero):

    def __init__(self, name, lvl=1, hp=100, mp=100):
        #Атрибуты экземпляра\объекта класса
        super().__init__(name, lvl, hp)
        self.mp = mp

    def cast_spell(self):
        return f"{self.name} fire boll!!"

    def method_1(self):
        return f"{self.name}-{self.lvl}-{self.hp}"


ardager = Hero("ardager")
gerald = MageHero("Gerald")
print(gerald.mp)
print(ardager.hp)
# print(ardager.method_1())
# print(gerald.method_1())

class Swim:
    def swim(self):
        print('Swim')

class Fly:
    def fly(self):
        print('Fly')

class Duck(Fly, Swim):
    pass

donald_duck = Duck()


# donald_duck.fly()
# donald_duck.swim()

# HeroMage
# donald_duck

class A:
    def action(self):
        print('A')

class B(A):
    def action(self):
        super().action()
        print("B")

class C(A):
    def action(self):
        super().action()
        print("C")

class D(C):
    def action(self):
        super().action()
        print('D')

test_obj = D()
test_obj.action()
print(D.mro())
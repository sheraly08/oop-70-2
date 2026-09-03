# data = "Ardager"
#
# name = data

# def  init_test(self, name, lvl, hp):
#     pass
#
# init_test()



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

kirito = Hero("Kirito")# 1
asuna = Hero("Asuna", 111, 1111)# 2
my_int = int(123)
my_str = "TEXT"
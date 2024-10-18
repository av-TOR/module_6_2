class Vehicle:
    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    __COLOR_VARIANTS = ['blue', 'green', 'black', 'white']

    def get_model(self):
        return print(f"Модель: {self.__model}")

    def get_horsepower(self):
        return print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        return print(f"Цвет: {self.__color}")

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        return print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        str(new_color)
        flag = False
        for i in self.__COLOR_VARIANTS:
            if i.lower() == new_color.lower():
                self.__color = new_color
                flag = True

        if flag is False:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


Car = Sedan("Alex", "BYD", 98, "black")

Car.print_info()
Car.set_color('Yellow')
print("---------------------------------------")
Car.set_color('whiTe')
Car.owner = 'Elena'

Car.print_info()

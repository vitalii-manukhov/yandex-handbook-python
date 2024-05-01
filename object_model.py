# # TEST
# flag_1 = False
# flag_2 = True

# def check_not(flag_1_, flag_2_):
#     if not flag_1_ and flag_2_:
#         return True
#     else:
#         return False
    
# def check_not_not(flag_1_, flag_2_):
#     if not flag_1_ and not flag_2_:
#         return True
#     else:
#         return False
    
# result = check_not(flag_1, flag_2)

# print(result)

# result = check_not_not(flag_1, flag_2)

# print(result)
# # TEST

# Процедурное программирование с помощью функций
def create_car(color,
               tank_volume,
               consumption,
               mileage = 0):
    return {
        "color": color,
        "tank_volume": tank_volume,
        "reserve": tank_volume,
        "consumption": consumption,
        "mileage": mileage,
        "engine_on": False
    }

def start_engine(car):
    if not car["engine_on"] and car["reserve"] > 0:
        car["engine_on"] = True
        return "Двигатель запущен."
    return "Двигатель уже был запущен или нет топлива."

def stop_engine(car):
    if car["engine_on"]:
        car["engine_on"] = False
        return "Двигатель остановлен."
    return "Двигатель уже был остановлен."

def drive(car, distance):
    if not car["engine_on"]:
        return "Двигатель не запущен"
    if car["reserve"] / car["consumption"] * 100 < distance:  # л/100км
        return "Малый запас топлива."
    car["mileage"] += distance
    car["reserve"] -= car["consumption"] * distance / 100
    return f"Проехали {distance} км. Остаток топлива: {car['reserve']}"

def refuel(car):
    car["reverse"] = car["tank_volume"]

def get_mileage(car):
    return f"Пробег {car['mileage']} км."

def get_reserve(car):
    return f"Запас топлива {car['reserve']} л."

car_1 = create_car(color="pink", consumption=10, tank_volume=60)

# # testing car
# print(start_engine(car_1))
# print(drive(car_1, 100))
# print(drive(car_1, 100))
# print(drive(car_1, 100))
# print(drive(car_1, 300))
# print(get_mileage(car_1))
# print(get_reserve(car_1))
# print(stop_engine(car_1))
# print(drive(car_1, 100))

# Создание класса
class MyCar:
    
    def __init__(self,
                 color,
                 tank_volume,
                 consumption,
                 mileage = 0):
        self.color = color
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False
        self.consumption = consumption

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен или нет топлива."

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен"
        if self.reserve / self.consumption * 100 < distance:  # л/100км
            return "Малый запас топлива."
        self.mileage += distance
        self.reserve -= self.consumption * distance / 100
        return f"Проехали {distance} км. Остаток топлива: {self.reserve}"

    def refuel(self):
        self.reverse = self.tank_volume

    def get_mileage(self):
        return f"Пробег {self.mileage} км."

    def get_reserve(self):
        return f"Запас топлива {self.reserve} л."
    
# car_1 = MyCar("light gray", 55, 10)
# print(car_1.start_engine())
# print(car_1.drive(100))
# print(car_1.drive(100))
# print(car_1.drive(100))
# print(car_1.drive(300))
# print(f"Пробег {car_1.get_mileage()} км.")
# print(f"Запас топлива {car_1.get_reserve()} л.")
# print(car_1.stop_engine())
# print(car_1.drive(100))

# ТЕСТ
# Взаимодействие с атрибутами (полями) объекта класса напрямую
# car_1 = MyCar("dark chocolate", 100, 20)
# car_1.mileage = 999.5
# print(car_1.mileage)

class Mechanism:

    def __init__(self, energy_source_name, power_name):
        self.energy_source_name = energy_source_name
        self.power_name = power_name

    def get_energy_source(self):
        return self.energy_source_name
    
    def get_power_name(self):
        return self.power_name
    
class Transport:

    def __init__(self, transoprt_name):
        self.name = transoprt_name

    def get_transport_name(self):
        return self.name

class Car(Mechanism, Transport):

    def __init__(self, color, consumption, capacity, mileage=0):
        Mechanism.__init__(self, "engine", "horse power")
        Transport.__init__(self, "car")
        self.color = color
        self.consumption = consumption
        self.tank_volume = capacity
        self.reserve = capacity
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен."

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."

    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return self.mileage

    def get_reserve(self):
        return self.reserve

    def get_consumption(self):
        return self.consumption


class ElectricCar(Car):

    def __init__(self, color, consumption, capacity, acceleration_hundred, mileage=0):
        super().__init__(color=color,
                         consumption=consumption,
                         capacity=capacity,
                         mileage=mileage)
        self.acceleration_hundred = acceleration_hundred

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / self.consumption * 100 < distance:
            return "Малый заряд батареи."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

    def recharge(self):
        self.reserve = self.bat_capacity

    # Magic method
    def __str__(self):
        return f"Электромобиль. " \
               f"Цвет: {self.color}. " \
               f"Пробег: {self.mileage} км. " \
               f"Остаток заряда: {self.reserve} кВт*ч."


def range_reserve(car):
    return car.get_reserve() / car.get_consumption() * 100


# car_1 = Car(color="black", consumption=10, capacity=55)
# car_2 = ElectricCar(color="white", consumption=15, capacity=90, acceleration_hundred=5)
# print(car_1)
# print(car_2)
# print(f"Запас хода обычного автомобиля: {range_reserve(car_1)} км.")
# print(f"Запас хода электрического автомобиля: {range_reserve(car_2)} км.")
# print(car_2)

# Специальные методы
# print(str(car_1))
# print(repr(car_1))

# Практика
# Class Programmer
class Programmer:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.time = 0
        self.savings = 0
        if (position == "Junior"):
            self.salary = 10
        elif (position == "Middle"):
            self.salary = 15
        else:
            self.salary = 20

    def work(self, time):
        self.time += time
        self.savings += self.salary * time

    def rise(self):
        if (self.position == "Junior"):
            self.position = "Middle"
            self.salary = 15
        elif (self.position == "Middle"):
            self.position = "Senior"
            self.salary = 20
        else:
            self.salary += 1

    def info(self):
        return f"{self.name} {self.time}ч. {self.savings}тгр."
    
# first = Programmer("Виталий", "Middle")

# print(first.info())

# second = Programmer("Василий Иванов", "Junior")

# second.work(750)
# print(second.info())
# second.rise()
# second.work(500)
# print(second.info())
# second.rise()
# second.work(250)
# print(second.info())
# second.rise()
# second.work(250)
# print(second.info())

# # Class Rectangle
# class Rectangle:

#     def __init__(self, angle_first, angle_second):
#         self.left_upper_angle = (round(min(angle_first[0], angle_second[0]), 2), 
#                                  round(max(angle_first[1], angle_second[1]), 2))
#         self.right_lower_angle = (round(max(angle_first[0], angle_second[0]), 2),
#                                   round(min(angle_first[1], angle_second[1]), 2))

#         if (self.left_upper_angle[0] <= 0 and self.right_lower_angle[0] >= 0 or self.left_upper_angle[0] >= 0 and self.right_lower_angle[0] <= 0):
#             self.center = (round((self.left_upper_angle[0] + self.right_lower_angle[0]) / 2, 2), 0)
#         else:
#             self.center = (round((self.left_upper_angle[0] - self.right_lower_angle[0]) / 2, 2), 0)

#         if (self.left_upper_angle[1] <= 0 and self.right_lower_angle[1] >= 0 or self.left_upper_angle[1] >= 0 and self.right_lower_angle[1] <= 0):
#             self.center = (self.center[0], round((self.left_upper_angle[1] + self.right_lower_angle[1]) / 2, 2))
#         else:
#             self.center = (self.center[0], round((self.left_upper_angle[1] - self.right_lower_angle[1]) / 2, 2))

#     def perimeter(self):
#         return round(round(abs(self.left_upper_angle[0] - self.right_lower_angle[0]), 2) * 2 + 
#                      round(abs(self.left_upper_angle[1] - self.right_lower_angle[1]), 2) * 2, 2)

#     def area(self):
#         return round(round(abs(self.left_upper_angle[0] - self.right_lower_angle[0]), 2) * 
#                      round(abs(self.left_upper_angle[1] - self.right_lower_angle[1]), 2), 2)

#     def get_pos(self):
#         return (round(self.left_upper_angle[0], 2),
#                 round(self.left_upper_angle[1], 2))

#     def get_size(self):
#         return (round(abs(self.left_upper_angle[0] - self.right_lower_angle[0]), 2),
#                 round(abs(self.left_upper_angle[1] - self.right_lower_angle[1]), 2))

#     def move(self, shift_x, shift_y):
#         self.left_upper_angle = (round(self.left_upper_angle[0] + shift_x, 2), 
#                                  round(self.left_upper_angle[1] + shift_y, 2))
#         self.right_lower_angle = (round(self.right_lower_angle[0] + shift_x, 2), 
#                                   round(self.right_lower_angle[1] + shift_y, 2))

#     def resize(self, width, height):
#         self.right_lower_angle = (round(self.left_upper_angle[0] + width, 2), 
#                                   round(self.left_upper_angle[1] + height, 2))

#     def turn(self):

#         self.left_upper_angle, self.right_lower_angle = (self.left_upper_angle[0], self.right_lower_angle[1]), (self.right_lower_angle[0], self.left_upper_angle[1])

#         self.left_upper_angle = (self.left_upper_angle[1], round((-1) * self.left_upper_angle[0], 2))
#         self.right_lower_angle = (self.right_lower_angle[1], round((-1) * self.right_lower_angle[0], 2))


#     def scale(self, factor):
#         self.left_upper_angle = (round(self.left_upper_angle[0] * factor, 2), round(self.left_upper_angle[1] * factor, 2))
#         self.right_lower_angle = (round(self.right_lower_angle[0] * factor, 2), round(self.right_lower_angle[1] * factor, 2))

# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.scale(2.0)
# print(rect.get_pos(), rect.get_size(), sep='\n')

# Rect2
class Rectangle:

    def __init__(self, angle_first, angle_second):
        self.left_upper_angle = (round(min(angle_first[0], angle_second[0]), 2), 
                                 round(max(angle_first[1], angle_second[1]), 2))
        self.right_lower_angle = (round(max(angle_first[0], angle_second[0]), 2),
                                  round(min(angle_first[1], angle_second[1]), 2))

    def perimeter(self):
        return round(round(abs(self.left_upper_angle[0] - self.right_lower_angle[0]), 2) * 2 + 
                     round(abs(self.left_upper_angle[1] - self.right_lower_angle[1]), 2) * 2, 2)

    def area(self):
        return round(round(abs(self.left_upper_angle[0] - self.right_lower_angle[0]), 2) * 
                     round(abs(self.left_upper_angle[1] - self.right_lower_angle[1]), 2), 2)

    def get_pos(self):
        return (round(self.left_upper_angle[0], 2),
                round(self.left_upper_angle[1], 2))

    def get_size(self):
        return (round(abs(self.left_upper_angle[0] - self.right_lower_angle[0]), 2),
                round(abs(self.left_upper_angle[1] - self.right_lower_angle[1]), 2))

    def move(self, shift_x, shift_y):
        self.left_upper_angle = (round(self.left_upper_angle[0] + shift_x, 2), 
                                 round(self.left_upper_angle[1] + shift_y, 2))
        self.right_lower_angle = (round(self.right_lower_angle[0] + shift_x, 2), 
                                  round(self.right_lower_angle[1] + shift_y, 2))

    def resize(self, width, height):
        self.right_lower_angle = (round(self.left_upper_angle[0] + width, 2), 
                                  round(self.left_upper_angle[1] + height, 2))

    def turn(self):

        temporary_angle = self.left_upper_angle
        self.left_upper_angle  = (self.left_upper_angle[0], self.right_lower_angle[1]) 
        self.right_lower_angle = (self.right_lower_angle[0], temporary_angle[1])

        self.left_upper_angle = (self.left_upper_angle[1], 
                                 round((-1) * self.left_upper_angle[0], 2))
        self.right_lower_angle = (self.right_lower_angle[1],
                                  round((-1) * self.right_lower_angle[0], 2))

    def scale(self, factor):
        self.left_upper_angle = (round(self.left_upper_angle[0] * factor, 2), 
                                 round(self.left_upper_angle[1] * factor, 2))
        self.right_lower_angle = (round(self.right_lower_angle[0] * factor, 2),
                                  round(self.right_lower_angle[1] * factor, 2))

# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.turn()
# print(rect.get_pos(), rect.get_size(), sep='\n')

# Checkers
# Можно использовать hashable map - dict() или list

# # Test
# for symbol_number in range(8):
#     print(f"{chr(ord('A') + symbol_number)} : {ord('A') + symbol_number}")
# # Test

# # Test
# # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/]
#     deck = [[0] * 3 for _ in range(3)]
#     deck[1][0] = 1

#     def ViewDeck(deck, size):
#         for line_number in range(size):
#             for cell_number in range(size):
#                 print(deck[line_number][cell_number], end = ' ')
#             print()

#     ViewDeck(deck, len(deck))

# # Test

# # Test
# # Create a 3x3 2D list initialized with zeros
# matrix = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]

# # Insert 1 at indices (1, 1)
# matrix[1][1] = 1

# # Print the updated matrix
# for row in matrix:
#     print(row)
# # Test

# # Test
# str = "C3"
# print((ord(str[0]) - 1) % 8, int(str[1]) - 1)
# # Test

# class Cell:
    
#     def __init__(self, condition):
#         if condition == 'W':
#             self.condition = 'W'
#         elif condition == 'B':
#             self.condition = 'B'
#         elif condition == 'X':
#             self.condition = 'X'

#     def status(self):
#         return self.condition

# class Checkers:

#     def __init__(self):
#         self.deck = [[Cell('X') for _ in range(8)] for _ in range(8)]

#         for line_number in range(8):
#                 for cell_number in range(8):
#                     if (line_number + cell_number) % 2 == 0 and line_number < 3:                   
#                         self.deck[line_number][cell_number].condition = 'W'
#                     elif (line_number + cell_number) % 2 == 0 and line_number > 4:
#                         self.deck[line_number][cell_number].condition = 'B'

#     def ViewDeck(self):
#         for row in range(7, -1, -1):
#             for column in range(8):
#                 print(self.deck[row][column].status(), end = ' ')
#             print()

#     def move(self, f, t):
#         current_position = ((ord(f[0]) - 1) % 8, int(f[1]) - 1)
#         new_position = ((ord(t[0]) - 1) % 8, int(t[1]) - 1)
        
#         self.deck[current_position[0]][ current_position[1]] = 'X'
        
#         if new_position[0] - current_position[0] > 1:
#             count = ...

#     def get_cell(self, p):
#         # print('\n')
#         # print((ord(p[0]) - 1) % 8, int(p[1]) - 1)
#         return self.deck[int(p[1]) - 1][(ord(p[0]) - 1) % 8]

# checkers = Checkers()
# for row in '87654321':
#     for col in 'ABCDEFGH':
#         print(checkers.get_cell(col + row).status(), end='')
#     print()

# Point 3
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, x_distance, y_distance):
        self.x += x_distance
        self.y += y_distance

    def length(self, other):
        return round(((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** (1 / 2), 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(x=0, y=0)
        elif len(args) == 1:
            super().__init__(x=args[0][0], y=args[0][1])
        elif len(args) == 2:
            super().__init__(x=args[0], y=args[1])

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, other):
        new_point = PatchedPoint(self.x + other[0],
                                 self.y + other[1])

        return new_point

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]

        return self

def CheckInit():
    # Добавить print(number) в каждый if в __init__

    point = PatchedPoint()
    print(point.x, point.y)
    point = PatchedPoint((1, 1))
    print(point.x, point.y)
    point = PatchedPoint(2, 2)
    print(point.x, point.y)

# first_point = second_point = PatchedPoint((2, -7))
# print(first_point, second_point, first_point is second_point)
# first_point += (7, 3)
# print(first_point, second_point, first_point is second_point)

# Fraction 1
class Fraction:

    def __init__(self, *args):
        if len(args) == 1:
            numerator_str, denominator_str = args[0].split(sep='/')
            
            if int(numerator_str) < 0 and \
               int(denominator_str) < 0:
                self.__numerator, self.__denominator = (
                    abs(int(numerator_str)), 
                    abs(int(denominator_str)))
            elif int(denominator_str) < 0:
                self.__numerator, self.__denominator = (
                    (int(numerator_str)) * (-1), 
                    abs(int(denominator_str)))
            else:
                self.__numerator, self.__denominator = (
                    int(numerator_str), 
                    int(denominator_str))
        elif len(args) == 2:
            if (args[0] < 0 and args[1] < 0):
                self.__numerator = abs(args[0])
                self.__denominator = abs(args[1])
            elif (args[1] < 0):
                self.__numerator = (-1) * args[0]
                self.__denominator = abs(args[1])               
            else:
                self.__numerator = args[0]
                self.__denominator = args[1]                

        self.__ReduceFraction()

    def __GSD(self):
        temporary_numerator = self.__numerator
        temporary_denominator = self.__denominator

        while temporary_numerator:
            temporary_denominator, \
                temporary_numerator = (
                    temporary_numerator, 
                    temporary_denominator %
                    temporary_numerator)

        return abs(temporary_denominator)

    def __ReduceFraction(self):
        gsd = self.__GSD()

        if (gsd != 1):
            self.__numerator //= gsd
            self.__denominator //= gsd

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        return f"Fraction('{self.__numerator}/{self.__denominator}')"

    def numerator(self, *args):
        if len(args) == 0:
            if (self.__numerator < 0):
                return self.__numerator * (-1)
            else:
                return self.__numerator
        elif len(args) == 1:
            self.__numerator = args[0]

            self.__ReduceFraction()

    def denominator(self, *args):
        if len(args) == 0:
            return self.__denominator
        elif len(args) == 1:
            if (args[0] < 0):
                self.__numerator *= (-1)
                self.__denominator = args[0] * (-1)
            else:
                self.__denominator = args[0]
            
            self.__ReduceFraction()

    def __neg__(self):
        temporary = Fraction(self.__numerator * (-1), self.__denominator)
        return temporary


a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())
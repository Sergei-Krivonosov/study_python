'''
Прямоугольник
-
Создайте класс Rectangle, который принимает ширину и высоту
прямоугольника при создании и должен иметь соответствующие
атрибуты width и height (целые числа).
Создайте метод area(), который возвращает площадь прямоугольника.
Создайте метод perimeter(), который возвращает периметр
прямоугольника.
Пример:
rect = Rectangle(2, 4)
a = rect.area() # Вернул 8
p = rect.perimeter() # Вернул 12
'''


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(2, 4)
a = rect.area()
b = rect.perimeter()

print(a)
print(b)

'''
Автомобиль
Создайте класс Car, который принимает марку автомобиля (make) в виде
строки и максимально возможную скорость (max_speed) в виде целого
числа при создании. Также при инициализации (в теле __init__)
экземпляра Car должен быть автоматически создан атрибут speed,
равный 0 (текущая скорость автомобиля). Подсказка: для speed в init
можно написать так self.speed = 0
Создайте метод display_speed(), который выводит в консоль текущую
скорость автомобиля.
Создайте метод accelerate(), который увеличивает скорость автомобиля
на 10, при этом скорость автомобиля не должна превышать max_speed,
если вызывается accelerate() при максимальной скорости, то скорость не
должна увеличиваться.
Создайте метод brake(), который уменьшает скорость автомобиля на 10,
при этом скорость автомобиля не может быть меньше 0. Если
вызывается метод brake() при скорости равной 0, то скорость не должна
уменьшаться.
Пример:
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed() # вывел в консоль 30
'''

class Car:
    def __init__(self, make, max_speed):
        self.make = make
        self.max_speed = max_speed
        self.speed = 0

    def display_speed(self):
        print(self.speed)

    def accelerate(self):
        if self.speed + 10 >= self.max_speed:
            self.speed += 0
        else:
            self.speed += 10

    def brake(self):
        if self.speed - 10 >= 0:
            self.speed -= 10

my_toyota = Car('Toyota', 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.brake()

my_toyota.display_speed()
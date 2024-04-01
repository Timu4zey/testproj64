class Shape:
    def size(self, a, b):
        pass


class Квадрат(Shape):
    def size(self, a, b):
        return a * a


class Прямоугольник(Shape):
    def size(self, a, b):
        return a * b


class Circle(Shape):  # Добавлено ключевое слово class
    def size(self, a, b):  # Исправлена ошибка в аргументах
        return a * a * 3.14  # Исправлено значение числа пи и умножение


def square_size(shape):
    print(shape.size(shape.a, shape.b))


квадрат = Квадрат()
прямоугольник = Прямоугольник()
квадрат.a, квадрат.b = 10, 10
прямоугольник.a, прямоугольник.b = 10, 20

square_size(квадрат)
square_size(прямоугольник)

круг = Circle()
круг.a, круг.b = 55, 55
square_size(круг)


class pararalepipet:
    def Sqwer(self, a, b, c):
        pass


class pippp(pararalepipet):
    def Sqwer(self, a, b, c):
        return a * b * c


def square_Sqwer(Sqwer_instance):
    return Sqwer_instance.Sqwer(Sqwer_instance.a, Sqwer_instance.b, Sqwer_instance.c)


pippp_instance = pippp()
pippp_instance.a, pippp_instance.b, pippp_instance.c = 3, 4, 5
result = square_Sqwer(pippp_instance)
print(result)







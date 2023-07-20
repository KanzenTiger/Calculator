d = str(input("Введите действие, которое хотите совершить из ниже пеоечисленны, \n +, -, /, *"))
try:#если нет типого исключения
    a = float(input("Введите число: "))
    b = float(input("Введите число: "))
    class Calculator():
        def __init__(self, a, b):
            self.alpha = a
            self.beta = b
        def calculating_P(self, alpha, beta):
            """Данная функция выполняет вычисления сложения"""
            c = alpha + beta
            return c
        def calculating_M(self, alpha, beta):
            """Данная функция выполняет вычисления вычитания"""
            c = alpha - beta
            return c
        def calculating_R(self, alpha, beta):
            """Данная функция выполняет вычисления деления"""
            c = alpha / beta
            return c
        def calculating_U(self, alpha, beta):
            """Данная функция выполняет вычисления умножения"""
            c = alpha * beta
            return c
    calculator = Calculator(a, b)
    #print(calculator.)
except ValueError:#если есть исключение типовое
    print("Ошибка, вы ввели слово")

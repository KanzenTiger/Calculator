first_operand = float(input("Введите 1 число: "))
second_operand = float(input("Введите 2 число: "))
action = str(input("(+)Сложить (-)Вычесть (/)Разделить (*)Умножить\nВыберите действие: "))

class Calculate():
    def __init__(self, a, b, action):        
        if action == '+':
            result = self.addiction(a, b)

        elif action == '-':
            result = self.subtraction(a, b)

        elif action in ('/', ':'):
            result =  self.division(a, b)

        elif action in ('*', 'x', 'X'):
            result =  self.multiplication(a, b)

        else:
            raise ValueError('Действие не поддерживается.')

        print('Результат:', int(result) if int(result) == result else result)

    def addiction(self, a, b):
        """Данная функция выполняет вычисления сложения"""
        c = a + b
        return c

    def subtraction(self, a, b):
        """Данная функция выполняет вычисления вычитания"""
        c = a - b
        return c

    def division(self, a, b):
        """Данная функция выполняет вычисления деления"""
        c = a / b
        return c

    def multiplication(self, a, b):
        """Данная функция выполняет вычисления умножения"""
        c = a * b
        return c

Calculate(first_operand, second_operand, action)

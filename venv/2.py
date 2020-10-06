class MyOwnException(Exception):
    def __init__(self, txt):
        self.txt = txt

x = input("Введите первое число: ")
y = input("Введите второе число: ")
try:
    x = int(x)
    y = int(y)
    if y==0:
        raise MyOwnException("Делить на ноль нельзя!")
    c = x / y
except ValueError:
    print("Введите число!")
except MyOwnException as err:
    print(err)
else:
    print(f"Результат деления {x}:{y} = {round(c,3)}")
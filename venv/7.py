class ComplexNum:
    def __init__(self, num, compl):
        self.num = num
        self.compl = compl

    def __str__(self):
        if self.compl<0:
            return f'Комплексное число: {self.num}{self.compl}i'
        return f'Комплексное число: {self.num}+{self.compl}i'

    def __add__(self, other):
        if (self.compl + other.compl) < 0:
            return f'Результат сложения:  {self.num + other.num}{self.compl + other.compl}i'
        return f'Результат сложения:  {self.num + other.num}+{self.compl + other.compl}i'

    def __mul__(self, other):
        if (self.num * other.compl + other.num * self.compl) < 0:
            return f'Результат умножения: {self.num * other.num - self.compl * other.compl}{self.num * other.compl + other.num * self.compl}i'
        return f'Результат умножения: {self.num * other.num - self.compl * other.compl}+{self.num * other.compl + other.num * self.compl}i'


n_1 = ComplexNum(4, -6)
n_2 = ComplexNum(6, 4)
print(n_1)
print(n_2)
print(n_1 + n_2)
print(n_1 * n_2)
class Data:
    def __init__(self, user_data):
        self.user_data = user_data
        user_data = str(user_data)

    @classmethod
    def extr(cls,user_data):
        user_data = list(user_data.split('-'))
        date = int(user_data[0])
        month = int(user_data[1])
        year = int(user_data[2])
        user_data = [date,month,year]
        return cls([date,month,year])

    @staticmethod
    def get_data(self):
        if self.user_data[0] > 31:
            print("Невероно указано число!")
        elif self.user_data[1] > 13:
            print("Неверно указан месяц!")
        elif self.user_data[2] > 2099 and self.user_data[2] < 1800:
            print("Неверно указан год!")
        else:
            return f'Число: {self.user_data[0]} \nМесяц: {self.user_data[1]} \nГод: {self.user_data[2]}'




data_1 = Data.extr('12-4-1991')
print(Data.get_data(data_1))
#data_1 = Data('12-04-1991')
#print(data_1.user_data)
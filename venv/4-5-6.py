class Warehouse:
    def __init__(self):
        self.all_tovar = []


    def add_new(self, info):
        self.all_tovar.append(Equipment(info))

    def __str__(self):
        return self.all_tovar



class Equipment:
    def __init__(self, name, color, article, cost ):
        self.info = {"Name":name,"Color":color,"Article":article,"Price":cost}

    @staticmethod
    def relev(self):
        if self.name=='1':
            self.name = 'Принтер'
            return self.name
        elif self.name=='2':
            self.name = 'Сканер'
            return self.name
        else:
            print("Error!")

class Printer(Equipment):
    def __init__(self, color_range, print_speed):
        self.color_range = color_range
        self.print_speed = print_speed
        super().__init__(color, article, cost)

class Scanner(Equipment):
    def __init__(self, scan_speed):
        self.scan_speed = scan_speed
        super().__init__(color, article, cost)

class Xerox(Equipment):
    def __init__(self, format):
        super().__init__(color, article, cost)
        self.format = format



p_1 = Equipment('1','red',463572,330)
print(Equipment.relev(p_1))

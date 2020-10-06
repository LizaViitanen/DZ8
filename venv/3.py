class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    user_list = input("Введите число для заполнения списка, для завершения введите q: ")
    try:
        if user_list.isdigit() == False:
            if user_list == 'q':
                print(f"Ваш список готов:\n {my_list}")
                break
            raise MyOwnError("Необходимо ввести число!")
    except MyOwnError as err:
        print(err)
    else:
        user_list = int(user_list)
        my_list.append(user_list)

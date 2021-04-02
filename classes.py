class Visitors:

    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def get_list(self):
        return print(f"Посетитель {self.name}, г. {self.city}, статус `{self.status}`")


class Clients(Visitors):

    def __init__(self, name, city, status):
        super().__init__(name, city, status)

    def get_list(self):
        return print(f"Клиент {self.name}, г. {self.city}, статус `{self.status}`")



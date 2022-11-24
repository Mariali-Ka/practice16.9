class Customers:
    def __init__(self, Family, Name, city, balance):
        self.family = Family
        self.name = Name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''"{self.family} {self.name}. {self.city}. Баланс: {self.balance} руб."'''

    def get_guest(self):
        return f'{self.family} {self.name}, г.{self.city}'


customer_1 = Customers('Иван','Петров','Москва',50)
customer_2 = Customers('Владимир','Зайцев','Кострома',50)
customer_3 = Customers('Олеся','Янина','Новосибирск',50)

guest_list=[customer_1, customer_2, customer_3]


for guest in guest_list:
    print(guest.get_guest())
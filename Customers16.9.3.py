class Customers:
    def __init__(self, Family, Name, city, balance):
        self.family = Family
        self.name = Name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''"{self.family} {self.name}. {self.city}. Баланс: {self.balance} руб."'''


customer_1 = Customers('Иван', 'Петров', 'Москва', 50)
print(customer_1)
from uuid import uuid4
import datetime as dt
from db import clients
from db import partners
""" A lot of changes this is only basic sheet"""
class Bike:
    def __init__(self,age, manufacturer, bike_type):
        self.age = age
        self.manufacturer = manufacturer
        self.bike_type = bike_type



class Person:
    def __init__(self, name, age, email):
        self.id = uuid4()
        self.name = name
        self.age = age
        self.email = email



class Billing:
    def __init__(self):
        self.id = uuid4()
        self.date = dt.datetime
        self.state = "pending"

    def show_bill(self, pay_class: object):
        print(f" Dear Client {Person.name()} , "
              f"Total Amount will be : {pay_class.payment_by_type()} "
              f"{self.id} <===> {self.date}")

    def close_bill(self):
        closed_bills = []
        if self.state == "pending":
            self.state = "closed"
            closed_bills.append(self.state)
        else:
            print("Your bill is already payed")


class PayPerKm:
    def __init__(self, bike_type, derived_kms: float):
        self.derived_kms = derived_kms
        self.km_price = 0.2  # default bike type C
        self.bike_type = bike_type

    def payment_by_type(self, bike_type):
        if bike_type == "C":
            return self.derived_kms * self.km_price
        elif bike_type == "B":
            return self.derived_kms * self.km_price * 1.5
        elif bike_type == "A":
            return self.derived_kms * self.km_price * 1.9
        elif bike_type == "S":
            return self.derived_kms * self.km_price * 2.2
        else:
            raise ValueError("Unknown bike type")


class PayPerDay:
    def __init__(self, bike_type, days_spent: int):
        self.days_spent = days_spent
        self.day_price = 9  # default bike type C
        self.bike_type = bike_type

    def payment_by_type(self, bike_type):
        if bike_type == "C":
            return self.days_spent * self.day_price
        elif bike_type == "B":
            return self.days_spent * self.day_price * 1.2
        elif bike_type == "A":
            return self.days_spent * self.day_price * 1.4
        elif bike_type == "S":
            return self.days_spent * self.day_price * 1.7
        else:
            raise ValueError("Unknown bike type")


class PayPerHour:
    def __init__(self, bike_type, derived_hours: float):
        self.derived_hours = derived_hours
        self.hour_price = 0.9  # default bike type C
        self.bike_type = bike_type

    def payment_by_type(self, bike_type):
        if bike_type == "C":
            return self.derived_hours * self.hour_price
        elif bike_type == "B":
            return self.derived_hours * self.hour_price * 1.3
        elif bike_type == "A":
            return self.derived_hours * self.hour_price * 1.6
        elif bike_type == "S":
            return self.derived_hours * self.hour_price * 1.9
        else:
            raise ValueError("Unknown bike type")


class RentManagement:
    def __init__(self):
        self.returned = False


    def rent(self):
         pass



class ClientManagement(Person):
    def __init__(self,name, age, email,rented_bike)
        super().__init__()
        self.ranted_bike = rented_bike
    def add_client(self):
        clients.append(repr(Person(self.name,self.age,self.email)))



    pass


class PartnerManagement(Person):
    def __init__(self, name, age, email, owned_bike)
        super().__init__()
        self.owned_bike = owned_bike

    def add_partner(self):
        partners.append(repr(Person(self.name,self.age,self.email)))

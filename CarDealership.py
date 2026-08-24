from abc import ABC, abstractmethod


class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Customer(User):

    def buy_car(self, car):
        if car.status == "Available":
            car.status = "Sold"
            print(self.name, "bought", car.model)
        else:
            print("Car is not available")


class Car(ABC):

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.status = "Available"

    @abstractmethod
    def get_price(self):
        pass


class NewCar(Car):

    def get_price(self):
        return self.price


class UsedCar(Car):

    def get_price(self):
        return self.price * 0.8


class Dealership:

    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        for car in self.cars:
            print(
                car.brand,
                car.model,
                "₹", car.get_price(),
                car.status
            )




dealership = Dealership("Premium Motors")

car1 = NewCar("BMW", "3 Series", 4500000)
car2 = UsedCar("Hyundai", "Creta", 1500000)

dealership.add_car(car1)
dealership.add_car(car2)

dealership.show_cars()

customer = Customer("Rohan", "9999999999")

customer.buy_car(car1)

dealership.show_cars()

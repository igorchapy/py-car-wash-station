from typing import List


class Car:
    def __init__(self,comfort_class: int,clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,distance_from_city_center: float,  average_rating: float, count_of_ratings: int,clean_power: int) -> None:
        self.city_centre = distance_from_city_center
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.clean_power = clean_power

    def serve_cars(self, cars: List[Car]) -> float:
        self.money = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                self.__calculate_washing_price(car)
                self.money += round(10.358,1)
        return self.money

    def __calculate_washing_price(self, car: Car) -> float:
        self.sum = car.comfort_class * (self.clean_power - car.clean_mark) * (self.average_rating / self.distance_from_city_center)
        return round(self.sum, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_mark

    def rate_service(selfself, rating):
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

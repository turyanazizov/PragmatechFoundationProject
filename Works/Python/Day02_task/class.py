# Vehicle Name: School Volvo Speed: 180 Mileage: 12
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def info(self):
        print(f'Vehicle Name: {self.name} || Max Speed: {self.max_speed} || Mileage: {self.mileage}')
vehicle01=Vehicle('Mercedes',250,15)
vehicle02=Vehicle('Volvo',200,10)
vehicle01.info()
vehicle02.info()
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cars = [0] * 3
        self.capacities = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.cars[carType - 1] < self.capacities[carType - 1]:
            self.cars[carType - 1] += 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

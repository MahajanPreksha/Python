class Vehicle:

    def __init__(self, capacity):
        self.capacity = capacity
    
    def getFare(self):
        self.fare = self.capacity * 100
        return self.fare

class Bus(Vehicle):
    
    def __init__(self, capacity):
        super().__init__(capacity)

    def getFare(self):
        vehicle_fare = super().getFare()
        maintenace_fare = 0.1 * vehicle_fare
        total_fare = vehicle_fare + maintenace_fare
        return total_fare
    
vehicle1 = Vehicle(50)
print("Vehicle Fare:", vehicle1.getFare())

bus1 = Bus(50)
print("Bus Fare:", bus1.getFare())

'''Output:
Vehicle Fare: 5000
Bus Fare: 5500.0
'''
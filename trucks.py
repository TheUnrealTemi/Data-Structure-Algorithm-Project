from datetime import timedelta, datetime

class Truck:
    def __init__(self, truck_id, capacity=16, speed=18, start_address="Hub", start_time=datetime(2020, 1, 1, 8, 0)):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed 
        self.packages = []  # holds Package objects
        self.mileage = 0.0
        self.address = start_address
        self.start_time = start_time
        self.current_time = start_time
        self.route = []  # list of addresses visited

    def load_package(self, package):
        """Load a package if capacity allows"""
        if len(self.packages) < self.capacity:
            self.packages.append(package)
            return True
        return False

    def add_miles(self, miles):
        """Update mileage and time based on truck speed"""
        self.mileage += miles
        hours = miles / self.speed
        self.current_time += timedelta(hours=hours)

    def __str__(self):
        return (f"Truck {self.truck_id}: {len(self.packages)} packages loaded, "
                f"Miles Driven: {self.mileage:.2f}, "
                f"Current Location: {self.address}, "
                f"Current Time: {self.current_time.strftime('%H:%M')}")


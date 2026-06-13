import datetime

class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, note):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.departure_time = None
        self.delivery_time = None
        self.status = "At Hub"
        self.truck_id = None
        
    def update(self, current_time):
        """Updates package status based on the given current time, 
        handling delivery times, address corrections, and special delays"""

        # Special times
        correction_time = datetime.datetime(2025, 1, 1, 10, 20)
        delayed_time = datetime.datetime(2025, 1, 1, 9, 5)
        delayed_packages = {6, 25, 28, 32}

        #Handle address correction for package 9
        if self.id == 9:
            if current_time < correction_time:
                self.address = "300 State St"
                self.city = "Salt Lake City"
                self.state = "UT"
                self.zipcode = "84103"
                self.note = "Wrong address listed"
            else:
                self.address = "410 S State St"
                self.city = "Salt Lake City"
                self.state = "UT"
                self.zipcode = "84111"
                self.note = "Address corrected at 10:20 am"

        #Handle delayed flight packages
        if self.id in delayed_packages and current_time < delayed_time:
            self.status = f"Delayed"
            return
        
        """Update package status based on a datetime object"""
        if self.delivery_time and self.delivery_time <= current_time:
            self.status = "Delivered"
        elif self.departure_time and self.departure_time <= current_time:
            self.status = "En Route"
        else:
            self.status = "At Hub"
         
    def __str__(self):
        return (f"Package {self.id}: {self.address}, {self.city}, {self.state}, {self.zipcode}, "
                f"Deadline: {self.deadline}, Weight: {self.weight}kg, "
                f"Status: {self.status}, Delivery Time: {self.delivery_time}, Delivered by Truck: {self.truck_id if self.truck_id else 'N/A'}")
        
    def __repr__(self):
        return (f"Package(id={self.id}, address='{self.address}', city='{self.city}', "
            f"state='{self.state}', zipcode='{self.zipcode}', deadline='{self.deadline}', "
            f"weight={self.weight}, note='{self.note}', status='{self.status}', "
            f"departure_time={self.departure_time}, delivery_time={self.delivery_time})")
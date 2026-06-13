# Student ID: 011336027

import csv
import datetime
from hash_table import HashTable
from package import Package
from trucks import Truck

#-------LOAD CSV FILES-------
# Read and store the distance data from the CSV file into a list of lists
with open("distances.csv") as distance_csv:
    distance_file = list(csv.reader(distance_csv))
    
# Read and store the address data from the CSV file into a list of lists
with open("addresses.csv") as address_csv:
    address_file = list(csv.reader(address_csv))

#Create an empty hash table to store the package data
hash_table = HashTable()


#-------HELPER FUNCTIONS-------
#Load Packages
def load_package(filename, hash_table):
    """Reads package data from a csv file, creates package objects for each entry, 
    and inserts them into the hash table"""
    with open(filename, encoding='utf-8-sig') as package_csv:
        package_data = csv.reader(package_csv)
        
        for package in package_data:
            #Extract each field from the csv
            id = int(package[0].strip('\ufeff'))
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline = package[5]
            weight = package[6]
            note = package[7]

            # Create a package object using the data extracted
            package = Package(id, address, city, state, zipcode, deadline, weight, note)

            # Store the created package object inside the hash table 
            hash_table.insert(package)

#Calculate Distance
def distance_in_between(i, j):
    """Return distance between two addresses using their index positions in the distance matrix"""
    distance = distance_file[i][j]
    if distance == '':
        distance = distance_file[j][i]
    return float(distance)

#Extract Address Index
def extract_address(address):
    """Find the index of a given street address from the address CSV. 
    This index corresponds to the correct row/column in the distance matrix"""
    for i, row in enumerate(address_file):
        if address.strip().lower() == row[1].strip().lower():
            return i
    raise ValueError(f"Address not found: {address}")


#-------NEAREST NEIGHBOR ALGORITHM-------
def deliver_packages(truck):
    """the delivery process for a given truck susing the Nearest Neighbor algorithm.
    The goal is to minimize total travel distance by always delivering to 
    the closest next address from the trucks current location"""
    
    #Retrieve all packages currently assigned to the truck
    not_delivered = [hash_table.lookup(id) for id in truck.packages]
    #Clear the trucks package list, it will be refilled in delivery order
    truck.packages.clear()

    #Continue delivering until all packages are delivered
    while not_delivered:
        nearest_package = None
        shortest_distance = float("inf")
        
        #Compare distance between the trucks current location and each undelivered package
        for package in not_delivered:
            dist = distance_in_between(extract_address(truck.address), extract_address(package.address))
            if dist < shortest_distance:
                shortest_distance = dist
                nearest_package = package
                
        #Deliver the nearest package next
        truck.packages.append(nearest_package.id)
        not_delivered.remove(nearest_package)
                
        #Update truck mileage and address after delivery
        truck.add_miles(shortest_distance)
        truck.address = nearest_package.address
        
        #Record the delivery and depature times for the package
        nearest_package.delivery_time = truck.current_time
        nearest_package.departure_time = truck.start_time
        nearest_package.truck_id = truck.truck_id

def main():
#---------MAIN LOGIC---------
    # Load Package Data
    load_package("packages.csv", hash_table)


    # Initiate trucks
    truck1 = Truck(1, start_address="4001 South 700 East", start_time=datetime.datetime(2025, 1, 1, 8, 0))
    truck1.packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

    truck2 = Truck(2, start_address="4001 South 700 East", start_time=datetime.datetime(2025, 1, 1, 10, 20))
    truck2.packages = [3, 6, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]

    truck3 = Truck(3, start_address="4001 South 700 East", start_time=datetime.datetime(2025, 1, 1, 9, 5))
    truck3.packages = [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33]


    # Deliver packages
    deliver_packages(truck1)
    
    deliver_packages(truck2)

    # Truck 3 leaves after the first two finish
    truck3.start_time = min(truck1.current_time, truck2.current_time)
    deliver_packages(truck3)
    
#-------USER INTERFACE-------
    print("Western Governors University Parcel Service")

    try:
        #Ask the user for a time to check package status
        user_time = input("Enter a time (HH:MM) to check package status: ")
        #Convert user input to datetime
        start_date = datetime.datetime(2025, 1, 1)
        h, m = map(int, user_time.split(":"))
        current_time = start_date + datetime.timedelta(hours=h, minutes=m)
        
        #Ask if the user would like to check the status of a specific package, or all packages
        mode = input("Type 'specify' for a specific package, or 'all' to view all packages: ").lower()

        #If the user inputs 'specify', the program will ask for the Package ID and print the status of that package
        if mode == "specify":
            specific_id = int(input("Enter package ID: "))
            package = hash_table.lookup(specific_id)
            package.update(current_time)
            print(package)
        #If the user inputs 'all', the program will print the status of all packages
        elif mode == "all":
            for id in range(1, 41):
                package = hash_table.lookup(id)
                package.update(current_time)
                print(package)
        else:
            print("Invalid mode. Exiting.")

    except ValueError:
        print("Invalid input. Exiting.")
    
    #Print the milelage for each truck, and total of all trucks
    print(f"\nTruck 1 mileage: {truck1.mileage} miles\n")
    print(f"\nTruck 2 mileage: {truck2.mileage} miles\n")
    print(f"\nTruck 3 mileage: {truck3.mileage} miles\n")    
    print(f"\nTotal mileage for all trucks: {truck1.mileage + truck2.mileage + truck3.mileage:.2f} miles\n")     

#Call main
if __name__ == "__main__":
    main()
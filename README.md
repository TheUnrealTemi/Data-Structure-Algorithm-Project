# WGUPS Route Optimization and Delivery Simulation

## Overview

WGUPS Route Optimization and Delivery Simulation is a Python application that models and optimizes package deliveries for the Western Governors University Parcel Service (WGUPS).

The system uses data structures and routing algorithms to efficiently deliver 40 packages while satisfying delivery constraints, tracking package statuses in real time, and minimizing total mileage traveled across delivery trucks.

The project demonstrates algorithm design, object-oriented programming, route optimization, and simulation of real-world logistics operations.

---

## Business Problem

The Western Governors University Parcel Service (WGUPS) needed a reliable way to deliver packages on time while minimizing travel distance.

Challenges included:

* Package delivery deadlines
* Limited truck capacity
* Delayed package arrivals
* Incorrect delivery addresses
* Multiple trucks with limited drivers
* Mileage constraints

The goal was to ensure all packages were delivered on time while keeping the total distance traveled below 140 miles.

---

## Solution

This application simulates package delivery operations using:

* A custom hash table for package storage and lookup
* A nearest neighbor routing algorithm for route optimization
* Time-based package tracking
* Object-oriented design principles
* Delivery constraint management

The system calculates delivery routes, tracks package status throughout the day, and reports total mileage traveled by each truck.

---

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* Hash Tables
* Greedy Algorithms
* CSV Data Processing
* Route Optimization
* Logistics Simulation

---

## Project Architecture

```text
Package Data (CSV)
        │
        ▼
Custom Hash Table
        │
        ▼
Truck Assignment
        │
        ▼
Nearest Neighbor Algorithm
        │
        ▼
Route Optimization
        │
        ▼
Package Delivery Simulation
        │
        ▼
Status Tracking & Mileage Reporting
```

---

## Core Components

### Package Class

Represents individual delivery packages and stores:

* Package ID
* Address
* City
* State
* ZIP Code
* Deadline
* Weight
* Delivery Notes
* Status
* Delivery Time
* Assigned Truck

Responsibilities:

* Track package delivery status
* Handle delayed package scenarios
* Manage address corrections
* Provide package information to users

---

### Truck Class

Represents delivery trucks and manages:

* Truck capacity
* Current location
* Mileage traveled
* Delivery route
* Current time
* Assigned packages

Responsibilities:

* Load packages
* Track mileage
* Update delivery times
* Simulate truck movement

---

### Hash Table

Packages are stored in a custom hash table to provide efficient package lookup by package ID.

Benefits:

* Fast retrieval
* Constant-time average lookup complexity
* Scalable package management

---

## Routing Algorithm

### Nearest Neighbor Algorithm

The system uses a greedy nearest neighbor approach to determine delivery order.

Process:

1. Start at the hub.
2. Calculate distances to all undelivered package locations.
3. Select the nearest location.
4. Deliver the package.
5. Repeat until all packages have been delivered.

This approach minimizes travel distance while maintaining efficient delivery operations.

Pseudo Process:

```text
Current Location
        │
        ▼
Find Closest Undelivered Package
        │
        ▼
Deliver Package
        │
        ▼
Update Mileage & Time
        │
        ▼
Repeat Until Complete
```

---

## Delivery Constraints Handled

### Truck Capacity

Each truck is limited to a maximum of 16 packages.

### Delayed Packages

Certain packages cannot leave the hub until 9:05 AM.

Examples:

* Package 6
* Package 25
* Package 28
* Package 32

### Address Correction

Package 9 contains an incorrect address that becomes available at 10:20 AM.

Before 10:20 AM:

```text
300 State St
```

After 10:20 AM:

```text
410 S State St
```

### Driver Availability

Only two drivers are available for three trucks.

Truck 3 departs only after one of the first two trucks returns.

---

## User Features

### Package Status Lookup

Users can query package status at any point during the day.

Example:

```text
Enter a time (HH:MM):
09:30
```

The application returns:

* Package information
* Current status
* Delivery time
* Assigned truck

### View All Packages

Users can view the status of all packages at a selected time.

Possible statuses:

* At Hub
* Delayed
* En Route
* Delivered

### Mileage Reporting

The application reports:

* Truck 1 mileage
* Truck 2 mileage
* Truck 3 mileage
* Total system mileage

---

## Time Complexity

### Package Lookup

Hash Table Lookup:

```text
Average Case: O(1)
```

### Route Selection

Nearest Neighbor Search:

```text
O(n²)
```

Where n is the number of packages assigned to a truck.

This tradeoff provides a simple and effective routing solution for the project requirements.

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/TheUnrealTemi/Route-Optimization-and-Delivery-Simulation-System.git
cd route-optimization-and-delivery-system
```

### Run Application

```bash
python main.py
```

### Required Files

* packages.csv
* addresses.csv
* distances.csv

---

## Example Output

```text
Western Governors University Parcel Service

Enter a time (HH:MM) to check package status:
13:00

Type 'specify' for a specific package, or 'all' to view all packages:
all
```

The application displays package statuses and delivery information for the selected time.
<img width="747" height="476" alt="Screenshot 2026-06-13 at 01 00 22" src="https://github.com/user-attachments/assets/725fd285-3361-4156-b063-35b9711c5efd" />

---

## Skills Demonstrated

### Algorithms

* Greedy Algorithms
* Route Optimization
* Nearest Neighbor Search

### Data Structures

* Hash Tables
* Lists
* Object Collections

### Software Engineering

* Object-Oriented Design
* Modular Architecture
* Code Organization
* Simulation Development

### Problem Solving

* Constraint-Based Routing
* Time-Based State Management
* Logistics Optimization

---

## Key Outcomes

* Successfully optimized delivery routes using a nearest neighbor algorithm
* Simulated real-world package delivery operations
* Tracked package statuses throughout the delivery lifecycle
* Managed delivery constraints including delayed packages and address corrections
* Maintained efficient package retrieval through hash table implementation

---

## Future Enhancements

* Implement Dijkstra's Algorithm or A* for route optimization
* Dynamic package assignment
* Interactive route visualization
* Web-based dashboard
* GPS integration
* Real-time traffic considerations
* Automated route balancing between trucks

---

## Author

Temitope Otunbanjo

Bachelor of Science, Computer Science
Western Governors University

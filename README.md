<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg)" alt="logo" width="300px" style="margin-top: 20px;"/>

# Logistics App

## Description
The app is used by large Australian company to manage the delivery of packages between hubs in major Australian cities. It can record the details of a delivery package, create or search for suitable delivery routes, and inspect the current state of delivery packages, transport vehicles and delivery routes. 

## Functionalities 
The application can support the following operations:
-	Creating a delivery package – unique id, start location, end location and weight in kg, and contact information for the customer.
- Creating a delivery route, the first location is the starting location – it has a departure time. The other locations have expected arrival time.
-	Search for a route based on package’s start and end locations.
-	Updating a delivery route – assign a free truck to it. 
-	Updating a delivery route – assign a delivery package.
-	View an information about routes, packages and trucks.

## Commands and User Manual 
Examples of all commands with output when the command is executed successfully and when an error occurs.
### add_pack_to_route
This command adds a package to a route, if a truck is added to this route and if the package is not already assigned to this route. It accepts package id and truck id.
Example input:
```
addpacktoroute 1 101
```
Example output:
```
-----------------------
Package №: 1 was added successfuly
```
Example output when an error ocures:
```
-----------------------
Package with ID: 2 can't be find!
```

### add_package
This command adds a package to a waiting list to be added to a route. It accepts start location, end location, package weight, customer first, last name and email.
Example input:
```
addpackage Sydney Melbourne 4000 David Bechkam dave@abv.bg
```
Example output:
```
-----------------------
Package #1 with weight 4000.0 was added to the waiting list.
```

### add_route
This command adds a route form a start location to an end location. It can accept locations between the start and the end location, as well. There must be a date and time in the format in the example input.
Example input:
```
addroute 20240218T0255 Sydney Melbourne Adelaide
```
Example output:
```
-----------------------
Route #101 from Sydney created.
```
Example output when city dosn't exists:
```
-----------------------
The city Sofia does not exist
```

### assign_truck
This command assigns truck to a given route. It accepts the name of the truck and the id of the route.
Example input:
```
assigntruck Man 101
```
Example output:
```
-----------------------
Truk Man with ID:1011 was assigned to route #101
```
Example output when truck is assigned:
```
-----------------------
Truck is already assign to this route!
```

### check_route
This commang checks if there is any routes, that are passing between two cities. 
Example input:
```
checkroute Melbourne Adelaide
```
Example output:
```
-----------------------
Sydney (Feb 18 02:55h) → Melbourne (Feb 18 12:59h) → Adelaide (Feb 18 21:19h)
```
Example output when there is no routes:
```
-----------------------
There is not a route from Sydney to Perth
```

### find_package
This command gives information about the package by its id
Example input:
```
findpackage 1
```
Example output:
```
-----------------------
Package: #1
Created on: Feb 19 11:32h
From: Sydney
To: Melbourne
Weight: 4000.0
Status: Unassign
Still in the hub. Its not assign to route, yet!

Email with this information was send to dave@abv.bg
```
Example output when there is no package with that id:
```
-----------------------
Package with ID: 2 can't be find!
```

### login
This command awolls an employee to log in in the app. It acepts username and pasword 
Example input:
```
login dave 12345
```
Example output:
```
-----------------------
User dave successfully logged in!
```
Example output when employee is logged:
```
-----------------------
Employee dave is logged in! Please log out first!
```


### logout
This command logs out logged in users.
Example input:
```
logout
```
Example output:
```
-----------------------
You logged out!
```
Example output when you are not logged in:
```
-----------------------
You are not logged in! Please login first!
```

### register_employee
This command registers an employee in the system. It takes username, first and last name and a password.
Example input:
```
registeremployee dave David Bechkam 12345
```
Example output:
```
-----------------------
User dave registered successfully!
```
Example output when username already exists:
```
-----------------------
User dave already exist. Choose a different username!
```

### remove_package
This command removes a package from a route. It takes package id and route id.
Example input:
```
removepackfromroute 1 101
```
Example output:
```
-----------------------
Package #1 with weight 4000,0 was removed from route #101
```
Example output when there is no such package:
```
-----------------------
Package with ID: 2 can't be find!
```

### show_trucks_in
This command shows all trucks in a given location. 
Example input:
```
showtrucksin Melbourne
```
Example output:
```
-----------------------
Melbourne hup have total of standing trucks: 5
------------------------
Scania: 1
Man: 2
Actros: 2
```

### view_routes
This command shows all routes, that are in progress, current location and the distance untill the next location.
Example input:
```
viewroutes
```
Example output:
```
-----------------------
Route #116
Sydney (Feb 19 02:55h) → Melbourne (Feb 19 12:59h) → Adelaide (Feb 19 21:19h)
Total distance: 1602
Current locations: 86 km till Melbourne
```
Example output when there is no routes:
```
-----------------------
There is no routes in progress.
```

### view_unsent_packages
This command shows all packages, that are unsent and their start and end location.
Example input:
```
viewunsentpackages
```
Example output:
```
-----------------------
Start location: Sydney
 - Amount of packages: 1
 - Total weight: 4000.0
End locations:
 - Melbourne (3)
```
Example output when there is no unsent packages:
```
-----------------------
No unsent packages found.
```
from abstract_vehicle import AbstractVehicle
from truck import Truck
from car import Car

 
 
 
 #The test_vehicle module is a python script that generates the following output:
  # Car: 2014 Toyota Camry in excellent condition with 50000 km.
   #Truck: 2018 Ford Explorer in fair condition with 5500 km.
   #Car: 2016 VW Jetta in perfect condition with 26100 km.
   #Truck: 1990 Ford Ranger in poor conditions with 350000 km. 

#print_report will print the details of the vehicles like the above example.
def print_report(vehicles):
    for vehicle in vehicles:
        print(vehicle.get_details())
    


def main():
    vehicles = []
    vehicles.append(Car("2014 Toyota Camry", "Camry", 2014, "excellent", 50000))
    vehicles.append(Truck("2018 Ford Explorer", "Explorer", 2018, "fair", 5500))
    vehicles.append(Car("2016 VW Jetta", "Jetta", 2016, "perfect", 26100))
    vehicles.append(Truck("1990 Ford Ranger", "Ranger", 1990, "poor", 350000))
    print_report(vehicles)


if __name__ == "__main__":
    main()

    



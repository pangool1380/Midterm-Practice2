from abstract_vehicle import AbstractVehicle

class Car(AbstractVehicle):
    def __init__(self, name, model, year, condition, distance_travelled, seats):
        """Initializes the Car class"""
        super().__init__(name, model, year, condition, distance_travelled)
        self.seats = seats

    def set_seats(self, seats):
        """Sets the seats of the car"""
        self.seats = seats

    def get_seats(self):
        """Returns the seats of the car"""
        return self.seats


    def get_details(self):
        """Returns a string with the details of the car"""
        return super().get_details() + " and has " + str(self.seats) + " seats."
     
      


        
 
       

    




  

   

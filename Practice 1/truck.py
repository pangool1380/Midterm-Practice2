from abstract_vehicle import AbstractVehicle


class Truck(AbstractVehicle):
    def __init__(self, name, model, year, color, max_speed, cargo_capacity):
        super().__init__(name, model, year, color, max_speed)
        self.cargo_capacity = cargo_capacity


    def set_cargo_capacity(self, cargo_capacity):
        """Sets the cargo capacity of the truck"""
        self.cargo_capacity = cargo_capacity

    def get_cargo_capacity(self):
        """Returns the cargo capacity of the truck"""
        return self.cargo_capacity

    def get_details(self):
        """Returns a string with the details of the truck"""
        return super().get_details() + " and has a cargo capacity of " + str(self.cargo_capacity) + "."

        
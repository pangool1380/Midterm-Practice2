class AbstractVehicle:
    #With constructors: name, model, year(int), color, max_speed(float)
    def __init__(self, name, model, year, condition, distance_travelled):
        """Initializes the AbstractVehicle class"""
        AbstractVehicle._validate_string(name)
        self.name = name
        AbstractVehicle._validate_string(model)
        self.model = model
        AbstractVehicle._validate_int(year)
        self.year = year
        AbstractVehicle._validate_string(condition)
        self.condition = condition
        AbstractVehicle._validate_int(distance_travelled)
        self.distance_travelled = distance_travelled


    #With setters: name, model, year(int), color, max_speed(float)
    def set_name(self, name):
        """Sets the name of the vehicle"""
        self.name = name

    def set_model(self, model):
        """Sets the model of the vehicle"""
        self.model = model

    def set_year(self, year):
        """Sets the year of the vehicle"""
        self.year = year


    def set_condition(self, condition):
        """Sets the condition of the vehicle"""
        self.condition = condition

    def set_distance_travelled(self, distance_travelled):
        """Sets the distance travelled of the vehicle"""
        self.distance_travelled = distance_travelled

    #With getters: name, model, year(int), ...
    def get_name(self):
        """Returns the name of the vehicle"""
        return self.name

    def get_model(self):
        """Returns the model of the vehicle"""
        return self.model

    def get_year(self):
        """Returns the year of the vehicle"""
        return self.year

    def get_condition(self):
        """Returns the condition of the vehicle"""
        return self.condition

    def get_distance_travelled(self):
        """Returns the distance travelled of the vehicle"""
        return self.distance_travelled

    def get_details(self):
        """Returns a string with the details of the vehicle"""
        #Example: 2014 Toyota Camry in excellent condition with 50000 km.
        #Example: 2018 Ford Explorer in fair condition with 10000 km.
        return int(self.year) + " " + self.model + " in " + self.condition + " condition with " + int(self.distance_travelled) + " km."

    @staticmethod
    def _validate_string(label, value):
        """Validates that the value is a string"""
        if not isinstance(value, str):
            raise ValueError(label + " must be a string")


    @staticmethod
    def _validate_int(label, value):
        """Validates that the value is an integer"""
        if not isinstance(value, int):
            raise ValueError(label + " must be an integer")


        

    

        
# Define 5 of your favorite vehicles
# Move all common properties in your vehicles to a new Vehicle class.
# Create a drive() method in the Vehicle class.

class Vehicle:
    def __init__(self, main_color, maximum_occupancy):
        self.main_color = main_color
        self.maximum_occupancy = maximum_occupancy

    def drive(self):
        print("vrooom!")

    def turn(self, direction):
        print(f"turn {direction}")

    def stop(self):
        print("The vehicle comes to a stop.")

class Tesla(Vehicle):
    def __init__(self, main_color, maximum_occupancy, battery_kwh):
        super().__init__(main_color, maximum_occupancy)
        self.battery_kwh = battery_kwh

    def drive(self):
        print(f"the {self.main_color} car goes zoooom'")

    def stop(self):
        print(f"The {self.main_color} vehicle comes to a stop.")

class Zero(Vehicle):
    def __init__(self, main_color, maximum_occupancy, battery_kwh):
        super().__init__(main_color, maximum_occupancy)
        self.battery_kwh = battery_kwh

    def drive(self):
        print("Zoooooooooooom!")

class Cessna(Vehicle):
    def __init__(self, main_color, maximum_occupancy, fuel_capacity):
        super().__init__(main_color, maximum_occupancy)
        self.fuel_capacity = fuel_capacity

    def drive(self):
        print("Zoooooooooooom!")


class Dodge(Vehicle):
    def __init__(self,  main_color, maximum_occupancy, fuel_capacity):
        super().__init__(main_color, maximum_occupancy)
        self.fuel_capacity = fuel_capacity

    def drive(self):
        print("Zoooooooooooom!")

class BMW(Vehicle):
    def __init__(self, main_color, maximum_occupancy, fuel_capacity):
        super().__init__(main_color, maximum_occupancy)
        self.fuel_capacity = fuel_capacity

    def drive(self):
        print("Zoooooooooooom!")



# Create an instance of each vehicle.

modelS = Tesla('White', 5, 350)
zeroFXS = Zero('Red', 2, 100)
cessna182 = Cessna('Blue', 10, 500)
ram = Dodge('Orange', 5, 100)
m2 = BMW('Purple', 5, 75)

# modelS.drive()
# modelS.turn("right")
# modelS.stop()

# zeroFXS.drive()
# zeroFXS.turn("right")
# zeroFXS.stop()

# cessna182.drive()
# cessna182.turn("right")
# cessna182.stop()

# ram.drive()
# ram.turn("right")
# ram.stop()

# m2.drive()
# m2.turn("right")
# m2.stop()

















# Define a different value for each vehicle's properties.





# Define a different value for each vehicle's properties.



# Create a drive() method in the Vehicle class.

# Override the drive() method in all the other vehicle classes. 
# Include the vehicle's color in the message (i.e. "The blue Ram drives past.
#  RRrrrrrummbbble!").

# Create a turn(self, direction) method, and a stop(self) method on Vehicle. 
# Define a basic implementation of each.

# Override all three of those methods on some of the vehicles.
#  For example, the stop() method for a plane would be to output the message
# "The white Cessna rolls to a stop after rolling a mile down the runway."


# Make your vehicle instances perform all three behaviors.
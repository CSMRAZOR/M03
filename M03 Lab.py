# M03 Lab - Case Study: Lists, Functions, and Classes
# Owen Mills 04/03/2024

class Vehicle:
    # Define vehicle type
    def __init__(self):
        self.vehicle_type = ""

    # Set the vehicle type
    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    # Show vehicle type to user
    def display_information(self):
        print("Vehicle type:", self.vehicle_type)

class Automobile(Vehicle):
    def __init__(self):

        # Call parent class
        super().__init__()

        # Define attributes for Autombile
        self.make = ""
        self.model = ""
        self.year = ""
        self.doors = ""
        self.roof = ""

    # Set Automobile information
    def set_info(self, make, model, year, doors, roof):
        self.make = make
        self.model = model
        self.year = year
        self.doors = doors
        self.roof = roof

    def display_information(self):

        # Call display_information method
        super().display_information()

        # Show infomation
        print("Make:" ,self.make)
        print("Model:" ,self.model)
        print("Year:", self.year)
        print("Doors:" ,self.doors)
        print("Roof:" ,self.roof)

def main():

    # Make car = Automobile
    car = Automobile()

    # Set vehicle type
    car.set_vehicle_type("car")

    # Get var information form the user
    make = input("Make of the car: ")
    model = input("Model of the car: ")
    year = input("Year of the car: ")

    # Check to make sure either 2 or 4 was entered for the amount of doors
    while True:
        doors = input("How many doors the car has (2 or 4): ")
        if doors in ['2', '4']:
            break
        else:
            print("Please enter 2 or 4 for the number of doors the car has.")

    # Check to make sure either solid or sun roof was entered for the roof
    while True:
        roof = input("What kind of roof (solid or sun roof): ")
        if roof in ['solid', 'sun roof']:
            break
        else:
            print("Please enter (solid) or (sun roof)")

    #Set car information
    car.set_info(make, model, year, doors, roof)

    #Display the cars information
    print("\nCar Information:")
    car.display_information()

if __name__ == "__main__":
    main()



# 03_class_attributes_property.py
# Lesson 03: Class Attributes vs Instance Attributes + @property Decorator
# Goal: Understand shared (class) vs unique (instance) data, and how @property
# makes methods behave like attributes for cleaner, safer code.

class Car:
    # CLASS ATTRIBUTE: Shared by ALL Car objects (like a global constant for the class).
    # Changing this affects every existing and future Car instance.
    wheels = 4                  # Every car has 4 wheels — shared knowledge
    manufacturer = "AutoCorp"   # All cars made by the same fictional company

    def __init__(self, make, model, year, mileage=0):
        # INSTANCE ATTRIBUTES: Unique to THIS specific car object.
        # Each Car can have completely different values here.
        self.make = make
        self.model = model
        self.year = year
        self._mileage = mileage     # Private by convention (underscore prefix)

    # INSTANCE METHOD: Works on this specific car's data (uses self).
    def drive(self, miles):
        self._mileage += miles
        print(f"Drove {miles} miles. Total mileage now: {self._mileage}")

    # PROPERTY (getter): Makes a method look and feel like a regular attribute.
    # Users can do car.mileage instead of car.get_mileage()
    @property
    def mileage(self):
        """Read-only access to mileage."""
        return self._mileage

    # SETTER: Controls how the 'mileage' attribute is changed.
    # Prevents invalid values (e.g., decreasing mileage).
    @mileage.setter
    def mileage(self, value):
        if value < self._mileage:
            raise ValueError("Mileage cannot decrease!")
        self._mileage = value
        print(f"Mileage updated to: {value}")

    # CLASS METHOD: Operates on the class itself, not an instance.
    # Use when you want to change shared class data.
    @classmethod
    def change_manufacturer(cls, new_name):
        cls.manufacturer = new_name
        print(f"All cars now made by: {new_name}")

    # STATIC METHOD: Just a regular function inside the class (no self or cls).
    # Useful for utility/helper functions related to cars.
    @staticmethod
    def is_valid_year(year):
        return 1886 <= year <= 2100  # Cars were invented around 1886


# === Examples & Expected Results ===

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022, 50000)

# Instance attributes are unique
print(f"Car1: {car1.make} {car1.model}, Year: {car1.year}")
# Expected: Car1: Toyota Camry, Year: 2020

print(f"Car2: {car2.make} {car2.model}, Year: {car2.year}")
# Expected: Car2: Honda Civic, Year: 2022

# Class attributes are shared
print(f"All cars have {Car.wheels} wheels")
# Expected: All cars have 4 wheels

print(f"Car1 manufacturer: {car1.manufacturer}")
print(f"Car2 manufacturer: {car2.manufacturer}")
# Both show "AutoCorp" (shared)

# Drive method (instance method)
car1.drive(100)
# Expected: Drove 100 miles. Total mileage now: 100

print(f"Car1 mileage (via @property): {car1.mileage}")
# Expected: Car1 mileage (via @property): 100

# Property setter with validation
car1.mileage = 200
# Expected: Mileage updated to: 200

# Trying to decrease mileage raises error (uncomment to see):
# car1.mileage = 50  # → ValueError: Mileage cannot decrease!

# Class method changes shared data for everyone
Car.change_manufacturer("FutureMotors")
print(car1.manufacturer)  # Expected: FutureMotors
print(car2.manufacturer)  # Expected: FutureMotors

# Static method (no instance needed)
print(Car.is_valid_year(2025))  # Expected: True
print(Car.is_valid_year(1800))  # Expected: False

# Summary of expected full output when run:
# Car1: Toyota Camry, Year: 2020
# Car2: Honda Civic, Year: 2022
# All cars have 4 wheels
# Car1 manufacturer: AutoCorp
# Car2 manufacturer: AutoCorp
# Drove 100 miles. Total mileage now: 100
# Car1 mileage (via @property): 100
# Mileage updated to: 200
# All cars now made by: FutureMotors
# FutureMotors
# FutureMotors
# True
# Falsees_property.py
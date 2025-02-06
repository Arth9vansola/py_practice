# 1. polymorphism
# class Bird:
#     def speak(self):
#         return "Chirp"

# class Dog:
#     def speak(self):
#         return "Woof"

# # Using polymorphism
# def animal_sound(animal):
#     print(animal.speak())

# bird = Bird()
# dog = Dog()

# animal_sound(bird)  # Output: Chirp
# animal_sound(dog)   # Output: Woof


# 2.method overriding
# class Vehicle:
#     def fuel_type(self):
#         return "Petrol or Diesel"

# class ElectricCar(Vehicle):
#     def fuel_type(self):
#         return "Electricity"

# # Objects
# car1 = Vehicle()
# car2 = ElectricCar()

# print(car1.fuel_type())  # Output: Petrol or Diesel
# print(car2.fuel_type())  # Output: Electricity

# 3. operator overloading
# class Number:
#     def __init__(self, value):
#         self.value = value  # Assign value to the instance variable

#     def __add__(self, other):
#         return self.value + other.value  # Adding the values of two Number objects

# num1 = Number(10)
# num2 = Number(20)

# print(num1 + num2)  # Output: 30 ,,,,,,   calls internally num1.__add__(num2)


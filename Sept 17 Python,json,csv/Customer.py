# Parent class
class Vehicle:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
  
class Car(Vehicle):
	def __init__(self, brand, model, doors):
		# Call parent constructor
		super().__init__(brand, model)
		self.doors = doors

	def displayinfo(self):
		return f"Car: {self.brand} {self.model}, Doors: {self.doors}"


# Create object
v1 = Vehicle("Tata", "Truck")
c1 = Car("Ford", "Mustang", 4)

# Call methods
#print(v1.displayinfo())  # This will raise an AttributeError
print(c1.displayinfo())
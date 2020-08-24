
"""
Code: "UTF-8"
Author: "Akshata"
Language: Python ; version: 3.8.x
"""
"""
EXERCISE
Write and object oriented program that performs the following tasks:
1. Define a class called "Employee" and create an instance of that class
2. Create an attribute called name and assign it with a value
3. Change the name you previously defined within a method and call this method by making use of the object you created
"""

#Define class

class Employee:
	Name = "Ben"

	#define mothod
	def update_name(self):
		self.Name = "Ron"


#Instance of a class
employee1 = Employee()
print("Before name update: ",employee1.Name)
employee1.update_name()
print("After update: ", employee1.Name)

		
#define class
class rentcar:
	def __init__(self):
		self.cost = {'Hatchback':30,'Sedan':50,'SUV':100}

	def checkAvailability(self,key):
        if key in self.cost:
            print("Yes!, Car is available for rent")
        else:
            print("Sorry!, This car is not available. Please select another car")

	def displayFair(self):
		print("Cost per day: ")
		print("Hatchback: $",self.cost['Hatchback'])
		print("Sedan: $",self.cost['Sedan'])
		print("SUV: $",self.cost['SUV'])

	def calculateFair(self,key,days):
		return self.cost[key] * days

car = rentcar()
while True:
	print("Enter 1 to display available cars")
	print("Enter 2 to rent a car")
	print("Enter 3 to exit")
	customer_input=(int(input()))
	if customer_input ==1:
		car.displayFair()
	elif customer_input ==2:
		print("Please select car from available list")
		key = str(input())
		car.checkAvailability(key)
		print("How many days for rent?")
		days = int(input())
		TotalFair = car.calculateFair(key,days)
		print("Total fair for this rent: $",TotalFair)
	else:
		quit()

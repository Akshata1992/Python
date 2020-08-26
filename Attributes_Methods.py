"""
Code: "UTF-8"
Author: "Akshata"
Language: Python ; version: 3.8.x
"""

"""
EXERCISE

Write an object oriented program to create a precious stone. Not more than 5 precious stones can be held in possession at a given point of time. If there are more than 5 precious stones, delete the first stone and store the new one.

"""

#Define class

class precious_stone:
	numberOfPreciousStones = 0
	PreciousStoneCollection = []

	#Define method
	def __init__(self,name):
		self.name = name
		precious_stone.numberOfPreciousStones +=1

		if precious_stone.numberOfPreciousStones > 5:
			del precious_stone.PreciousStoneCollection[0]
		else:
			precious_stone.PreciousStoneCollection.append(self.name)

	def displayPreciousStones():
        for precious_stone in precious_stone.preciousStoneCollection:
            print(preciousStone.name, end = ' ')
        print()


#Instantiate
stone1 = precious_stone('Ruby')
stone2 = precious_stone('Emerald')
stone3 = precious_stone('Diamond')
stone4 = precious_stone('Onlyx')
stone5 = precious_stone('Amber')
#print(stone1.name)
stone6 = precious_stone('Sapphire')
#print(stone1.name)

GrassPosXMinMax = 8, 15
GrassPosYMax = 10

bushPosX = 9,10, 11
bushPosYMax = 5

PumpkinWidthXY = 8, 8

sunflowerPosY = get_world_size() - 2, get_world_size() - 1

treePosY = get_world_size() - 2 , get_world_size() - 1

def CheckPlantType(currentX, currentY):
	plantType = 0

	if (currentY == sunflowerPosY[0] or currentY == sunflowerPosY[1]) and currentX % 2 == 0:
		plantType = Entities.Sunflower
	elif (currentY == treePosY[0] or currentY == treePosY[1]) and currentX % 2 == 1:
		plantType = Entities.Tree
	elif currentX <= (PumpkinWidthXY[0] - 1) and currentY <= (PumpkinWidthXY[1] - 1):
		plantType = Entities.Pumpkin
	elif (currentX >= GrassPosXMinMax[0] and currentX <= GrassPosXMinMax[1] ) and currentY <= GrassPosYMax:
		plantType = Entities.Grass
	elif (currentX == bushPosX[0] or currentX == bushPosX[1] or currentX == bushPosX[2] ) and currentY <= bushPosYMax:
		plantType = Entities.Bush
	else:
		plantType = Entities.Carrot
		
	return plantType
	
def CheckPlantingPos(currentX, currentY, plantPosXMinMax, PlantPosYMinMax):
	a = 0
	
	

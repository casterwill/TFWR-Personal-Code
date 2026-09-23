import HarvestPlantMove
import CheckWhatToPlant

while True :
	currentX = get_pos_x()
	currentY = get_pos_y()
	currentXY = get_pos_x(), get_pos_y()
	
	plantType = CheckWhatToPlant.CheckPlantType(currentX, currentY)
	
	HarvestPlantMove.HarvestAndPlantAndMove(plantType, North, currentY)
	
	

	
		
			
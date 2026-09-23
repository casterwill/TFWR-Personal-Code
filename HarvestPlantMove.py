import CheckIfEnding 

def HarvestAndPlantAndMove(plantType, moveTo, currentY):

	if can_harvest() :
		harvest()
		
	if (plantType == Entities.Carrot or plantType == Entities.Pumpkin or plantType == Entities.Sunflower) and get_ground_type() != Grounds.Soil:
		till()
	if plantType == Entities.Grass and get_ground_type() != Grounds.Grassland:
		till()

	if plantType != Entities.Grass :
		plant(plantType)
	
	if num_items(Items.Fertilizer) != 0:
		a = 1
		#use_item(Items.Fertilizer)

	isEnding = CheckIfEnding.CheckIfEnding(currentY)
	
	if isEnding:
		return
	else:
		move(moveTo)
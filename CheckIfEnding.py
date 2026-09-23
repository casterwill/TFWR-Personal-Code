def CheckIfEnding(currentY):
	if currentY == (get_world_size() - 1):
		move(North)
		move(East)
		return True
	else:
		return False
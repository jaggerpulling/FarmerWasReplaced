def punkin():
	# if standing over all blocks and equal to pumpkling harvest
	while True:
		pumpkin_count = 0
		
		for i in range(get_world_size()):
			for i in range(get_world_size()):
				waterfunction()
				if get_ground_type() == Grounds.Grassland:
					till()
			
				if get_entity_type() == Entities.Pumpkin:
					pumpkin_count += 1
		
						if pumpkin_count != 6:
							plant(Entities.Pumpkin)
				else:
					harvest()
					
				move(North)
			move(East)
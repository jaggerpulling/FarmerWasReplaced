
	# if standing over all blocks and equal to pumpkling harvest
	while True:
		total_count = 0
		pumpkin_count = 0
		for i in range(get_world_size()):
		
			for i in range(2):
				for i in range(get_world_size()):
					
					#waterfunction()
					
					if get_ground_type() == Grounds.Grassland:
						till()
				
					if get_entity_type() == Entities.Pumpkin:
						pumpkin_count += 1
	
					if pumpkin_count != 72:
						plant(Entities.Pumpkin)
					else:
						harvest()
						pumpkin_count = 0
						
					if pumpkin_count >= 5:
						if get_entity_type() != Entities.Pumpkin:
							pumpkin_count -= 1
						
					move(North)
			move(East)
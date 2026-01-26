def pumpkinRow():
	bad_pumpkin = True
	
	while bad_pumpkin:
		bad_pumpkin = False #set default to false and continue if true
		
		for i in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				till()
				plant(Entities.Pumpkin)
			else:
				if get_ground_type() == Grounds.Soil and get_entity_type() != Entities.Pumpkin:
					plant(Entities.Pumpkin)
				
			#check for bad pumpkin, replant and toggle (bad pumpkin returns False)
			if can_harvest() != True:
				bad_pumpkin = True
						
			move(North)
		


MAX_DRONES = max_drones()
WORLD_SIZE = get_world_size()
def run():
	#spawn while moving east after allowing drone to finish	
	count = 0 #determine how many times moved 	
	done = False
	while done == False:
		if spawn_drone(pumpkinRow):
			move(East)
			count += 1
		else:
			pumpkinRow()
			move(East)
		
		#wait to finish while more than 1 drone
		if count == 12:
			while num_drones() != 1:
				do_a_flip()
			harvest()
			done = True

			
			

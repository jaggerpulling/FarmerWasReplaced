def punkin():
	# if standing over all blocks and equal to pumpkling harvest
	while True:
		world_size = get_world_size()

		#Checks and doesnt move from row until good
		for i in range(get_world_size()):
			move_count = 0
			bad_pumpkin_count = get_world_size() # set bad pumpkin count to all in the row

			while bad_pumpkin_count > 0:
				not_pumpkin = True
				#waterfunction()
				
				if get_ground_type() == Grounds.Grassland:
					till()
			
				if get_entity_type() == Entities.Pumpkin:
					bad_pumpkin_count -= 1 # subtract 1 for each good pumpkin
					
				# Run on first cycle only
				if move_count < get_world_size():
					plant(Entities.Pumpkin)
					if get_entity_type() == Entities.Pumpkin:
						use_item(Items.Fertilizer)
						use_item(Items.Fertilizer)
					
				#Keep planting pumpkin without passing until good
				if move_count > get_world_size():
					if not can_harvest():
						while not_pumpkin:
							if not can_harvest():
								plant(Entities.Pumpkin)
								use_item(Items.Fertilizer)
							else:
								bad_pumpkin_count -= 1
								not_pumpkin = False
					
					
				move(North)
				move_count += 1
			
			move(East)
		harvest()
		
punkin()
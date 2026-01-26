def checkercarrottree():
	while True:
		#y loop
		for i in range(get_world_size()):
			x = get_pos_x()
	
			#x loop
			for index in range(get_world_size()):
				if can_harvest():
					harvest()

				y = get_pos_y()
		
				if (x + y) % 2 == 0:   # even sum
					plant(Entities.Tree)
				else:                  # odd sum
					if get_ground_type() == Grounds.Grassland:
						till()
						plant(Entities.Carrot)
		
				move(North)
			move(East)
		
				
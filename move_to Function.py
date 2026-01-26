def move_to(x,y):

	while get_pos_x() != x and get_pos_y() != y:
		
		if get_pos_x() != x:
			if get_pos_x() < x:
				move(East)
			else:
				move(West)
		
		if get_pos_y() != y:
			if get_pos_y() < y:
				move(North)
			else:
				move(South) 

		
	  
move_to(0,0)
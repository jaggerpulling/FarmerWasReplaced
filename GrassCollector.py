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

def grasscollector():
		
		for i in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Sunflower)
			if can_harvest():
				harvest()
				plant(Entities.Sunflower)
			
			for i in range(get_world_size()):
				#waterfunction()
				
				if can_harvest():
					harvest()
					
				move(North)
			move(East)
while True:			
	spawn_drone(grasscollector)
	move(East)
	grasscollector()

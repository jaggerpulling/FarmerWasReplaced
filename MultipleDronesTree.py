import WaterFunction

def treecollector():
	for i in range(get_world_size()):
		x = get_pos_x()
		y = get_pos_y()
		
		if can_harvest():
			harvest()
		
		
		if (x + y) % 2 == 0:   # even sum
			plant(Entities.Tree)
			WaterFunction.waterfunction()
		else:                  # odd sum
			if get_ground_type() == Grounds.Grassland:
				till()
				plant(Entities.Carrot)
			else:
				plant(Entities.Carrot)	
		
		move(North)



max_drones = max_drones()
#set_world_size(max_drones)

def tree():
	
	for _ in range(get_world_size() * 3):
		if spawn_drone(treecollector):
			move(East)
		else:
			treecollector()
			move(East)
			

def carrotcollector():
	for i in range(get_world_size()):
		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Carrot)
			use_item(Items.Fertilizer)
		
		if can_harvest():
			harvest()
			plant(Entities.Carrot)	
			use_item(Items.Fertilizer)	
		
		move(North)



max_drones = max_drones()
#set_world_size(max_drones)

def carrot():
	
	for _ in range(get_world_size() * 2):
		if spawn_drone(carrotcollector):
			move(East)
		else:
			carrotcollector()
			move(East)
			

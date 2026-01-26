def grasscollector():
	for i in range(get_world_size()):
		harvest()
		move(North)



max_drones = max_drones()
#set_world_size(max_drones)

def grass():
	
	for _ in range(get_world_size()):
		if spawn_drone(grasscollector):
			move(East)
		else:
			grasscollector()
			move(East)
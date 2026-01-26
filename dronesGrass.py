def grasscollector():
	for i in range(get_world_size()):
		harvest()
		move(North)



max_drones = max_drones()
#set_world_size(max_drones)

def runningGrass():
	while True:
		for _ in range(max_drones):
			spawn_drone(grasscollector)
			move(East)
		grasscollector()	

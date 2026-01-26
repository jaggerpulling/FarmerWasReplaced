def sort_x():
	list = []
	
	for i in range(get_world_size()):
		list.append(measure())

		#avoid last bug, swapping over end
		if i == get_world_size():
			move(North)
			break
	
		#skip first
		if len(list) < 1:
			print(len(list))
			continue
		
		# if pcurrent is greater than future
		if list[i] < list[i-1]:
			swap(South)

			#swap list elements
			list[i], list[i - 1] = list[i - 1], list[i]
			
		move(North)

def sort_y():
	list = []
	
	for i in range(get_world_size()):
		list.append(measure())

		#avoid last bug, swapping over end
		if i == get_world_size():
			move(East)
			break
	
		#skip first
		if len(list) < 1:
			print(len(list))
			continue
		
		# if pcurrent is greater than future
		if list[i] < list[i-1]:
			swap(West)

			#swap list elements
			list[i], list[i - 1] = list[i - 1], list[i]
			
		move(East)

def cactusFarm():
	# Plant full of cactus 
	for i in range(get_world_size()):
		
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Cactus)
		
		move(North)
		
	
def startDrones():
	#plant and sort x
	for _ in range(get_world_size()):
		
		if spawn_drone(cactusFarm):			
			move(East)
		else:
			cactusFarm()
			move(East)
	while True:		
		for _ in range(get_world_size()):
			
			if spawn_drone(sort_x):			
				move(East)
			else:
				sort_x()
				move(East)
		
		for _ in range(get_world_size()):
			
			if spawn_drone(sort_y):			
				move(North)
			else:
				sort_y()
				move(North)

							

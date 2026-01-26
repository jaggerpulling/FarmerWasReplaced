def sort_x(list):
	
	list_len = len(list)

	#to initialize the loop
	swap_count = 1
	while swap_count > 0:
		
		swap_count = 0

		for i in range(get_world_size()):
			
			#ignore if last cactus in row to avoid bug
			if i == list_len-1:

				move(North)
				break
			
			# if current is greater than one ahead,
			if list[i] > list[i+1]:
				swap(North)
				move(North)
				
				#swap list elements
				list[i], list[i + 1] = list[i + 1], list[i]

			
				
				#adds 1 to continue loop if any swaps occur
				swap_count += 1
			else:
				move(North)
	
	sorted_list = list
	return sorted_list

def sort_y(list):
	
	list_len = len(list)

	#to initialize the loop
	swap_count = 1
	while swap_count > 0:
		
		swap_count = 0

		for i in range(get_world_size()):
			
			#ignore if last cactus in row to avoid bug
			if i == list_len-1:

				move(North)
				break
			
			# if current is greater than one ahead,
			if list[i] > list[i+1]:
				swap(North)
				move(North)
				
				#swap list elements
				list[i], list[i + 1] = list[i + 1], list[i]

			
				
				#adds 1 to continue loop if any swaps occur
				swap_count += 1
			else:
				move(North)
	
	sorted_list = list
	return sorted_list	
	
	


def start_farm():
	sorted_list = []
	row_list = []
	global unsorted
	
	for i in range(get_world_size()):
			
		#Plant Cactus
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Cactus)
		
		#create list of cactus size values for each row
		row_list.append(measure())
		
		if unsorted:
			move(North)
		else: 
			move(East)

	#overwrites row_list to sorted list
	sorted_list = sort_x(row_list)



#create correct grid size
max_drones = max_drones()
#set_world_size(max_drones-1)

def runningCactus():
	global unsorted
	
	#Sort by x
	#uses unsorted variable to start farm to to do x first then y
	unsorted = True 
	for _ in range(max_drones):
		spawn_drone(start_farm)
		move(East)
	print('done')
	unsorted = False
	
	#Sort by Y
	wait_for(drone)
	for _ in range(max_drones):
		spawn_drone(start_farm)
		move(North)
	print('done')
		
runningCactus()
# each drone sorts only in its row. appends new list. doesnt compare to other row
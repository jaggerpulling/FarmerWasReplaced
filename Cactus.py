def sort(list):
	
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
	
def compare_list(sorted_list, row_list, swap_count_y):

	if sorted_list: #skip first
		
		#compare current row to previous row 
		for i in range(get_world_size()):
			if sorted_list[i] > row_list[i]:
				swap(West)
				move(North)
				
				#Swap list items
				sorted_list[i], row_list[i] = row_list[i], sorted_list[i]
				swap_count_y += 1
				
			else:
				move(North)
				

	return sorted_list, swap_count_y, row_list
				

def start_farm():
	sorted_list = []
	swap_count_y = 0
	
	for i in range(get_world_size()):
		row_list = []
		for i in range(get_world_size()):

			
			#Plant Cactus
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Cactus)
			
			#create list of cactus size values for each row
			row_list.append(measure())
	
			move(North)
		
		sorted_list, swap_count_y, row_list = compare_list(sorted_list, row_list, swap_count_y)
		sorted_list = sort(row_list)
		move(East)


	return swap_count_y
		
def cactus():
	swap_count_y = 1
	while swap_count_y > 0:							  
		swap_count_y = start_farm()
	harvest()
	
cactus()		

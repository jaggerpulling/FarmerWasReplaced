#allows drone for each row
set_world_size(max_drones())
NUM_ROWS = max_drones()

def waterfunction(min_water_lvl = 0.3):
	#Checks ground water level and adds water if it drops below min_water_lvl.
	#Default min_water_lvl = 0.3
	water_level = get_water()
	
	#water the ground
	if water_level < min_water_lvl:
		use_item(Items.Water)

def move_to(x,y):

	while get_pos_x() != x or get_pos_y() != y:
		
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

def sunflower_farm():
	for i in range(get_world_size()):
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Sunflower)
		move(North)


def plant_sunflower():
	
	for _ in range(get_world_size()):
		if spawn_drone(sunflower_farm):
			move(East)
		else:
			sunflower_farm()
			move(East)

#Plant all sunflower			
plant_sunflower()
			
def measure_row():
	sunflower_measurement_by_location = {}

	for _ in range(get_world_size()):
		x, y = get_pos_x(), get_pos_y()
		sunflower_measurement_by_location[(x, y)] = measure()
		move(East)

	return sunflower_measurement_by_location

def start_sunflower():
	drones = []
	
	for _ in range(NUM_ROWS):
		drone = spawn_drone(measure_row)
		drones.append(drone)
		move(South)  # move main drone to next row
	
	#list of dict values 			
	rows = []
	# list of just measurements
	all_measure_values = []
	#all pairs in one dict
	total_dict = {}
	
	for drone in drones:
		rows.append(wait_for(drone))
	
	
	# COMBINE ROWS INTO 1 Dictionary
	# get each item from row of rows 
	for row in rows:
		for coord in row: 
			all_measure_values.append(row[coord])
			total_dict[coord] = row[coord]
	
	#loop that checks for greatest value and harvests
	while True:
		#end loop if empty
		if not all_measure_values:
			print("BREKOUT")
			break
		
		greatest_value=max(all_measure_values)
		
		#get x,y coord of greatest value
		for coord in total_dict:
			if total_dict[coord] == greatest_value:
				x, y = coord
				break
	
		move_to(x, y)
		harvest()

		#remove selected coordinate
		total_dict.pop((x, y))
		all_measure_values.remove(greatest_value)

start_sunflower()

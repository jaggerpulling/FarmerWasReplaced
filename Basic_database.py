
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

def waterfunction(min_water_lvl = 0.3):
	#Checks ground water level and adds water if it drops below min_water_lvl.
	#Default min_water_lvl = 0.3
	water_level = get_water()
	
	#water the ground
	if water_level < min_water_lvl:
		use_item(Items.Water)

def sunflower_farm():

	#while total sunflowers in garden > 10
	while True:
	
		#remember to reset this 
		sunflower_measurement_location = {}
		
		#plant all sunflowers, measure value and store
		for i in range(get_world_size()):				
			for i in range(get_world_size()):
				
				min_water_lvl = .3
				waterfunction(min_water_lvl)
				
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Sunflower)
				x, y = get_pos_x(), get_pos_y()
				sunflower_measurement_location[(x, y)] = measure()
					
				move(North)
			move(East)
			
		
		while True:
			# find greatest value
			
			all_values = []
			for coord in sunflower_measurement_location:
				all_values.append(sunflower_measurement_location[coord])
	
			#end loop if empty
			if not all_values:
				break
					
			greatest_value = max(all_values)
		
			# find coordinates corresponding to greatest value
			for coord in sunflower_measurement_location:
				if sunflower_measurement_location[coord] == greatest_value:
					x, y = coord
					break
					
			move_to(x, y)
			harvest()
			
			#remove selected coordinate
			sunflower_measurement_location.pop((x, y))
					 					 		
def carrot():
	while True:
		
		for i in range(get_world_size()):	
			for i in range(get_world_size()):
				waterfunction()
				
				if get_ground_type() == Grounds.Grassland:
					till()
					plant(Entities.Carrot)
				
				if can_harvest():
					harvest()
					plant(Entities.Carrot)		
					
				move(North)
			move(East)


def punkin():
	# if standing over all blocks and equal to pumpkling harvest
	while True:
		pumpkin_count = 0
		world_size = get_world_size()
		
		
		for i in range(get_world_size()):
			for i in range(get_world_size()):
				#waterfunction()
				
				if get_ground_type() == Grounds.Grassland:
					till()
			
				if get_entity_type() == Entities.Pumpkin:
					pumpkin_count += 1

				if pumpkin_count != world_size ** 2:
					plant(Entities.Pumpkin)
				else:
					harvest()
					
				move(North)
			move(East)

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

def checker_wood():
	while True:
		#y loop
		for i in range(get_world_size()):
			x = get_pos_x()
	
			#x loop
			for index in range(get_world_size()):
				if can_harvest():
					harvest()

				y = get_pos_y()
				
				#water the Grounds
				waterfunction()
		
				#plant trees and carrots
				if (x + y) % 2 == 0:   # even sum
					plant(Entities.Tree)
				else:                  # odd sum
					if get_ground_type() == Grounds.Grassland:
						till()
						plant(Entities.Carrot)
					else:
						plant(Entities.Carrot)
		
				move(North)
			move(East)




def waterfunction():
#will check ground water level and add if drops below 0.2	
	
	water_level = get_water()
	
	#water the ground
	if water_level < 0.2:
		use_item(Items.Water)
import Basic_database
import DINO_SNAKE
import MAZE_RUNNER
import Cactus
	 

farms = {
	'hay': Basic_database.runningGrass,
	'wood': Basic_database.checker_wood,
	'carrot': Basic_database.carrot,
	'pumpkin': Basic_database.punkin,
	'cactus': Cactus.cactus,
	#needs fixing'dino': snake,
	#'weird': weird_farm,
	#'maze': maze_runner
}

inventory_items = {
	'hay': (Items.Hay),
	'wood': (Items.Wood),
	'carrot': (Items.Carrot),
	'pumpkin': (Items.Pumpkin),
	'cactus': (Items.Cactus),
	'dino': (Items.Bone),
	'weird': (Items.Weird_Substance),
	'maze': (Items.Gold)
}
prev_amount = None


#compares inventory item values to determine which is greater
for key in inventory_items: 
	amount = num_items(inventory_items[key]) # get inventory amount for each item
	
	if prev_amount != None:
		if prev_amount < amount :
			print(amount)
			print(prev_amount)
			#do something
			selected_farm = prev_key
			#planting(selected_farm)
			break
	
	#assign amount and key to last rather than current
	prev_amount = amount
	prev_key = key

		
def planting(selected_farm):
	#start farm for selected farm
	farms[selected_farm]()

	

# Get amount needed and current amount
target_amount = amount
current_amount = prev_amount 

# Run the farm until resource is greater than current
while current_amount <= target_amount:
	print(prev_key)
	print(key)
	planting(selected_farm)
	
	# Get current amount
	current_amount = num_items(inventory_items[prev_key]) 
	
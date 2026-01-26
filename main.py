import Basic_database
import MultipleDronesGrass
import MultipleDronesCarrot
import MultipleDronesTree
#import DINO_SNAKE
import MAZE_RUNNER
import cactusDrones
import MultiplePumpkin
	 

farms = {
	'hay': MultipleDronesGrass.grass,
	'wood': MultipleDronesTree.tree,
	'carrot': MultipleDronesCarrot.carrot,
	'pumpkin': MultiplePumpkin.run,
	'cactus': cactusDrones.startDrones,
	#'dino': DINO_SNAKE.snake,
	#'maze': MAZE_RUNNER.maze_runner
}

inventory_items = {
	'hay': (Items.Hay),
	'wood': (Items.Wood),
	'carrot': (Items.Carrot),
	'pumpkin': (Items.Pumpkin),
	'cactus': (Items.Cactus),
	#'dino': (Items.Bone),
	#'weird': (Items.Weird_Substance),
	#'maze': (Items.Gold)
}

prev_amount = None

	
def planting(selected_farm):
	#start farm for selected farm
	farms[selected_farm]()
	
	

while True:
	#compares inventory item values if first is less than following
	for key in inventory_items: 
		amount = num_items(inventory_items[key]) # get inventory amount for each item
		
		
		if prev_amount != None: # ignore first 
			
			if prev_amount < amount : 
				selected_farm = prev_key
				
				print(selected_farm)
				#keep doing current farm until amount is even
				while prev_amount < amount:
					#check prev amount 
					prev_amount = num_items(inventory_items[prev_key])
					planting(selected_farm)
					
				#reset farm after finished
				Basic_database.move_to(0,0)
				clear()

		prev_amount = amount
		prev_key = key
	

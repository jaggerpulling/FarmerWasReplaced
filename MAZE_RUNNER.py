def try_harvest():
	if get_entity_type() == Entities.Treasure:
		harvest()

def maze_runner():
	directions = [North, East, South, West]  # clockwise
	facing = 0  # start facing North
	
	while get_entity_type() != Entities.Treasure:
			# Try right first
		if move(directions[(facing + 1) % 4]):
			facing = (facing + 1) % 4
			continue
		# Try forward
		if move(directions[facing]):
			continue
		# Try left
		if move(directions[(facing - 1) % 4]):
			facing = (facing - 1) % 4
			continue
			# Dead end: turn around
		facing = (facing + 2) % 4
		move(directions[facing])

def maze():
	while True:
		plant(Entities.Bush)
		n_substance = get_world_size() * get_world_size()
		use_item(Items.Weird_Substance, n_substance)
		maze_runner()
		harvest()
		DONE = True

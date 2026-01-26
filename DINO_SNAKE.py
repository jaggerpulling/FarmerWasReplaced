def home():
	while get_pos_x() != 0:
		move(West)
	while get_pos_y() != 0:
		move(South)

def reset():
	change_hat(Hats.Straw_Hat)
	home()
	global DO 
	DONE = True
	

def move_north():
	if move(North) == False:
		reset()

def move_south():
	if move(South) == False:
		reset()

def move_east():
	if move(East) == False:
		reset()

def move_west():
	if move(West) == False:
		reset()
		
def snake():
	world_edge2edge = (get_world_size()-1)
	inner_zigzag_size = world_edge2edge-1
	
	global DONE
	while DONE == False:
#1
		for i in range(world_edge2edge):
			move_north()
#2
		for i in range(world_edge2edge):
			move_east()
		move_south()
		
		#inner zig zag
		for tile in range(world_edge2edge-2):
#3
			for i in range(inner_zigzag_size):
				move_west()
			if get_pos_y() != 0:
				move_south()
#4			
			if tile != (world_edge2edge-4):
				for i in range(inner_zigzag_size):
					move_east()
				if get_pos_y() != 0:
					move_south()
			else:
				home()
				break
#5

		

#initialize hat and pos
DONE = False


change_hat(Hats.Straw_Hat)
home()
change_hat(Hats.Dinosaur_Hat)
snake()
def sort(list):

	sorted_list = list[:]
	list_length = len(sorted_list)
	
	for i in range(list_length):
		for j in range(0, n-i-1):
			if sorted_list[j] > sorted_list[j+1]:
					sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
					
					
	return sorted_list

									 
def max_gain(input_list):
	if (input_list[len(input_list)-1] - input_list[0]  < 0):
		return 0
	else:
		input_list.sort()
		return  input_list[len(input_list)-1] - input_list[0] 

print(max_gain([0,50,10,100,30]))
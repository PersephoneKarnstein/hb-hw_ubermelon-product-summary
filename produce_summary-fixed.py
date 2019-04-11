files = ["um-deliveries-20140519.txt"]#, "um-deliveries-20140520.txt", "um-deliveries-20140521.txt"]

def summarize_deliveries(file_list):
	"""
	I built in a frankly unnecessary amount of safety against badly-formatted program calls and 
	files that don't exist: I think the whole thing could hae basically been lines 19, 21, 25, 27.
	"""
	import calendar 

	if not isinstance(file_list, list) and not isinstance(file_list, str): #if you were writing this function to actually use, you could conceivably give it only a single file, or give it a list of multiple filenames. Check to make sure the variable passed to it is one of those.
		print("This function only takes strings and lists of strings as its parameters.\n\n")
		raise ValueError
		return #tbh if they give you something that's not a string or a list they're clearly not trying so the program just nopes out.
	else:
		if isinstance(file_list, str): #in order to use "for a in b," we have to make any individual filenames we get passed into lists.
			file_list = [file_list]
		else: pass

		for path in file_list:
			try:
				with open(path) as f:
					date = path.split('-')[2].split(".")[0]
					print("\n\n" + str(int(date[6:8])) +" "+ calendar.month_name[int(date[4:6])] +" "+ str(int(date[:4])))
					print("{:-<20}".format(""))
					for line in f:
						line = line.rstrip().split('|')
						print("Delivered {0:<2} {1:<46} for a total of ${2}.".format(line[1], line[0]+"s,", line[2]))
			except FileNotFoundError: 
				print(f"{path} is not a valid filename.")
				continue

summarize_deliveries(files)
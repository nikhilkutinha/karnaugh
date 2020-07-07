def compare(combo, flag, kmap):

	for _ in combo:
		if not kmap[_] == 1 and not kmap[_] == flag:
			return False
	return True

def assign(combo, kmap):
	for _ in combo:
		kmap[_] = -1
	return kmap

def remove_key(d, key):
    r = dict(d)
    del r[key]
    return r

def remove_redundant(sop, combined):
	check_list = []
	redundant_grps = []
	
	for group in combined:
		check_dict = remove_key(combined, group)
		for j in check_dict:
			check_list.extend(check_dict[j])

		if set(combined[group]).issubset(check_list):
			redundant_grps.append(group)

		check_list = []

	for term in redundant_grps:
		if term in sop:
			sop.remove(term)
	
	return sop

def validate(expression, map_type):
	
	errors = []

	# check if the input == blank
	if not expression:
		errors.append("You cannot enter a blank value.")


	if map_type == '1':
		if len(expression) > 4:
			errors.append("Please do not enter more than 4 elements.")
		try:
			if max(expression) > 3:
				errors.append("Please do not enter a value larger than 3.")
		except:
			pass


	if map_type == '2':
		if len(expression) > 8:
			errors.append("Please do not enter more than 8 elements.")
		try:
			if max(expression) > 7:
				errors.append("Please do not enter a value larger than 7.")
		except:
			pass

	if map_type == '3':
		if len(expression) > 16:
			errors.append("Please do not enter more than 16 elements.")
		try:
			if max(expression) > 15:
				errors.append("Please do not enter a value larger than 15.")
		except:
			pass

	# check if there are duplicates present in the input
	if not len(set(expression)) == len(expression):
		errors.append("Please do not enter duplicate elements.")

	
	if errors:
		for _ in errors : print(_)
		return False

	else:
		return True




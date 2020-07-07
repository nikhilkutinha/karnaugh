from utils import validate, compare, assign, remove_redundant

class Karnaugh:
	
	def __init__(self, kmap_type, expression):
		self.kmap_type = kmap_type
		self.expression = expression
		self.kmap = self.create_kmap()
		self.combos = {
			
			# combinations for the two variable kmap
			'two' : {
				'quads' : {
					'***' : [0, 1, 2, 3],
				},

				'pairs' : {
					'A-' : [0, 1],
					'A' : [2, 3],
					'B-' : [0, 2],
					'B' : [1, 3],
				},

				'loners' : {
					'A-B-' : [0],
					'AB-' : [2],
					'A-B' : [1],
					'AB' : [3],
				}

			},

			# combinations for the three variable kmap
			'three' : {
				'octets' : {
					'***' : [0, 1, 2, 3, 4, 5, 6, 7],
				},

				'quads' : {
					'A-' : [0, 1, 3, 2],
					'B-' : [0, 1, 4, 5],
					'C-' : [0, 2, 4, 6],

					'A' : [4, 5, 6, 7],
					'B' : [2, 3, 6, 7],
					'C' : [1, 3, 5, 7],
				},

				'pairs' : {
					'B-C-' : [0, 4],
					'A-B-' : [0, 1],
					'A-C-' : [0, 2],

					'B-C' : [1, 5],
					'A-C' : [1, 3],
					'BC' : [3, 7],

					'A-B' : [2, 3],
					'BC-' : [2, 6],
					'AB-' : [4, 5],

					'AC-' : [4, 6],
					'AC' : [5, 7],
					'AB' : [6, 7],
				},

				'loners' : {
					'A-B-C-' : [0],
					'A-B-C' : [1],
					'A-BC' : [3],
					'A-BC-' : [2],
					'AB-C-' : [4],
					'AB-C' : [5],
					'ABC' : [6],
					'ABC' : [7],
				},
			},

			# combinations for the four variable kmap
			'four' : {
				'octets' : {
					
					'A-' : [0, 1, 3, 2, 4, 5, 6, 7],
					'A' : [12, 13, 15, 14, 8, 9, 11, 10],

					'B' : [4, 5, 7, 6, 12, 13, 15, 14],
					'B-' : [0, 1, 3, 2, 8, 9, 11, 10],

					'C-' : [0, 1, 4, 5, 12, 13, 8, 9],
					'C' : [3, 2, 7, 6, 15, 14, 11, 10],

					'D' : [1, 3, 5, 7, 13, 15, 9, 11],
					'D-' : [0, 2, 4, 6, 12, 14, 8, 10],

				},

				'quads' : {

					'A-C-' : [0, 1, 4, 5],
					'A-C' : [3, 2, 7, 6],
					'BC-' : [4, 5, 12, 13],
					'BC' : [7, 6, 15, 14],
					'AC-' : [12, 13, 8, 9],
					'AC' : [15, 14, 11, 10],

					'A-D' : [1, 3, 5, 7],
					'BD' : [5, 7, 13, 15],
					'AD' : [13, 15, 9, 11],

					'A-B-' : [0, 1, 3, 2],
					'A-B' : [4, 5, 7, 6],
					'AB' : [12, 13, 15, 14],
					'AB-' : [8, 9, 11, 10],

					'C-D-' : [0, 4, 12, 8],
					'C-D' : [1, 5, 13, 9],
					'CD' : [3, 7, 15, 11],
					'CD-' : [2, 6, 14, 10],

					'B-D-' : [0, 2, 8, 10],

					'B-C-' : [0, 1, 8, 9],
					'B-C' : [3, 2, 11, 10],
					'B-D' : [1, 3, 9, 11],

					'A-D-' : [0, 2, 4, 6],
					'AD-' : [12, 14, 8, 10],
					'BD-' : [4, 6, 12, 14],

				},

				'pairs' : {
					'A-B-C-' : [0, 1],
					'A-B-C' : [3, 2],
					'A-BC-' : [4, 5],
					'A-BC' : [7, 6],
					'ABC-' : [12, 13],
					'ABC' : [15, 14],
					'AB-C-' : [8, 9],
					'AB-C' : [11, 10],

					'A-B-D' : [1, 3],
					'A-BD' : [5, 7],
					'ABD' : [13, 15],
					'AB-D' : [9, 11],
					
					'A-C-D-' : [0, 4],
					'A-C-D' : [1, 5],
					'A-CD' : [3, 7],
					'A-CD-' : [2, 6],
					'AC-D-' : [12, 8],
					'AC-D' : [13, 9],
					'ACD' : [15, 11],
					'ACD-' : [14, 10],
					
					'BC-D-' : [4, 12],
					'BC-D' : [5, 13],
					'BCD' : [7, 15],
					'BCD-' : [6, 14],

					'A-B-D-' : [0, 2],
					'A-BD-' : [4, 6],
					'ABD-' : [12, 14],
					'AB-D-' : [8, 10],
					
					'B-C-D-' : [0, 8],
					'B-C-D' : [1, 9],
					'B-CD' : [3, 11],
					'B-CD-' : [2, 10],

				},

				'loners' : {
					'A-B-C-D-' : [0],
					'A-B-C-D' : [1],
					'A-B-CD' : [3],
					'A-B-CD-' : [2],

					'A-BC-D-' : [4],
					'A-BC-D' : [5],
					'A-BCD' : [7],
					'A-BCD-' : [6],

					'ABC-D-' : [12],
					'ABC-D' : [13],
					'ABCD' : [15],
					'ABCD-' : [14],

					'AB-C-D-' : [8],
					'AB-C-D' : [9],
					'AB-CD' : [11],
					'AB-CD-' : [10],

				},
			},
		}

	def reduce(self):
		
		sop = []
		combined = {}			# used for redundant group removal
		combos = self.combos
		m = self.kmap			# copying the expression to a smaller variable name for readibility

		####################################
		###### 2 Variable Karnaugh Map #####
		####################################

		if self.kmap_type == '1':

			###### QUAD CHECK #####
			combo = combos['two']['quads']['***']
			if compare(combo, 1, m):
				sop.append('***')
				m = assign(combo, m)

			###### PAIR CHECK ######
			for flag in [1, -1]:
				for i in range(0, 4):
					if m[i] == 1 :
						for pair in combos['two']['pairs']:
							if i in combos['two']['pairs'][pair]:
								combo = combos['two']['pairs'][pair]
								if compare(combo, flag, m):
									sop.append(pair)
									m = assign(combo, m)

			###### LONER CHECK ######
			for flag in [1]:
				for i in range(0, 4):
					if m[i] == 1 :
						for loner in combos['two']['loners']:
							if i in combos['two']['loners'][loner]:
								combo = combos['two']['loners'][loner]
								if compare(combo, 1, m):
									sop.append(loner)
									m = assign(combo, m)

		####################################
		###### 3 Variable Karnaugh Map #####
		####################################

		if self.kmap_type == '2': 

			###### OCTET CHECK #####
			combo = combos['three']['octets']['***']
			if compare(combo, 1, m):
				sop.append('***')
				m = assign(combo, m)

			###### QUAD CHECK ######
			for flag in [1, -1]:
				for i in range(0, 8):
					if m[i] == 1 :
						for quad in combos['three']['quads']:
							if i in combos['three']['quads'][quad]:
								combo = combos['three']['quads'][quad]
								if compare(combo, flag, m):
									sop.append(quad)
									combined.update({"{}".format(quad) : combo})
									m = assign(combo, m)
			

			###### PAIR CHECK ######
			for flag in [1, -1]:
				for i in range(0, 8):
					if m[i] == 1 :
						for pair in combos['three']['pairs']:
							if i in combos['three']['pairs'][pair]:
								combo = combos['three']['pairs'][pair]
								if compare(combo, flag, m):
									sop.append(pair)
									combined.update({"{}".format(pair) : combo})
									m = assign(combo, m)
			
			###### LONER CHECK ######
			for flag in [1]:
				for i in range(0, 8):
					if m[i] == 1 :
						for loner in combos['three']['loners']:
							if i in combos['three']['loners'][loner]:
								combo = combos['three']['loners'][loner]
								if compare(combo, 1, m):
									sop.append(loner)
									combined.update({"{}".format(loner) : combo})
									m = assign(combo, m)

		####################################
		###### 4 Variable Karnaugh Map #####
		####################################

		if self.kmap_type == '3': 

			###### OCTET CHECK ######
			for flag in [1, -1]:
				for i in range(0, 16):
					if m[i] == 1 :
						for octet in combos['four']['octets']:
							if i in combos['four']['octets'][octet]:
								combo = combos['four']['octets'][octet]
								if compare(combo, flag, m):
									sop.append(octet)
									combined.update({"{}".format(octet) : combo})
									m = assign(combo, m)

			###### QUAD CHECK ######
			for flag in [1, -1]:
				for i in range(0, 16):
					if m[i] == 1 :
						for quad in combos['four']['quads']:
							if i in combos['four']['quads'][quad]:
								combo = combos['four']['quads'][quad]
								if compare(combo, flag, m):
									sop.append(quad)
									combined.update({"{}".format(quad) : combo})
									m = assign(combo, m)

			###### PAIR CHECK ######
			for flag in [1, -1]:
				for i in range(0, 16):
					if m[i] == 1 :
						for pair in combos['four']['pairs']:
							if i in combos['four']['pairs'][pair]:
								combo = combos['four']['pairs'][pair]
								if compare(combo, flag, m):
									sop.append(pair)
									combined.update({"{}".format(pair) : combo})
									m = assign(combo, m)

			###### LONER CHECK ######
			for flag in [1]:
				for i in range(0, 16):
					if m[i] == 1 :
						for loner in combos['four']['loners']:
							if i in combos['four']['loners'][loner]:
								combo = combos['four']['loners'][loner]
								if compare(combo, 1, m):
									sop.append(loner)
									combined.update({"{}".format(loner) : combo})
									m = assign(combo, m)
		

		return remove_redundant(sop, combined) 

	def create_kmap(self):
		if self.kmap_type == '1':
			kmap = [0, 0, 
					0, 0]

		elif self.kmap_type == '2':
			kmap = [0, 0, 0, 0, 
				 	0, 0, 0, 0]

		elif self.kmap_type == '3':
			kmap = [0, 0, 0, 0, 
				 	0, 0, 0, 0,
				 	0, 0, 0, 0,
				 	0, 0, 0, 0]

		for _ in self.expression:
			kmap[_] = 1

		return kmap



while True:
	kmap_type = input("1) 2 Variable \n2) 3 Variable \n3) 4 Variable \n")
	if kmap_type == '1' or kmap_type == '2' or kmap_type == '3':
		break
	else:
		print("<{}> == an invalid input, please enter the correct corresponding value.\n".format(kmap_type))

# 2 variable kmap
if kmap_type == '1': 
	while True:
		expression = [int(_) for _ in input("\nEnter the expression \n(A, B) = ").split()]
		if validate(expression, kmap_type):
			break

# 3 variable kmap
elif kmap_type == '2':
	while True:
		expression = [int(_) for _ in input("\nEnter the expression \n(A, B, C) = ").split()]
		if validate(expression, kmap_type):
			break

# 4 variable kmap 
elif kmap_type == '3': 
	while True:
		expression = [int(_) for _ in input("\nEnter the expression \n(A, B, C, D) = ").split()]
		if validate(expression, kmap_type):
			break

map = Karnaugh(kmap_type, expression)

sop = map.reduce()
sop = ' + '.join(sop).replace('-', '\'')

print("SOP = {}".format(sop))
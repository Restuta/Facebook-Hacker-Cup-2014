def is_in_valid_range(first_sharp_y, first_sharp_x, current_y, current_x, square_length):
	fromY = first_sharp_y
	toY = fromY + square_length - 1

	fromX = first_sharp_x
	toX = fromX + square_length - 1

	#todo: we can avoid checking for "from" here for x
	in_valid_range = (current_y >= fromY and current_y <= toY) and (current_x >= fromX and current_x <= toX)

	#print current_x, current_y, in_valid_range
	return in_valid_range

#square detector
f = open('square_detector_example_input.txt', 'r')
number_of_test_cases = int (f.readline())

#reading input
for case_number in xrange(number_of_test_cases):
	dimention = int (f.readline())

	field = []
	for j in xrange(dimention):
		field.append([(f.read(1)) for x in xrange(dimention)])
		f.read(1) #todo: refactor

	#print field

	#find square
	first_line_of_sharps_was_found = False
	first_sharp_was_found = False
	first_sharp_x = 0
	first_sharp_y = 0
	square_length = 0
	square_exists = None

	for x in xrange(dimention):
		if square_exists == False:
			break

		for y in xrange(dimention):
			#print field[x][y]

			if first_line_of_sharps_was_found:
				if is_in_valid_range(first_sharp_y, first_sharp_x, y, x, square_length):
					if field[x][y] != '#':
						square_exists = False
						break
				else:
					if field[x][y] == '#':
						square_exists = False
						break
			else:
				if first_sharp_was_found:
					if field[x][y] == '.' or y == (dimention - 1):
						first_line_of_sharps_was_found = True
						#print x,y

					if field[x][y] == '#':
						square_length += 1
				else:
					if field[x][y] == '#':
						first_sharp_was_found = True
						first_sharp_y = y
						first_sharp_x = x
						square_length = 1
						#print x,y

	#todo: vertical iteration check
	#todo: add successfull result if no fails were added
	if square_exists == None and first_sharp_was_found:
		square_exists = True
	if square_exists == None:
		square_exists = False
	
	print "Case #{}: {}".format(case_number + 1, 'YES' if square_exists else 'NO')
f.close()			 	

import timeit
def insertsort(arraylist):
	for index in range(1, len(arraylist)):
		currentvalue = arraylist[index]
		position = index

		while position>0 and arraylist[position-1]>currentvalue:
			arraylist[position] = arraylist[position-1]
			position = position -1

		arraylist[position] = currentvalue

	return arraylist 
# all students wearing red shirts must be in a same row
# all students		   blue shirts
# students taller  than infront of them
# if numbers same : return false

#O(nlogn) time - sort | O(1) space -> mutuating input array: if not then O(n) auxilary space
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	shirtColorInFirstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE" # tallest student/ biggest number is added to blueShirtHeights followed by, redShirtHeights
	for idx in range(len(redShirtHeights)):
		redShirtHeight = redShirtHeights[idx]
		blueShirtHeight = blueShirtHeights[idx]
		
		if shirtColorInFirstRow == "RED":
			if redShirtHeight >= blueShirtHeight:
				return False
		else:
			if blueShirtHeight >= redShirtHeight:
				return False
	return True
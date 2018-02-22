import random
x = "n"
while x != "y":
	players = [[0 for r in range(5)] for i in range(100)]
	y = input("Πατήστε y και enter άμα θέλετε να θέσετε χειροκίνητα τους αριθμούς αλλιώτικα απλά πατήστε enter ")
	if y == "y":
		for a in range(100):
			number = [0,0,0,0,0]
			for k in range(5):
				che = 0
				lv = 0
				while che == 0:
					try:
						lv = int(input("Πατήστε τον αριθμό  " + str(k+1) + " του  " + str(a) + " παίκτη "))
					except Exception as e:
						print("Γράψτε αριθμό όχι κάτι άλλο")
						continue
					che = 1
					if lv > 80 :
						che = 0
						print("Διάλεξε έναν αριθμό έως το 80")
						continue
					if lv < 1 :
						che = 0
						print("Διάλεξε έναν αριθμό από το 1 και μετά")
						continue
					for klo in range(5):
						if number[klo] == lv:
							che = 0
							print("Διάλεξε έναν αριθμό που δεν έχεις διαλέξει")
							break
				number[k] = lv
				players[a][k] = lv	
	else:
		for a in range(100):
			number = [0 for r in range(80)]
			for n in range(80):
				number[n] = n+1
			for k in range(5):
				lv = random.choice(number)
				players[a][k] = lv
				number.remove(lv)
	foravr = 0
	for m in range(100):
		print ("Ο παίκτης "+ str(m+1) + " έχει τους αριθμούς " + str(players[m]))
	input("Πατήστε enter για να αρχίσει το πρώτο παιχνίδι ΜΠΙΝΓΚΟ")
	for xil in range(1000):
		numbers = [0 for r in range(80)]
		bingo = 1
		win = []
		for n in range(80):
			numbers[n] = n+1
		for n in range(80):
			y = random.choice(numbers)
			numbers.remove(y)
			win.append(y)
			print("Διαλεκτικέ ο αριθμός " + str(y))
			for m in range (100):
				sumwin = 0
				for j in range(5):
					for t in range(len(win)):
						if win[t] == players[m][j]:
							sumwin = sumwin + 1
				if sumwin == 5:
					bingo = 2
					foravr = foravr+n+1
					print("\nΠαιχνίδι " + str(xil +1) + " νίκησε ο παίκτης " + str(m+1) + " την φορά " + str(n+1))
					break
			if bingo == 2:
				break
		if xil == 999:
			print ("\nΟ μέσος ορός των φορών που χαριστικέ να επιλεχθεί αριθμός για να νικήσει κάποιος είναι " + str(foravr/1000))
		else:
			input("Πατήστε enter για να αρχίσει το επόμενο παιχνίδι ΜΠΙΝΓΚΟ")
	x = input("Πατήστε y  και enter για να κλείσει το πρόγραμμα ή απλά enter για να ξαναπαίξετε ")
	

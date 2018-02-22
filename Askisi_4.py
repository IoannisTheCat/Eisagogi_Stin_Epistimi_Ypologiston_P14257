bnums = ["","one ","two ","three ","four ","five ","six ","seven ","eight ","nine ","ten ","eleven ","twelve ","thirteen ","fourteen ","fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]
dnums = ["twenty ","thirty ","forty ","fifty ","sixty ","seventy ","eighty ","ninety "]
def Dnum(f):
	if f == 0:
		return "zero"
	elif f < 20:
		return bnums[f]
	else:
		return dnums[(f//10) - 2] + bnums[f - ((f//10)*10)]
y = 0
while y == 0:
	num = "0"
	x = 0
	try:
		x = int(input("Γράψτε τον αριθμό που θες να μετατρέψεις σε λατινικούς χαρακτήρες\n"))
	except Exception as e:
		print("Γράψτε αριθμό όχι κάτι άλλο")
		continue
	if x > 1000000:
		print("Διάλεξε έναν αριθμό μέχρι το 1000000")
		continue
	if x < 0:
		print("Διάλεξε έναν θετικό αριθμό ")
		continue
	if x == 1000000:
		num = "One Million"
	elif x >= 100000:
		if (x -((x//1000)*1000))//100 == 0:
			te = ""
		else:
			te = bnums[(x -((x//1000)*1000))//100] + "hundred "
		num = bnums[x//100000] + "hundred " + Dnum((x - ((x//100000)*100000))//1000) + "thousand " + te + Dnum((x -(x//100)*100))
	elif x >= 1000:
		if (x -((x//1000)*1000))//100 == 0:
			te = ""
		else:
			te = bnums[(x -((x//1000)*1000))//100] + "hundred "
		num = Dnum(x//1000) + "thousand " + te + Dnum((x -(x//100)*100))
	elif x >= 100:
		num = bnums[x//100] + "hundred " + Dnum((x -(x//100)*100))
	else:
		num = Dnum((x -(x//100)*100))
	print(num)
	end = input("Πατήστε y  και enter για να κλείσει το πρόγραμμα ή απλά enter για να μετατρέψετε ξανά\n")
	if end == "y":
		y = 1

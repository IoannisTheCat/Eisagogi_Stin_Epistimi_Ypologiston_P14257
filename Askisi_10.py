import random
words = []
triades = []
cvb = 0
while cvb == 0:
	words = []
	try:
		x = input("enter the file path ")
		with open(x, "r") as y:
			for l in y:
				for w in l.split():
					up = 0
					for c in w:
						if c.isupper():
							up = 1
					if up == 0:
						words.append(w)
	except Exception as e:
		print("this file does not exist")
		continue
	cvb = 1
tri = 0
if len(words) >= 3:
	tri =  len(words) -2
for n in range(tri):
	triades.append(words[n] + " " + words[n+1] + " " + words[n+2])
met = 0
r = ""
if len(triades) == 0:
	met = 67
else:
	r = random.choice(triades)
	print(r, end = " ")
while met != 67:
	pith = []
	wo = r.split()
	for ri in triades:
		woo = ri.split()
		if wo[1] == woo[0]:
			if wo[2] == woo[1]:
				pith.append(ri)
	if len(pith) != 0:
		r = random.choice(pith)
		print(r, end = " ")
		met = met + 1
	else:
		met = 67
input("\nPress Enter to exit")
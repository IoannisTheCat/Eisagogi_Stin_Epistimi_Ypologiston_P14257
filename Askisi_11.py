import random
import string
pan = []
kat = []
dex = []
ari = []
for x in range(100):
	pan.append(random.choice(string.ascii_uppercase))
for x in range(100):
	kat.append(random.choice(string.ascii_uppercase))
for x in range(100):
	dex.append(random.choice(string.ascii_uppercase))
for x in range(100):
	ari.append(random.choice(string.ascii_uppercase))
dex[0] = pan[99]
dex[99] = kat[99]
ari[0] = pan[0]
ari[99] =kat[0]
for kloy in range(100):
	print(pan[kloy], end ="")
print(" ",end ="\n")
for kloy in range(98):
	print(ari[kloy+1],end = "")
	for sp in range(98):
		print(" ",end = "")
	print(dex[kloy+1])
for kloy in range(100):
	print(kat[kloy], end ="")
print(" ",end ="\n")
q = 0
while q == 0:
	try:
		op = input("enter the file path ")
		with open(op, "r") as lok:
			for li in lok:
				for wor in li.split():
					for t1 in range(100 - len(wor)):
						pani = ""
						kati = ""
						dexi = ""
						arii = ""
						pani2 = ""
						kati2 = ""
						dexi2 = ""
						arii2 = ""
						for t2 in range(len(wor)):
							pani = pani + pan[t1 + t2]
							kati = kati + kat[t1 + t2]
							dexi = dexi + dex[t1 + t2]
							arii = arii + ari[t1 + t2]
							pani2 = pani2 + pan[-(t1 + t2 + 1)]
							kati2 = kati2 + kat[-(t1 + t2 + 1)]
							dexi2 = dexi2 + dex[-(t1 + t2 + 1)]
							arii2 = arii2 + ari[-(t1 + t2 + 1)]
						if wor == pani:
							print(wor, end =" ")
							break
						if wor == kati:
							print(wor, end =" ")
							break
						if wor == dexi:
							print(wor, end =" ")
							break
						if wor == arii:
							print(wor, end =" ")
							break
						if wor == pani2:
							print(wor, end =" ")
							break
						if wor == kati2:
							print(wor, end =" ")
							break
						if wor == dexi2:
							print(wor, end =" ")
							break
						if wor == arii2:
							print(wor, end =" ")
							break
	except Exception as e:
		print("this file does not exist")
		continue
	q = 1
input("\nPress Enter to exit")

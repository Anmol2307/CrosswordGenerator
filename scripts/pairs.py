f = open("pairs.csv")
f1 = open("pairs-v1.csv","w")
l = f.readlines()
for k in l:
	s = k.split(",")
	a = s[0].strip().lower()
	b =	s[1].strip().lower()

	f1.write(a+","+b+"\n")

f1.close()
f.close()

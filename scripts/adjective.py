f = open("adjectives.csv")
l = f.readlines()
f1 = open("adjectives-v1.csv","w")
for k in l:
	k = k.strip()
	if k.isalpha():
		f1.write(k+"\n")

f1.close()
f.close()

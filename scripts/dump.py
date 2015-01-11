import requests
from string import ascii_letters
f = open("movies-v1.csv")
l = f.readlines()
url = "http://www.omdbapi.com/?t=%s&y=%s&plot=short&r=json"
f1 = open("movies-data.csv","a")
i = 0;
for k in l:

	s = k.split(",")
	title = ""

	if s[0][0] == '"' and s[0][-1] == '"':
		title = s[0][1:-1]
	elif all(c in ascii_letters+' ' for c in s[0]):
		title = s[0]

	if title == "":
		continue;

	year = s[1]

	r = requests.get(url%(title,year));
	if r.status_code == 200:
		title = title.replace(" ","")
		title = title.replace("	","")
		try:
			f1.write(title+"::"+r.json()["Plot"]+"::"+r.json()["Director"]+"\n");
			print r.json()
		except Exception, e:
			print e
		else:
			pass
		finally:
			pass

	print i
	i+=1
f.close()
f1.close()
url = "http://api.wordnik.com:80/v4/word.json/%s/definitions?limit=200&includeRelated=true&sourceDictionaries=all&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"
f = open("sports.csv")
f1 = open("sports-data.csv","w")
import requests
l  = f.readlines()
i = 0
for k in l:
	k = k.strip()
	r = requests.get(url%k)
	print r.json()
	if r.status_code == 200:
		try:
			ik = 0
			for p in r.json():
				if "exampleUses" in p:
					break
				ik+=1
			text = r.json()[ik]["text"]
			pos = r.json()[ik]["partOfSpeech"]
			exampleUses = "None"
			if r.json()[ik]["exampleUses"] != []:
				exampleUses = r.json()[0]["exampleUses"][0]["text"]
			f1.write(k+"::"+text+"::"+pos+"::"+exampleUses+"\n");
			print i
		except Exception, e:
			print e
		else:
			pass
		finally:
			pass
	i+=1
f1.close()
f.close()



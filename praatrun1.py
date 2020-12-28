
def praatrun1():
	import subprocess
	# Pour windows
	# subprocess.call(['Praat.exe', '--run', 'script1.praat'])

	# pour linux les deux premières commandes ne fonctionnent pas mais ça fonctionne bien en utilisant parcelmouth
	#subprocess.Popen(['Praat.exe, script1.praat'], shell=True)
	#subprocess.call('Praat.exe', '--run', 'script1.praat', shell=True)
	import parselmouth # pip install praat-parselmouth
	parselmouth.praat.run_file('script1.praat')

	f1 = open("record.TextGrid", "r", encoding = 'utf8')
	tG= f1.read()

	f1.close()

	tG = tG.split("\n")

	phonoption = {"a":"o", "e":"9", "o":"a","9":"e", "y":"u", "u":"y", "E":"e", "e":"E"}
	transcription = ""
	ok = False
	contenu = ""
	cpt = 0
	cpt2 = 0

	for i in range (0, len(tG)):

		if "text" in tG[i] :
			print(tG[i])
			cpt = 0
			cpt2 +=1
			for j in range (0, len(tG[i])):

				if tG[i][j] == "\"" and cpt<1:
					newtr = ""
					transcription = tG[i][j:len(tG)]
					cpt +=1
					for h in range(0, len(transcription)):
						if transcription[h] in phonoption and cpt2 <=1:
							newtr = newtr + transcription[h]+"*"+phonoption[transcription[h]][0]+"*"
							#transcription[h]=transcription[h]+"*"
						else:
							newtr = newtr + transcription[h]
					contenu = contenu + newtr
				elif cpt == 0:
					contenu = contenu + tG[i][j]
				elif j == len(tG[i])-1:
					contenu = contenu + "\n"
		else:
			contenu = contenu + tG[i] + "\n"

	print(transcription)




	f1.close()
	f1 = open("nouveaurecord.TextGrid", "w", encoding = 'utf8')
	f1.write(contenu)
	f1.close()
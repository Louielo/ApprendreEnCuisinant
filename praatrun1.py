
### Fonction qui lance les deux premieres étapes de easy align 
### et modifie le premier textgrid pour rajouter des phonèmes en options

def praatrun1():
	import fonction as fc

	import subprocess
	# Pour windows
	subprocess.call(['Praat.exe', '--run', 'script1.praat'])

	# pour linux les deux premières commandes ne fonctionnent pas mais ça fonctionne bien en utilisant parselmouth
	#subprocess.Popen(['Praat.exe, script1.praat'], shell=True)
	#subprocess.call('Praat.exe', '--run', 'script1.praat', shell=True)
	#import parselmouth # pip install praat-parselmouth
	#parselmouth.praat.run_file('script1.praat')

	encod = fc.encod(file="record.TextGrid")
	f1 = open("record.TextGrid", "r", encoding=encod)
	tG= f1.read()

	f1.close()

	# c du textgrid dans une liste ligne par ligne
	tG = tG.split("\n")
	# Liste des phonèmes que l'on va choisir de mettre en option
	phonoption = {"y":"u", "u":"y", "e":"E", "e~":"9~"}
	phon = ""			# partie du textgrid que l'on veut modifier
	c = ""				# contenu du nouveau textgrid
	firsttext = True	# booléen qui permet de savoir qu'il s'agit de la première occurence de 'text' dans le textgrid et donc de la ligne avec les phonèmes que l'on veut modifier
	guillemet = False 	# booléen qui indique quand on rencontre le guillement dans la ligne et donc le début du changement
	etoiles = ""		# Ce qu'on affichera à l'utilisateur pour lui montrer la transcription avec les phonèmes en option

	# boucle qui parcourt ligne par ligne le textgrid
	for i in range (0, len(tG)):
		l = tG[i]	# ligne
		# si on a text dans la ligne alors c'est la ligne qu'il faut modifier mais seulement si c'est la première
		if "text" in tG[i] and firsttext:
			firsttext = False	# on a trouvé le premier 'text' alors le booléen passe en False
			# On parcourt tous les caractères de la ligne
			for j in range (0, len(tG[i])):
				car = l[j]	#caractère
				# si on tombe sur un " alors on commence à modifier
				if car == "\"" and not guillemet:
					guillemet = True	# pour ne pas prendre en compte le second guillemet 
					phon = l[j:len(tG)]	# La transcription actuelle à changer
					# boucle qui parcourt la transcription
					for h in range(0, len(phon)):
						car = phon[h]
						if h < len(phon)-1:	# si on ne regarde pas le dernier caractère
							if car == "~":
								pass
							elif phon[h+1] == "~":	# Les cas où on a une ~ après le caractère
								vnasal = phon[h:h+2] # la voyelle plus le ~ de la nasalité
								if vnasal in phonoption:
									c+= vnasal+"*"+phonoption[vnasal]+"*"
									etoiles+= vnasal+"*"+phonoption[vnasal]+"*"
								else:
									c+= vnasal
									etoiles+= vnasal
							else:
								if car in phonoption:
									c+= car+"*"+phonoption[car]+"*"
									etoiles+= car+"*"+phonoption[car]+"*"
								else:
									c+= car
									etoiles+= car
						else:
							c+= car
							etoiles+= car
				# Si on est à la fin de la ligne on saut une ligne en rajoutant \n
				elif j == len(tG[i])-1:
					if etoiles[-2] != "\"":			# je sais pas pourquoi des fois le dernier guillemet ne s'affiche pas (-2 parce que le mot se termine par un espace dans le textgrid)
						c+= '\"\n'
					else:
						c+= "\n"
				# On écrit text = mais pas la suite quand on a rencontré le premier guillemet
				elif not guillemet:
					c+= car

		# On écrit le textgrid qui n'a pas besoin d'être modifié
		else:
			c+= tG[i] + "\n"

	f1 = open("nouveaurecord.TextGrid", "w", encoding = 'utf-8')
	f1.write(c)
	f1.close()

	return etoiles
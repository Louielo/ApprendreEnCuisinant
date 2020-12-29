def phon():
	########## Récupération des phonèmes du mot en SAMPA à partir du textgrid ##########
	import fonction as fc

	# On vérifie l'encoding du fichier, si c'est utf-8 ou utf-16 pour ne pas avoir d'erreurs
	encod = fc.encod(file="final.TextGrid")
	f1 = open("final.TextGrid", "r", encoding=encod)
	praat = f1.read()
	f1.close()

	lignes = praat.split("\n")
	longu = int(lignes[13][-2])		# longueur du nombre de phonème + début du mot et fin du mot

	lignes = lignes[14:14+longu*4]	# Pour récupérer toutes les lignes concernant chaque phonème, le nombre de phonème est stocké dans longu
	# print(lignes)
	lignes = [x.strip(' ') for x in lignes]	# Enlever les espaces au début des lignes parce que c'est pas beau

	phoneme = []

	for i in range (0, len(lignes)):									# On parcourt toutes les lignes du tableau
		if "text" in lignes[i] and "_" not in lignes[i]:				# On regarde seulement les lignes avec text et sans _ pour récupèrer seulement les phonèmes
			for j in range (0, len(lignes[i])-1):						# On parcourt les caractères de chaque lignes
				if lignes[i][j] == "\"":								# Si on a un " ça veut dire que c'est le début du phonème, donc on l'écrit dans le tableau
					if lignes[i][j+1] == "\"":							# Mais si on a rien : "" alors c'est qu'il y a eu une erreur
						print("Erreur : Final.TextGrid ne s'est pas bien enregistré.")
						exit()
					else:
						phoneme.append(lignes[i][j+1])
					if lignes[i][j+2] != "\"":							# Si on a pas "a" par exemple mais "a~" on récupère le deuxième signe
						phoneme[-1] = phoneme[-1] + lignes[i][j+2]
	print('\033[94m'+"\nVotre prononciation en Sampa : "+' '.join(phoneme))

	########## Conversion de SAMPA à API à partir de notre tsv ##########


	f2 = open("SampaToApi.tsv", "r", encoding='utf-8')

	convert = f2.read().split("\n")				# On découpe lignes par lignes puis par tabulations pour avoir un tableau de type [[sampa, api], [sampa, api]]
	f2.close()

	for i in range (0, len(convert)):
		convert[i]=convert[i].split("\t")

	phonapi = ""
	for i in range (len(phoneme)):				# On créé une nouvelle variable avec des symboles api
		for j in range (len(convert)):
			#print("phoneme = "+phoneme[i])
			if phoneme[i] == convert[j][0]:
				phonapi = phonapi + convert[j][1]

	print('\033[94m'+"\nVotre prononciation en Api : "+' '.join(phonapi)+'\033[0m')

	#print("phonapi = "+phonapi)
	######### Comparaison de la prononciation de l'apprenant avec celle du lexique phonétisé #########

	f4 = open("mot.txt", "r", encoding="utf-8")		# Récupération du mot qui a été prononcé
	mot = f4.readline().strip("\n")
	f4.close()

	f3 = open("french.tsv", "r", encoding='utf-8')	# Récupération du lexique phonétique
	lex = f3.read().split("\n")
	f3.close()
	for i in range (0, len(lex)):
		lex[i]=lex[i].split("\t")	

	phonlex = []	# la transcription du lexique
	booleen = True
	newphonapi = []
	phonlexstr= ""
	trouve = False	# booléen pour vérifier si on a déjà trouvé le mot ou pas

	# On va parcourir le lexique à la recherche du mot
	for i in range (0, len(lex)):
		if lex[i][0] == mot:
			trouve = True
			phonlexstr = lex[i][1]
			phonlex = phonlexstr.split(' ')
			if ''.join(phonlex) == phonapi:			# Si la prononciation est exacte pas besoin de vérifier phonème par phonème
				print("Bonne prononciation, on prononce bien : "+phonapi)
			else:
				for y in range(0, len(phonapi)):
					#print(phonapi[y])
					if phonapi[y] != " ":
						newphonapi.append(phonapi[y])
				for k in range(0, len(newphonapi)-1):
					if phonlex[k] != newphonapi[k] and newphonapi[k]!=" " and phonlex[k] != " ":
						print("Votre prononciation : "+phonapi+"\nLa prononciation attendue : "+" ".join(phonlex)+"\nDans ce mot, il faut prononcer le phonème "+phonlex[k]+" et non pas "+newphonapi[k])
						break
			

	if not trouve:
		print("Erreur : Le mot n'est pas trouvé dans le lexique.")
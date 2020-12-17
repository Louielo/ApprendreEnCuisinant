
########## Récupération des phonèmes du mot en SAMPA à partir du textgrid ##########

f1 = open("record.TextGrid", "r", encoding='utf8')
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
				phoneme.append(lignes[i][j+1])
				if lignes[i][j+2] != "\"":							# Si on a pas "a" par exemple mais "a~" on récupère le deuxième signe
					phoneme[-1] = phoneme[-1] + lignes[i][j+2]


########## Conversion de SAMPA à API à partir de notre tsv ##########


f2 = open("SampaToApi.tsv", "r", encoding='utf8')

convert = f2.read().split("\n")				# On découpe lignes par lignes puis par tabulations pour avoir un tableau de type [[sampa, api], [sampa, api]]
f2.close()

for i in range (0, len(convert)):
	convert[i]=convert[i].split("\t")

phonapi = ""
for i in range (len(phoneme)):				# On créé une nouvelle variable avec des symboles api
	for j in range (len(convert)):
		if phoneme[i] == convert[j][0]:
			phonapi = phonapi + convert[j][1]+" "
phonapi = phonapi[:-1]						# On enlève le dernier espace


######### Comparaison de la prononciation de l'apprenant avec celle du lexique phonétisé #########


f3 = open("french.tsv", "r", encoding='utf8')	# Récupération du lexique phonétique
lexiphon = f3.read().split("\n")
f3.close()

f4 = open("mot.txt", "r", encoding='utf8')		# Récupération du mot qui a été prononcé
mot = f4.readline().strip("\n")
print(mot)
print(len(mot))
f4.close()

for i in range (0, len(lexiphon)):
	lexiphon[i]=lexiphon[i].split("\t")

phonlex = []
booleen = True
newphonapi = []
test= ""
for i in range (0, len(lexiphon)):

	if lexiphon[i][0] == mot:
		for g in range(0, len(lexiphon[i][1])):
			if lexiphon[i][1][g] != " ":
				phonlex.append(lexiphon[i][1][g])
				test = test+lexiphon[i][1][g]+" "
		if test[:-1] == phonapi:			# Si la prononciation est exacte pas besoin de vérifier phonème par phonème
			print("Bonne prononciation")
		
		else:
			print(test[:-1], phonapi)
			for y in range(0, len(phonapi)):
				if phonapi[y] != " ":
					newphonapi.append(phonapi[y])
			j= 0
			while booleen:
				for k in range(0, len(newphonapi)-1):
					if phonlex[k] != newphonapi[k] and newphonapi[k]!=" " and phonlex[k] != " ":
						print("Votre prononciation : "+phonapi+"\nLa prononciation attendue : "+str(phonlex)+"\nDans ce mot, il faut prononcer ce phonème : "+phonlex[k])
						booleen = False
						break
				booleen = False
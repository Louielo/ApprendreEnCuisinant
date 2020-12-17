
########## Récupération des phonèmes du mot en SAMPA à partir du textgrid ##########

f1 = open("output.TextGrid", "r", encoding='utf8')
praat = f1.read()

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

print(phoneme)


########## Conversion de SAMPA à API à partir de notre tsv ##########


f2 = open("SampaToApi.tsv", "r", encoding='utf8')

convert = f2.read().split("\n")				# On découpe lignes par lignes puis par tabulations pour avoir un tableau de type [[sampa, api], [sampa, api]]
for i in range (0, len(convert)):
	convert[i]=convert[i].split("\t")

for i in range (len(phoneme)):				# On remplace les symboles sampa par les symboles api
	for j in range (len(convert)):
		if phoneme[i] == convert[j][0]:
			phoneme[i] = convert[j][1]

print(phoneme)

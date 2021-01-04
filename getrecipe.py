
### Fonction getrecipe qui permet de récupérer une recette aléatoire sur le site de Marmiton

def getrecipe():
	from requests import get	# get pour émettre une requete HTTP
	from bs4 import BeautifulSoup	# on utilise la librairie BeautifulSoup pour le webscraping. pip install beautifulsoup4
	# On émet une requete HTTP vers le site de marmiton 

	url = "https://www.marmiton.org/"
	response = get(url)

	if response.status_code == 200 : # on vérifie que la requete ai bien abouti. Le code 200 indique le succés de la requête.
		source = response.text

		soup = BeautifulSoup(source, "html.parser")

		# On récupère le lien de la recette au hasard à l'aide de l'id "random-recipe"

		link = soup.find("a", {"id": "random-recipe"})
		link = link.get('href')

		url = "http://marmiton.org"+link # le nouvel url que l'on va utiliser 
		response = get(url)

		source = response.text
		soup = BeautifulSoup(source, "html.parser")

	else :	# prend en compte tous les autres codes d'erreurs
		print("Impossible de récupérer une recette sur le site de "+url)

	# on créé un fichier recette.txt dans lequel on va enregistrer le texte
	f = open("recette.txt", "w")

	recette = ""
	tabingr = []
	tabingr.append([])	# pour avoir un tableau à deux dimensions de type [[], [], []]

	# On affiche le titre de la recette et les ingrédients mais on ne l'enregistre pas dans le fichier
	# car on va seulement utiliser le texte de la recette pour éviter les erreurs de pos tagging avec corenlp.

	#### Titre de la recette ####
	title = soup.find("h1", {"class": "main-title"})
	title = title.get_text()
	print(title)

	#### Texte de la recette ####
	for text in soup.find_all("li", {"class": "recipe-preparation__list__item"}):
		recette = recette + text.get_text().replace("\t", "")	# on enlève les tabulations

	print(recette+"\n")
	f.write(recette)
	cpt = 0
	cpting = 0

	#### Ingrédients de la recette
	for ingredients in soup.find_all("span", {"class":["ingredient","recipe-ingredient-qt","recipe-ingredient__complement"]}):
		cpt+=1
		if ingredients.get_text() != " " and ingredients.get_text() != "":	#on prend pas en compte quand c'est vide
			tabingr[cpting].append(ingredients.get_text())
		if cpt == 3:	# quand on a récupéré les trois éléments des ingrédients (quantité, valeur, complément) alors on ajoute un nouveau tableau à l'intérieur du tableau
			print(' '.join(tabingr[cpting]))	# on utilise la fonction join de python pour séparer les valeurs par des espaces
			cpt = 0
			cpting+=1
			tabingr.append([])

	f.close()
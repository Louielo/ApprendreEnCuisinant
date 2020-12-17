
from requests import get	# get pour émettre une requete HTTP
from bs4 import BeautifulSoup	# il faut l'installer avant : pip install beautifulsoup4

tablink = []
tabtext = []
tabingr = []

url = "https://www.marmiton.org/"
response = get(url)

if response.status_code == 200 : # on vérifie que la requete ai bien abouti
	source = response.text
# Liste des codes de requete HTTP :
# 200 : succès de la requête ;
# 301 et 302 : redirection, respectivement permanente et temporaire ;
# 401 : utilisateur non authentifié ;
# 403 : accès refusé ;
# 404 : page non trouvée ;
# 500 et 503 : erreur serveur ;
# 504 : le serveur n'a pas répondu.
	soup = BeautifulSoup(source, "html.parser") 	#précise qu'on veut le format lxml

	for link in soup.find_all("a", {"class": "header-main-menu__item"}):
		tablink.append(link.get('href'))

	link = tablink[4]

	url = "http://marmiton.org"+link # faudra trouver un autre moyen de récupérer le début
	response = get(url)

	source = response.text
	soup = BeautifulSoup(source, "html.parser")

else :
	print("Impossible de récupérer une recette sur le site de "+url)


f = open("coreNLP/recette.txt", "w")

# for title in soup.find_all("h1", {"class": "main-title"}):
# 	title = title.get_text()
# 	print("\n"+title+"\n")
# 	print(f.write(title+"\n"))
for text in soup.find_all("li", {"class": "recipe-preparation__list__item"}):
	tabtext.append(text.get_text())
	print(text.get_text())
	print(f.write(text.get_text()+"\n"))
for ingredients in soup.find_all("span", {"class":["ingredient","recipe-ingredient-qt","recipe-ingredient__complement"]}):
	# Séparer les ingrédients quantité et valeur, ne pas mettre les quantités dans le fichier texte pour java mais les afficher dans le cmd.

	#print(ingredients)
		#tabingr.append(ingredients.get_text())
	print(ingredients.get_text())
	print(f.write(ingredients.get_text()))


f.close()
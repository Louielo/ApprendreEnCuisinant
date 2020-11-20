
from requests import get	# get pour émettre une requete HTTP
from bs4 import BeautifulSoup	# il faut l'installer avant : pip install beautifulsoup4
from random import randrange	# pour recette aléatoire


tablink = []
tabtext = []

url = "https://www.marmiton.org/recettes/recherche.aspx?aqt="
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
	soup = BeautifulSoup(source, "lxml") 	#précise qu'on veut le format lxml

for link in soup.find_all("a", {"class": "recipe-card-link"}):
	tablink.append(link.get('href'))
else :
	source = None

alea = randrange(15)

print(tablink[alea])	# on récupère un lien de recette aléatoire

# print(source)

url = "http://marmiton.org"+tablink[alea] # faudra trouver un autre moyen de récupérer le début
response = get(url)

if response.status_code == 200 : # on vérifie que la requete ai bien abouti
	source = response.text
	soup = BeautifulSoup(source, "lxml")
	# print(soup)
else :
	source = None

for text in soup.find_all("li", {"class": "recipe-preparation__list__item"}):
	tabtext.append(text.get_text())
	print(text.get_text())


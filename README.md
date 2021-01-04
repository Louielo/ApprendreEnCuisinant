# ApprendreEnCuisinant

A installer :
- Praat (si possible mettre le .exe dans le dossier sinon modifier le chemin)
- EasyAlign

#installer les bibliothèques utilisées

- Sounddevice : pip install sounddevice
- Scipy : pip install scipy
- Requests : python -m pip install requests
- BeautifulSoup : pip install beautifulsoup4

Pour linux :
- Playsound : pip install playsound
- Parselmouth : pip install praat-parselmouth

Manuel d'utilisation : 
- Lancer main.py
- Lancer CoreNLP lorsque le programme vous le demande. Avant ça, veillez à mettre le fichier texte recette dans le dossier Corenlp. Récupérez les fichiers en sortie (adjectifs.txt, verbes.txt, noms.txt, adverbes.txt) et mettez les dans le dossier principal où les scripts python et main.py se trouvent.
- Si vous n'avez pas pu lancer CoreNLP ou souhaitez choisir les mots à prononcer vous pouvez récupérer des fichiers textes d'exemple dans le dossier FichierCréésExemples. Pour les modifier il suffit d'écrire le mot et de vérifier qu'il soit suivi d'un saut de ligne.
- Suite de main.py en appuyant sur la touche entrée

Important : 
Selon linux ou windows, changer la librairie utilisée dans record.py et pour l'appel au script de praat avec parselmouth
Il faut changer les chemins (dans les scripts praat pour easyalign)

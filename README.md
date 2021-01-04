# ApprendreEnCuisinant


## A installer :
- Praat (si possible mettre le .exe dans le dossier sinon modifier le chemin)
- EasyAlign
<br>

## Installer les bibliothèques utilisées
- Sounddevice : pip install sounddevice
- Scipy : pip install scipy
- Requests : python -m pip install requests
- BeautifulSoup : pip install beautifulsoup4

Pour linux :
- Playsound : pip install playsound
- Parselmouth : pip install praat-parselmouth
<br>

## Modifications importantes
- Selon linux ou windows, le code doit légèrement être modifié car les librairies utilisées ne sont pas les mêmes. Ceci concerne les scripts record.py (l.8-9, l.22-25), praatrun1.py (l.9-16), praatrun2.py.
- Les chemins d’installations de Praat et EasyAlign dans les scripts praat (script1.praat et script2.praat) doivent être modifiés.
<br>

## Manuel d'utilisation : 
- Lancez main.py
- Lancez CoreNLP lorsque le programme vous le demande. Avant ça, veillez à mettre le fichier texte recette dans le dossier Corenlp. Récupérez les fichiers en sortie (adjectifs.txt, verbes.txt, noms.txt, adverbes.txt) et mettez les dans le dossier principal où les scripts python et main.py se trouvent.
- Si vous n'avez pas pu lancer CoreNLP ou souhaitez choisir les mots à prononcer vous pouvez récupérer des fichiers textes d'exemple dans le dossier FichierCréésExemples. Pour les modifier il suffit d'écrire le mot et de vérifier qu'il soit suivi d'un saut de ligne.
- Suite de main.py en appuyant sur la touche entrée

<br>

## Bon apprentissage et bonne cuisine !!

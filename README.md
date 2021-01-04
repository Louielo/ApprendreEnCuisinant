# ApprendreEnCuisinant


## A installer :
- [Praat](https://www.fon.hum.uva.nl/praat/) (si possible mettre le .exe dans le dossier sinon modifier le chemin)
- [EasyAlign](http://latlcui.unige.ch/phonetique/easyalign.php)
<br>

## Installer les bibliothèques utilisées
- [Sounddevice](https://python-sounddevice.readthedocs.io/en/0.4.1/) : 
```bash
pip install sounddevice
```
- [Scipy](https://www.scipy.org/install.html) : 
```bash
pip install scipy
```
- [Requests](https://requests.readthedocs.io/en/master/user/install/#install) : 
```bash
python -m pip install requests
```
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) : 
```bash
pip install beautifulsoup4
```

Pour linux :
- [Playsound](https://pypi.org/project/playsound/) : 
```bash
pip install playsound
```
- [Parselmouth](https://parselmouth.readthedocs.io/en/stable/) : 
```bash
pip install praat-parselmouth
```
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

## Reference :
- [Lexique phonétisé french.tsv](https://gricad-gitlab.univ-grenoble-alpes.fr/pedagogies-multimodales/lexiques-phonetises)
- [CoreNLP](https://stanfordnlp.github.io/CoreNLP/)
- [Marmiton](https://www.marmiton.org/)

## Bon apprentissage et bonne cuisine !!

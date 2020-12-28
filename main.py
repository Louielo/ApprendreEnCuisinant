
# Nos scripts

import getrecipe
import record
import praatrun1

# Pour avoir de la couleur dans l'invite de commande
red = '\033[91m'
bleu = '\033[94m'
norm = '\033[0m'

# On récupère une recette
getrecipe.getrecipe()

# On demande à l'utilisateur de lancer corenlp pour avoir les mots à prononcer
input(bleu+"\n\nVeuilliez maintenant lancer le script Corenlp pour récupérer les mots à prononcer.\n"+red+"ATTENTION : Vérifiez que les fichiers textes créés soient dans le dossier principal."+bleu+"\nLorsque vous êtes prêts, appuyez sur entrée.\n\n"+norm)

# Pour chaque mot
fichiers = ['adjectifs.txt', 'verbes.txt', 'noms.txt', 'adverbes.txt']
with open('mots.txt', 'w') as nf:
    for fname in fichiers:
        with open(fname, encoding="ISO-8859-1") as infile:	# cet encoding qui fonctionne
            nf.write(infile.read())

f = open("mots.txt", "r")
mots = f.readlines()
adj = mots[0]
verb = mots[1]
nom = mots[2]
adv = mots[3]
f.close()

for mot in range(0, len(mots)):
	record.record(mots[mot])

	praatrun1.praatrun1()


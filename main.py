
### Script principal qui va lancer l'application et utiliser les fonctions présentes dans les différents scripts

# Nos scripts
import getrecipe
import record
import praatrun1
import praatrun2
import phon
import fonction as fc

# Pour avoir de la couleur dans l'invite de commande
red = '\033[91m'
bleu = '\033[94m'
norm = '\033[0m'

# On récupère une recette
getrecipe.getrecipe()
print("\nCette recette vient du site www.marmiton.org")

# On demande à l'utilisateur de lancer corenlp pour avoir les mots à prononcer
input(bleu+"\n\nVeuilliez maintenant lancer le script Corenlp pour récupérer les mots à prononcer à partir du fichier recette.txt\n"+red+"ATTENTION : Vérifiez que les fichiers textes créés soient dans le dossier principal."+bleu+"\nLorsque vous êtes prêts, appuyez sur entrée.\n\n"+norm)

# Pour chaque mot
fichiers = ['verbes.txt', 'adjectifs.txt', 'noms.txt', 'adverbes.txt']
with open('mots.txt', 'w', encoding='utf-8') as nf:
    for fname in fichiers:
        with open(fname, encoding="ISO-8859-1") as infile:	# cet encoding qui fonctionne
            nf.write(infile.read())

f = open("mots.txt", "r", encoding='utf-8')
mots = f.readlines()
verb = mots[0]
adj = mots[1]
nom = mots[2]
adv = mots[3]
f.close()

for mot in range(0, len(mots)):
	record.record(mots[mot])

	option = praatrun1.praatrun1()
	print("\n"+bleu+"Les phonèmes en option : "+option+norm)
	praatrun2.praatrun2()
	
	phon.phon()
	if mot < len(mots)-1:
		arret = input(bleu+"\nVoulez vous passer au mot suivant ? (y/n)"+norm)
		if arret == "n":
			break
	# Avant de passer au mot suivant on supprime les textgrids existants (sinon erreurs d'encoding)
	t="record.TextGrid"
	fc.suppr(t)
	t="nouveaurecord.TextGrid"
	fc.suppr(t)
	t="final.TextGrid"
	fc.suppr(t)
import os
import io


### Fonction qui supprime un fichier
def suppr(file):
## on vérifie que le fichier existe
	if os.path.isfile(file):
	    os.remove(file)	# on le supprime
	else:
	    print("Erreur: %s not found" % myfile)


### Fonction qui vérifie l'encoding d'un fichier
def encod(file):
	encodings = ['utf-8', 'utf-16BE']
	for e in encodings:
		try:
			fh = io.open(file, 'r', encoding=e)
			fh.readlines()
			fh.seek(0)
		except UnicodeDecodeError:
			print('got unicode error with %s , trying different encoding' % e)
		else:
			print('opening '+file+' with encoding:  %s ' % e)
			return e
			break  
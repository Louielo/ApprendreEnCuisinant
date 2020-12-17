
import sounddevice as sd
from scipy.io.wavfile import write
#from playsound import playsound 	# pour linux
import os

f = open("coreNLP/adjectifs.txt", "r")
adj = f.readline()
f.close()

fs = 22000  # fréquence par défaut qui ne prend pas trop de place sur le disque
duree = 2  # Durée de l'enregistrement

while True :	# tant que l'utilisateur n'est pas content de sa prononciation il peut se réenregistrer
	record = sd.rec(int(duree * fs), samplerate=fs, channels=2) # commande pour enregistrer avec sounddevice

	print("prononcez le mot "+adj+" ...")
	sd.wait()  # on attend que l'enregistrement se termine
	write('record.wav', fs, record)  # enregistre en wav

	# Sur windows : 
	os.startfile("record.wav") # pour faire écouter à l'utilisateur ce qu'il a prononcé
	# Sur linux : on utilise la bibliothèque playsound
	#playsound('record.wav')
	avis = input("Voulez vous prononcer le mot encore une fois ? y/n ")
	if avis == "n" :
		break

f = open("mot.txt", "w")
f.write(adj)

#commandes pour installer les bibliothèques utilisées
#pip install sounddevice
#pip install scipy
#pip install playsound # pour linux
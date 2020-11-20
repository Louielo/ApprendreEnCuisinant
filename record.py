
import sounddevice as sd
from scipy.io.wavfile import write
import os

fs = 44100  # fréquence
seconds = 5  # Durée de l'enregistrement

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
print("Prononcez le mot..")
sd.wait()  # on attend que l'enregistrement se termine
print("Mot enregistré")
write('record.wav', fs, myrecording)  # enregistre en wav
os.startfile("record.wav")

#commandes pour installer les bibliothèques utilisées
#pip install sounddevice
#pip install scipy
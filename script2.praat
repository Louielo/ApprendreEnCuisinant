

# On ouvre le mot écrit et l'enregistrement audio
Read from file: "record.wav"
Read from file: "nouveaurecord.TextGrid"

selectObject: "Sound record"
plusObject: "TextGrid nouveaurecord"



# Troisième étape de EasyAlign

runScript: "C:\Users\Louis\Praat\plugin_easyalign\align_sound.praat", "ortho", "phono", "yes", "fra", "}-';(),.?¿", "no", "yes", "no", 90, "yes", "no"

# On enregistre le résultat final
selectObject: "TextGrid nouveaurecord"
Save as text file: "final.TextGrid"

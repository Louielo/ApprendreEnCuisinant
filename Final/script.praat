# On ouvre le mot écrit et l'enregistrement audio
Read from file: "record.wav"
Read Strings from raw text file: "mot.txt"

# Première étape de EasyAlign
selectObject: "Sound record"
plusObject: "Strings mot"
runScript: "C:\Users\Lou\Praat\plugin_easyalign\utt_seg2.praat", "ortho", "no"

# Seconde étape de EasyAlign
runScript: "C:\Users\Lou\Praat\plugin_easyalign\phonetize_orthotier2.praat", "ortho", "phono", "fra", "yes", "no"
selectObject: "TextGrid record"

# Troisième étape de EasyAlign
selectObject: "Sound record"
plusObject: "TextGrid record"
runScript: "C:\Users\Lou\Praat\plugin_easyalign\align_sound.praat", "ortho", "phono", "yes", "fra", "}-';(),.?¿", "no", "yes", "no", 90, "yes", "no"

# On enregistre le résultat final
selectObject: "TextGrid record"
Save as text file: "record.TextGrid"

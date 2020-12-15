# On ouvre le mot écrit et l'enregistrement audio
Read from file: "output.wav"
Read Strings from raw text file: "mot.txt"

# Première étape de EasyAlign
selectObject: "Sound output"
plusObject: "Strings mot"
runScript: "C:\Users\Lou\Praat\plugin_easyalign\utt_seg2.praat", "ortho", "no"

# Seconde étape de EasyAlign
runScript: "C:\Users\Lou\Praat\plugin_easyalign\phonetize_orthotier2.praat", "ortho", "phono", "fra", "yes", "no"
selectObject: "TextGrid output"

# Troisième étape de EasyAlign
selectObject: "Sound output"
plusObject: "TextGrid output"
runScript: "C:\Users\Lou\Praat\plugin_easyalign\align_sound.praat", "ortho", "phono", "yes", "fra", "}-';(),.?¿", "no", "yes", "no", 90, "yes", "no"

# On enregistre le résultat final
selectObject: "TextGrid output"
Save as text file: "G:\alao\praat\output.TextGrid"

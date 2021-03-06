# On ouvre le mot écrit et l'enregistrement audio
Read from file: "record.wav"
Read Strings from raw text file: "mot.txt"

# Première étape de EasyAlign
selectObject: "Sound record"
plusObject: "Strings mot"
# pour windows
runScript: "C:\users\louis\Praat\plugin_easyalign\utt_seg2.praat", "ortho", "no"
# runScript: "EA/utt_seg2.praat", "ortho", "no"

# Seconde étape de EasyAlign
runScript: "C:\Users\Louis\Praat\plugin_easyalign\phonetize_orthotier2.praat", "ortho", "phono", "fra", "yes", "no"
# runScript: "EA/phonetize_orthotier2.praat", "ortho", "phono", "fra", "yes", "no"
selectObject: "TextGrid record"

# On enregistre le TextGrid
Save as text file: "record.TextGrid"
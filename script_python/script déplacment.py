import json
import shutil
import os

source = r'C:\Users\ymaas\OneDrive\Documents\test_python'

destination = r'C:\Users\ymaas\OneDrive\Documents\test_reception'

files = os.listdir(source)
i = 0

#déplace les fichiers vers le nouveau répertoire
for file in files :
    new_place = shutil.move(f"{source}/{file}", destination)
#renomme les fichiers en covid i    
    for filename in files:
            i = i + 1
            os.rename(os.path.join(destination,filename), os.path.join(destination, 'covid' + str(i) +'.json'))
        

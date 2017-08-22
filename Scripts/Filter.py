import sys
import os.path
import pandas as pd
import os
os.chdir(sys.argv[1]) #Select your working directory
cwd = os.getcwd()
file = 'sample_Sirene'
B=True
while B:
    binary=input("Par défaut, le programme s'execute avec le sample, voulez-vous utiliser la base complète ?(y/n)")
    if binary=='y':
        file='dataset_Sirene'
        B=False
    if binary=='n':
        B=False
   
text_file = open(cwd+"/Scripts/info.txt", "w")
text_file.write(file)
text_file.close()

var_filter='APEN700'
l=['7211Z','6201Z','7219Z','7220Z','6311Z','6312Z','6202A','6202B','6203Z','6209Z']
v=['Biotechnologie',
   'Recherche-développement en autres sciences physiques et naturelles',
   'Recherche-développement en sciences humaines et sociales',
   'Traitement de données, hébergement et activités connexes',
   'Programmation informatique',
   'Portails Internet',
   "Conseil en systèmes et logiciels informatiques",
   "Tierce maintenance de systèmes et d'applications informatiques",
   "Gestion d'installations informatiques",
   'Autres activités informatiques']
print("Chargement de la base avec les secteurs d'activité:\n"+'\n'.join(v))
print('/!\ Si vous executez le programme avec la base complète Sirene, le chargement peut être relativement long')

if os.path.isfile(cwd+'/Sirene_data/'+file+'_subset.json')==False:
    iter_csv = pd.read_csv(cwd+'/Sirene_data/'+file+'.csv', 
                               iterator=True, chunksize=1000,
                               error_bad_lines=False,encoding='ISO-8859-1',
                               sep=';')
    df=pd.concat(chunk[chunk[var_filter].isin(l)] for chunk in iter_csv)

    df.to_json(cwd+'/Sirene_data/'+file+'_subset.json')

print('Subset SIRENE récupéré.')

#%%


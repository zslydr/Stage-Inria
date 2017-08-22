import sys

import pandas as pd
import os
os.chdir(sys.argv[1]) #Select your working directory
cwd = os.getcwd()

var_filter='APEN700'
l=['7211Z','6201Z','7219Z','7220Z','6311Z','6312Z','6202A','6202B','6203Z','6209Z']
print('Loading variables\n'+'\n'.join(l))
iter_csv = pd.read_csv(cwd+'/Sirene_data/sample.csv', 
                           iterator=True, chunksize=1000,
                           error_bad_lines=False,encoding='ISO-8859-1',
                           sep=';')

df=pd.concat(chunk[chunk[var_filter].isin(l)] for chunk in iter_csv)

df.to_json(cwd+'/subset_SIRENE.json')

print('subset from Sirene dataset recovered')


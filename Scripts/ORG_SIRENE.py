import sys
import os
os.chdir(sys.argv[1]) #Select your working directory
cwd = os.getcwd()
import codecs
import pandas as pd
import os.path
import numpy as np
import matplotlib.pyplot as plt
accents=['à','á','â','ç','è','é','ê','ë','ì','í','î','ï','ñ','ò','ó','ô','ù','ú','û','ü','ý','ÿ']
spec=accents+['/','*',',','.','?']
stopwords=['de','la','les','des','le','du']
from lib.Functions import *

file = open(cwd+"/Scripts/info.txt", "r").read()


sys.stdout.write('\r')
sys.stdout.write("[%-20s] %d%%" % ('='*2, 5*2))
sys.stdout.flush()

anHALytics={}
for x in os.listdir(cwd+'/data/json'):
    if (x=='ORGANISATION_NAME.json') or (x=='ORGANISATION.json'):
        anHALytics[x[:-5]]=pd.read_json(cwd+'/data/json/'+x)
   
subset_SIRENE=pd.read_json(cwd+'/Sirene_data/subset/'+file+'_subset.json')
subset_SIRENE=subset_SIRENE[subset_SIRENE['SIEGE']==1]

sys.stdout.write('\r')
sys.stdout.write("[%-20s] %d%%" % ('='*8, 5*8))
sys.stdout.flush()

liste_mots=pd.read_csv(cwd+'/data/liste_mots.txt',sep='\t',encoding='"ISO-8859-1"')


mots_accent=[]
for x in list(liste_mots['mot']):
    if len(set(x).intersection(set(accents)))>0:
        mots_accent.append(x)

import unicodedata

dico_mot_accent={}

for x in mots_accent:
    for i,y in enumerate(x):
        if y in accents:
            break
    dico_mot_accent[unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('utf-8')]=x[:i]+x[i+1:]

sys.stdout.write('\r')
sys.stdout.write("[%-20s] %d%%" % ('='*12, 5*12))
sys.stdout.flush()

subset_SIRENE['recherche'] = subset_SIRENE['NOMEN_LONG'].apply(lambda x: normalize(x,spec,stopwords,dico_mot_accent))

anHALytics['ORGANISATION_NAME']['recherche']=anHALytics['ORGANISATION_NAME']['name'].apply(lambda x: normalize(x,spec,stopwords,dico_mot_accent))

merged=pd.merge(subset_SIRENE[subset_SIRENE['recherche']!=''],
                anHALytics['ORGANISATION_NAME'][anHALytics['ORGANISATION_NAME']['recherche']!=''],
                on='recherche')

orgid=merged.groupby(['organisationID']).SIREN.count()[merged.groupby(['organisationID']).SIREN.count()<2].index.values


org_SIREN=merged[merged['organisationID'].isin(orgid)][['organisationID','SIREN']]

sys.stdout.write('\r')
sys.stdout.write("[%-20s] %d%%" % ('='*16, 5*16))
sys.stdout.flush()

subset_SIRENE['recherche_SIGLE'] = subset_SIRENE['SIGLE'].apply(lambda x: normalize(x,spec,stopwords,dico_mot_accent,sigle=True))

anHALytics['ORGANISATION_NAME']['recherche_SIGLE']=anHALytics['ORGANISATION_NAME']['name'].apply(lambda x: normalize(x,spec,stopwords,dico_mot_accent,sigle=True))

merged_SIGLE=pd.merge(subset_SIRENE[subset_SIRENE['recherche_SIGLE']!=''],
                anHALytics['ORGANISATION_NAME'][anHALytics['ORGANISATION_NAME']['recherche_SIGLE']!=''],
                on='recherche_SIGLE')


orgid_SIGLE=merged_SIGLE.groupby(['organisationID']).SIREN.count()[merged_SIGLE.groupby(['organisationID']).SIREN.count()<2].index.values


org_SIREN_SIGLE=merged_SIGLE[merged_SIGLE['organisationID'].isin(orgid_SIGLE)][['organisationID','SIREN']]

sys.stdout.write('\r')
sys.stdout.write("[%-20s] %d%%" % ('='*18, 5*18))
sys.stdout.flush()
org_SIREN=org_SIREN.append(org_SIREN_SIGLE)

org_SIREN=org_SIREN.drop_duplicates(['SIREN','organisationID'])

org_SIREN.index=[i for i in range(org_SIREN.shape[0])]

org_SIREN.to_json(cwd+'/data/json/ORG_SIREN.json')

sys.stdout.write('\r')
sys.stdout.write("[%-20s] %d%%" % ('='*20, 5*20))
sys.stdout.flush()
print(' Execution completed.')
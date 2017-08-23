# Stage-Inria

Les notebooks 1 et 2 contiennent des représentations plotly que github ne supporte pas.

Voici les liens pour les ouvrir:

Notebook#1 : http://nbviewer.jupyter.org/github/zslydr/Stage-Inria/blob/master/Notebooks/Notebook%231.ipynb

Notebook#2 : http://nbviewer.jupyter.org/github/zslydr/Stage-Inria/blob/master/Notebooks/Notebook%232.ipynb

## Exécution :

Pour exécuter les scripts, exécutez le fichier run:
```shell
$sh run.sh
```
Lors de l'exécution le choix de la base de données à utiliser vous sera demandé.
Le répertoire github contient uniquement le sample de la base Sirene. Pour utiliser la base complète, il faut la télécharger (8go+), et extraire le fichier .csv dans le dossier data_Sirene. 

Lien pour télécharger la base Sirene:

https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/

Le subset créé de la base Sirene se trouve dans le dossier /Sirene_data/subset

La table créée ORG_SIRENE du schéma relationnel se trouve dans le dossier /data/json

## Description

Le programme extrait un subset de la base Sirene en fonction du code APE (Activité Principal de l'Entreprise), car la base complete est très lourde (plus de 10 millions de lignes et 100 variables).

Ensuite le programme relie la base Sirene avec la table ORGANISTION de la base anHALytics comme indiqué dans le schéma relationnel.
En se basant sur la variable NOMEN_LONG de la base Sirene et sur la variable name de la table ORGANISATION_NAME, on peut retrouver certains noms qui sont les mêmes en normalisant le texte.
La fonction de normalisation se trouve dans le fichier /Scripts/lib/Function.py et peut être éditer à tout moment pour proposer des améliorations.

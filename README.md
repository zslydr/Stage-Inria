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
Le répertoire contient uniquement le sample de la base Sirene. Pour utiliser la base complète, il faut la télécharger (8go+), l'extraire le fichier .csv dans le dossier data_Sirene et la renommer "dataset_Sirene.csv".

Lien pour télécharger la base Sirene:

https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/

Le subset créé de la base Sirene se trouve dans le dossier /Sirene_data/subset

La table créée ORG_SIRENE du schéma relationnel se trouve dans le dossier /data/json

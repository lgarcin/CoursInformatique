#!/usr/bin/env python
# coding: utf-8

# # Tables

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///../../_databases/dummy.db')


# On ne traitera que d'un certain type de bases de données appelées bases de données **relationnelles**. Les données y sont stockées sous formes de **tables** (ou **relations**) pouvant avoir des liens entre elles.
# 
# Dans ce qui suit, on dispose d'une base de données de films. Voici par exemple la table `films` de cette base de données.

# In[2]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films\n')


# Cette table comporte cinq **colonnes** (ou **attributs**) : `id`, `titre`, `annee`, `duree` et `realisateur_id`. Chaque **ligne** est aussi appelé un **enregistrement**. On a volontairement limité l'affichage aux cinq premiers enregistrements.
# 
# ```{note}
# La première colonne `id` est un **identifiant** permettant d'identifier chaque ligne de manière unique. La dernière colonne est un également un identifiant faisant référence à une autre table.
# <!-- TODO Mettre un lien vers la section concernée. -->
# ```
# 
# Voilà également la table `realisateurs` de cette base de données.

# In[3]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM realisateurs\n')


# On appelle **domaine** d'un attribut l'ensemble des valeurs prises par cet attribut.
# 
# <!-- TODO Trouver un exemple -->
# 
# Chaque attribut d'une table possède un **type**. Par exemple, la colonne `titre` de la table `films` est du type *chaîne de caractères* tandis que la colonne `annee` de la table `films` est du type *entier*.
# 
# On condense les informations sur les tables à l'aide d'un **schéma de tables** faisant apparaître chaque table avec ses attributs et leurs types.
# 
# ```{mermaid}
# erDiagram
#   films {
#     int     id
#     string  titre
#     int     annee
#     int     duree
#     int     realisateur_id
#   }
# 
#   realisateurs {
#     int     id
#     string  nom
#     string  pays
#   }
# ```

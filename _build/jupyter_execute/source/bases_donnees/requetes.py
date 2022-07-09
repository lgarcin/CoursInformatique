#!/usr/bin/env python
# coding: utf-8

# # Requêtes
# 
# Pour retrouver des informations dans une base de données, on effectue ce qu'on appelle des **reqûetes** décrites dans un langage approprié. Le langage que nous utiliserons est le langage **SQL** (Structured Query Language). Une requête permet de renvoyer une nouvelle table à partir de tables stockées dans la base de données.

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///../../_databases/dummy.db')


# ## Sélection
# 
# Pour sélectionner les enregistrements d'une table dont les attributs vérifient une certaine condition on utilise la requête `SELECT` assortie d'une clause `WHERE`.

# In[2]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films WHERE annee < 1980\n')


# On dispose d'opérateurs logiques pour construire des conditions plus complexes.

# In[3]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films WHERE annee >= 1975 AND annee < 1990\n')


# La condition peut porter sur plusieurs colonnes.

# In[4]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films WHERE annee > 1980 OR duree <= 120\n')


# ## Projection
# 
# La requête `SELECT` permet également de sélectionner non les lignes mais les colonnes d'une table.

# In[5]:


get_ipython().run_cell_magic('sql', '', 'SELECT titre FROM films\n')


# ```{note}
# L'astérique `*` que l'on a utilisé jusqu'à maintenant permet de sélectionner toutes les colonnes d'une table.
# ```
# 
# On peut sélectionner plusieurs colonnes d'une table.

# In[6]:


get_ipython().run_cell_magic('sql', '', 'SELECT titre, duree FROM films\n')


# On peut également combiner les requêtes de sélection et de projection (sélection de lignes **et** de colonnes).

# In[7]:


get_ipython().run_cell_magic('sql', '', 'SELECT titre, annee FROM films WHERE annee >= 1990\n')


# ## Renommage
# 
# On peut renommer les colonnes et les tables à l'aide du mot-clé `AS`.

# In[8]:


get_ipython().run_cell_magic('sql', '', 'SELECT nom AS name, pays AS country FROM realisateurs\n')


# ## Mots-clés divers
# 
# Le mot clé `LIMIT` que nous avons utilisé depuis le début de ce chapitre pour des raisons cosmétiques permet de limiter le nombre d'enregistrements renvoyés par une requête. La requête suivante renvoie les 10 premiers enregistrements de la table `films`.

# In[9]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films LIMIT 10\n')


# ___
# 
# Dans le même ordre d'idée, le mot-clé `OFFSET` permet de retourner les enregistrements d'une requête à partir d'un certain rang. La requête suivante permet d'ignorer les 3 premiers enregistrements de la table `films` et de renvoyer les 5 suivants.

# In[10]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films LIMIT 5 OFFSET 3\n')


# ___
# 
# Une clause `ORDER BY` permet d'ordonner les résultats d'une requête. Si le type utilisé dans cette clause est textuel, les enregistrements sont ordonnées par l'ordre lexicographique.

# In[11]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films ORDER BY titre\n')


# Par défaut les enregistrements sont renvoyés par ordre croissant. On peut utiliser les mots clés `ASC` (ascendant) et `DESC` (descendant) si on veut spécifier l'ordre.

# In[12]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films ORDER BY titre ASC\n')


# In[13]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films ORDER BY titre DESC\n')


# On peut utiliser plusieurs critères de tris successifs. Dans la requête suivante, les résultats sont triés par année croissante puis par titre décroissant.

# In[14]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films ORDER BY annee, titre DESC\n')


# ___
# 
# Le mot clé `DISTINCT` permet de supprimer les doublons dans le résultat d'une requête.

# In[15]:


get_ipython().run_cell_magic('sql', '', 'SELECT nom, pays FROM realisateurs\n')


# In[16]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT pays FROM realisateurs\n')


# ___
# 
# On peut combiner tous les mots clés précédents pour effectuer des requêtes complexes.

# In[17]:


get_ipython().run_cell_magic('sql', '', 'SELECT titre, annee FROM films\nWHERE annee > 1980 OR duree > 150\nORDER BY duree DESC\nLIMIT 10\n')


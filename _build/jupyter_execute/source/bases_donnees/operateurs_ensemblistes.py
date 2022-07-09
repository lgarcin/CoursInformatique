#!/usr/bin/env python
# coding: utf-8

# # Opérateurs ensemblistes

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite://')


# In[2]:


get_ipython().run_cell_magic('sql', '', 'DROP TABLE IF EXISTS t1;\nDROP TABLE IF EXISTS t2;\nCREATE TABLE t1 (col_a varchar(10), col_b int);\nCREATE TABLE t2 (col_c varchar(10), col_d int);\nINSERT INTO t1 VALUES\n("abc", 1),\n("def", 2),\n("ghi", 3);\nINSERT INTO t2 VALUES\n("abc", 3),\n("def", 2);\n')


# Dans cette section, on considère les deux tables `t1` et `t2` suivantes.

# In[3]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM t1\n')


# In[4]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM t2\n')


# ## Union, intersection, différence
# 
# Comme son nom l'indique l'opérateur ensembliste `UNION` permet de créer la **réunion** de deux tables. Plus précisément, cet opérateur crée une table dont les lignes figurent dans l'une des deux tables.

# In[5]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM t1\nUNION\nSELECT * FROM t2\n')


# ___
# 
# L'opérateur `INTERSECT` permet de créer l'**intersection** de deux tables, c'est-à-dire la table dont les lignes figurent dans les deux tables à la fois.

# In[6]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM t1\nINTERSECT\nSELECT * FROM t2\n')


# ___
# 
# Enfin, l'opérateur `EXCEPT` crée la différence de deux tables, c'est-à-dire la table dont les lignes figurent dans la première table mais pas dans la seconde.

# In[7]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM t1\nEXCEPT\nSELECT * FROM t2\n')


# ___
# 
# ```{note}
# A chaque fois, les noms des colonnes de la table résultante sont les noms de la **première** table.
# ```
# 
# ```{warning}
# Le nombre de colonnes des deux tables intervenant dans une union, une intersection ou une différence doit être le même.
# ```

# In[8]:


get_ipython().run_cell_magic('sql', '', 'SELECT col_a FROM t1\nUNION\nSELECT col_c, col_d FROM t2\n')


# ## Produit cartésien
# 
# On peut effectuer le produit cartésien de deux tables (ou plus) à l'aide de la commande suivante.

# In[9]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM t1, t2\n')


# Les lignes de la table résultante sont formées des lignes de la première table appariées à chacune des lignes de la seconde table.
# 
# On peut sélectionner uniquement certaines colonnes de chacune des deux tables comme le montre l'example suivant.

# In[10]:


get_ipython().run_cell_magic('sql', '', 'SELECT col_a, col_d FROM t1, t2\n')


# <!-- TODO Introduire la syntaxe table.nom en cas d'ambiguïté -->

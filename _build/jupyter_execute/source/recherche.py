#!/usr/bin/env python
# coding: utf-8

# # Algorithmes de recherche
# 
# En informatique, un tableau est une structure de données représentant une séquence finie d'éléments auxquels on peut accéder par leur position dans la séquence. On utilisera des listes Python pour représenter ces tableaux. On peut également remarquer qu'une chaîne de caractères est un tableau de caractères.
# 
# On s'intéresse dans ce paragraphe à divers algorithmes permettant de traiter des tableaux ou de retrouver de l'information dans ceux-ci.
# 
# ## Recherche d'un élément
# 
# On cherche à savoir si une valeur donnée fait bien partie des éléments d'un tableau. On parcourt tout simplement ce tableau et on renvoie `True` dès qu'on trouve cette valeur dans le tableau. Si la valeur n'a pas été trouvée à la fin du parcours, on renvoie `False`.

# In[1]:


def appartient(valeur, tableau):
    for element in tableau:
        if element == valeur:
            return True
    return False


# In[2]:


appartient('Alice', ['Alice', 'Bob', 'Charles-Antoine'])


# In[3]:


appartient('Dédé', ['Alice', 'Bob', 'Charles-Antoine'])


# ```{note}
# Le langage Python dispose de l'opérateur `in` pour déterminer si une valeur appartient à une liste.
# ```

# In[4]:


'Alice' in ['Alice', 'Bob', 'Charles-Antoine']


# In[5]:


'Dédé' in ['Alice', 'Bob', 'Charles-Antoine']


# On peut modifier l'algorithme precédent afin qu'il renvoie l'indice du tableau où on a trouvé la valeur recherché et `None` si la valeur n'a pas été trouvée.

# In[6]:


def indice(valeur, tableau):
    for i in range(len(tableau)):
        if tableau[i] == valeur:
            return i
    return None


# In[7]:


indice(2, [5, 4, 1, 2, 3])


# In[8]:


print(indice(6, [5, 4, 1, 2, 3]))


# ```{note}
# La méthode `index` de la classe `list` permet de déterminer l'indice d'une valeur dans une liste.
# ```

# In[9]:


[5, 4, 1, 2, 3].index(2)


# In[10]:


[5, 4, 1, 2, 3].index(6)


# ## Recherche du maximum

# In[11]:


def maximum(tableau):
    m = None
    for element in tableau:
        if m == None or m < element:
            m = element
    return m


# In[12]:


maximum([4, 5, 8, 1, 3])


# In[13]:


print(maximum([]))


# In[14]:


def argmax(tableau):
    index = None
    for i in range(len(tableau)):
        if index == None or tableau[index] < tableau[i]:
            index = i
    return index


# In[15]:


argmax([4, 5, 8, 1, 3])


# In[16]:


print(argmax([]))


# In[17]:


def second_maximum(tableau):
    m1 = None
    m2 = None
    for element in tableau:
        if m1 == None or m1 < element:
            m2 = m1
            m1 = element
        elif m2 == None or m2 < element:
            m2 = element
    return m2


# In[18]:


second_maximum([4, 5, 8, 1, 3])


# In[19]:


print(second_maximum([]))


# In[20]:


print(second_maximum([2]))


# ## Comptage des éléments d'un tableau

# In[21]:


def comptage(tableau):
    d = {}
    for element in tableau:
        if element in d:
            d[element] += 1
        else:
            d[element] = 1
    return d


# In[22]:


comptage(['Alice', 'Bob', 'Alice', 'Charles', 'Charles', 'Alice'])


# ## Recherche d'un motif dans une chaîne

# In[23]:


def recherche_motif(motif, chaine):
    n = len(chaine)
    m = len(motif)
    for ind in range(n-m+1):
        nb = 0
        while nb < m and chaine[ind+nb] == motif[nb]:
            nb +=1
        if nb == m:
            return True
    return False


# In[24]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc

rc('animation', html='jshtml')


class Recherche:

    def __init__(self, motif, chaine):
        self.chaine = chaine
        self.motif = motif
        self.width = 10

        self.fig = plt.figure(figsize=(len(chaine), 3))
        plt.axis('off')
        plt.axis('equal')
        plt.axis([0, len(chaine) * self.width, 0, 3*self.width])

        self.rectangles_chaine = [plt.gca().add_patch(plt.Rectangle(
            [i * self.width, 0], 9, 9, color='b')) for i in range(len(chaine))]
        self.rectangles_motif = [plt.gca().add_patch(plt.Rectangle(
            [i * self.width, 2*self.width], 9, 9, color='y')) for i in range(len(motif))]
        self.annotations_chaine = [
            plt.gca().annotate(chaine[i], np.array([i * self.width, 0]) + np.array([(self.width - 1) * .5, (self.width - 1) * .5]), color='w',
                               weight='bold', fontsize=20,
                               ha='center',
                               va='center') for i in
            range(len(chaine))]
        self.annotations_motif = [
            plt.gca().annotate(motif[i], np.array([i * self.width, 2*self.width]) + np.array([(self.width - 1) * .5, (self.width - 1) * .5]), color='w',
                               weight='bold', fontsize=20,
                               ha='center',
                               va='center') for i in
            range(len(motif))]

    def move_up(self, i):
        self.rectangles_chaine[i].set_xy(
            np.array(self.rectangles_chaine[i].get_xy()) + np.array([0, self.width]))
        self.annotations_chaine[i].set_position(
            np.array(self.annotations_chaine[i].get_position()) + np.array([0, self.width]))
        yield

    def move_down(self, i, j):
        for k in range(i, j):
            self.rectangles_chaine[k].set_xy(
                np.array(self.rectangles_chaine[k].get_xy()) - np.array([0, self.width]))
            self.annotations_chaine[k].set_position(
                np.array(self.annotations_chaine[k].get_position()) - np.array([0, self.width]))
        yield

    def move_right(self):
        for rect in self.rectangles_motif:
            rect.set_xy(np.array(rect.get_xy()) + np.array([self.width, 0]))
        for ann in self.annotations_motif:
            ann.set_position(np.array(ann.get_position()) +
                             np.array([self.width, 0]))
        yield

    def win(self, i, j):
        for k in range(i, j):
            self.rectangles_chaine[k].set_color('g')
        yield

    def lose(self):
        for rect in self.rectangles_chaine:
            rect.set_color('r')
        yield

    def recherche_chaine(self):
        yield
        n = len(self.chaine)
        m = len(self.motif)
        for ind in range(n - m + 1):
            nb = 0
            while nb < m and self.chaine[ind + nb] == self.motif[nb]:
                yield from self.move_up(ind+nb)
                nb += 1
            if nb == m:
                yield from self.win(ind, ind+m)
                break
            yield from self.move_down(ind, ind+nb)
            if ind < n-m:
                yield from self.move_right()
            else:
                yield from self.lose()

    def animate(self, i):
        pass

    def get_animation(self):
        ani = FuncAnimation(
            self.fig, self.animate, frames=self.recherche_chaine, save_count=500)
        plt.close()
        return ani


# In[25]:


recherche_motif("pipa", "pitapipapa")


# In[26]:


Recherche("pipa", "patapipapa").get_animation()


# In[27]:


recherche_motif("tapa", "patapipapa")


# In[28]:


Recherche("tapa", "patapipapa").get_animation()


# ## Recherche des deux valeurs les plus proches d'un tableau

# In[29]:


def plus_proches_valeurs(tableau):
    valeurs = None
    for i in range(len(tableau)):
        for j in range(i+1, len(tableau)):
            if valeurs == None or abs(tableau[i] - tableau[j]) < abs(valeurs[0] - valeurs[1]):
                valeurs = tableau[i], tableau[j]
    return valeurs


# In[30]:


plus_proches_valeurs([7, 4, 9, 13])


# In[31]:


print(plus_proches_valeurs([]))


# In[32]:


print(plus_proches_valeurs([7]))


# ## Tri à bulles
# 
# Le **tri à bulles** fait partie des algorithmes de tri classiques. Trier un tableau consiste à ordonner ses éléments du plus petit au plus grand. On suppose donc que les éléments du tableau sont à valeurs dans un ensemble muni d'une relation d'ordre total.
# 
# Le tri à bulles consiste à déplacer les éléments du plus grand au plus petit vers la fin du tableau comme des bulles d'air dans un liquide. Plus précisément :
# 
# * on parcourt le tableau en comparant les couples d'éléments consécutifs ;
# * si deux éléments consécutifs ne sont pas dans le bon ordre, on les échange ;
# * à la fin de ce premiers parcours du tableau, on peut garantir que le plus grand élément du tableau est en dernière position ;
# * on répète alors ce qui précède sur le tableau privé de son dernier élément et ainsi de suite jusqu'à tri complet du tableau.

# In[33]:


from matplotlib import rc
from matplotlib.pyplot import gca, figure, axis, close, Rectangle
from matplotlib.animation import FuncAnimation
from numpy import array

rc('animation', html='jshtml')


class TriBulles:
    def __init__(self, tab):
        N = len(tab)
        self.tab = tab.copy()
        self.width = 10

        self.fig = figure(figsize=(len(self.tab), 3))
        axis('off')
        axis('equal')
        axis([0, len(self.tab) * self.width, 0, self.width])

        self.rectangles = [gca().add_patch(Rectangle(array([i*self.width, 0]), self.width-1, self.width-1, fc='b'))
                           for i in range(N)]
        self.annotations = [gca().annotate(self.tab[i], array([i*self.width, 0])+array([(self.width-1)*.5, (self.width-1)*.5]), color='w',
                                           weight='bold', fontsize=20,
                                           ha='center',
                                           va='center') for i in range(N)]
        self.indices = [n for n in range(N)]

    def move_vertical(self, i, j):
        for _ in range(self.width):
            self.rectangles[i].set_xy(
                array(self.rectangles[i].get_xy())-array([0, 1]))
            self.annotations[i].set_position(
                array(self.annotations[i].get_position())-array([0, 1]))
            self.rectangles[j].set_xy(
                array(self.rectangles[j].get_xy())+array([0, 1]))
            self.annotations[j].set_position(
                array(self.annotations[j].get_position())+array([0, 1]))
            yield

    def move_horizontal(self, i, j):
        for _ in range(self.width):
            self.rectangles[i].set_xy(
                array(self.rectangles[i].get_xy())+array([1, 0]))
            self.annotations[i].set_position(
                array(self.annotations[i].get_position())+array([1, 0]))
            self.rectangles[j].set_xy(
                array(self.rectangles[j].get_xy())-array([1, 0]))
            self.annotations[j].set_position(
                array(self.annotations[j].get_position())-array([1, 0]))
            yield

    def set_color(self, i, j, color):
        self.rectangles[i].set_color(color)
        self.rectangles[j].set_color(color)
        yield

    def freeze_color(self, i, color):
        self.rectangles[i].set_color(color)
        yield

    def tri(self):
        n = len(self.tab)
        yield
        for i in reversed(range(n)):
            for j in range(i):
                if self.tab[j+1] < self.tab[j]:
                    yield from self.set_color(self.indices[j], self.indices[j+1], 'r')
                    yield from self.move_vertical(self.indices[j], self.indices[j+1])
                    yield from self.move_horizontal(self.indices[j], self.indices[j+1])
                    yield from self.move_vertical(self.indices[j+1], self.indices[j])
                    yield from self.set_color(self.indices[j], self.indices[j+1], 'b')
                    self.tab[j], self.tab[j+1] = self.tab[j+1], self.tab[j]
                    self.indices[j], self.indices[j +
                                                  1] = self.indices[j+1], self.indices[j]
                else:
                    yield from self.set_color(self.indices[j], self.indices[j+1], 'y')
                    for _ in range(self.width):
                        yield
                    yield from self.set_color(self.indices[j], self.indices[j+1], 'b')
            yield from self.freeze_color(self.indices[i], 'g')
            for _ in range(self.width):
                yield

    def animate(self, i):
        pass

    def get_animation(self):
        N = len(self.tab)
        ani = FuncAnimation(self.fig, self.animate, frames=self.tri,
                            save_count=N*(N-1)/2*self.width*5)
        close()
        return ani


# In[34]:


from numpy.random import permutation
TriBulles(permutation(10)).get_animation()


# In[35]:


def tri_bulles(tableau):
    for i in reversed(range(len(tableau))):
        for j in range(i):
            if tableau[j+1] < tableau[j]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]


# In[36]:


t = [4, 2, 5, 3, 8, 7, 6, 1]
tri_bulles(t)
t


# In[37]:


t = []
tri_bulles(t)
t


# In[38]:


t = [4]
tri_bulles(t)
t


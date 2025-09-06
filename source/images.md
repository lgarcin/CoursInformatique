---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Images

## Images en niveaux de gris

Une image _en niveaux de gris_ est représentée par un tableau à deux dimensions. Chaque case de ce tableau est appelée **pixel**. Dans une image en niveaux de gris, les valeurs des pixels varient généralement entre $0$ (noir) et $255$ (noir).

```{code-cell}
import imageio.v3 as io
import matplotlib.pyplot as plt
import numpy as np

img = np.array(io.imread('imageio:camera.png'))
plt.imshow(img, cmap='gray');
```

```{code-cell}
img.shape
```

```{warning}
Les lignes d'une image sont traditionellement numérotées du haut vers le bas.
```

```{code-cell}
img[100:200, 50:100] = 0
img[250:350, 300:400] = 255
plt.imshow(img, cmap='gray');
```

## Image en couleurs

Une image _en couleurs_ est représentée par trois tableaux à deux dimensions de même taille : un pour le canal rouge, un pour le canal vert et un pour le canal bleu.

```{code-cell}
img = np.array(io.imread('imageio:coffee.png'))
plt.imshow(img)
plt.axis('off');
```

```{code-cell}
img.shape
```

```{code-cell}
rouge = img.copy()
rouge[:,:,1] = rouge[:,:,2] = 0
plt.subplot(1, 3, 1)
plt.gca().set_title('Canal rouge')
plt.imshow(rouge)
plt.axis('off');

vert = img.copy()
vert[:,:,0] = vert[:,:,2] = 0
plt.subplot(1, 3, 2)
plt.gca().set_title('Canal vert')
plt.imshow(vert)
plt.axis('off');

bleu = img.copy()
bleu[:,:,0] = bleu[:,:,1] = 0
plt.subplot(1, 3, 3)
plt.gca().set_title('Canal bleu')
plt.imshow(bleu)
plt.axis('off');
```

On peut vérifier que la somme des trois canaux redonne bien l'image initiale.

```{code-cell}
plt.imshow(rouge+vert+bleu)
plt.axis('off');
```

## Redimensionnement d'une image

```{code-cell}
:tags: ["remove-stdout", "remove-input"]
from bokeh.plotting import output_notebook
output_notebook()
```

```{code-cell}
:tags: ["remove-input"]
:load: ../_scripts/interpolation_bilineaire.py
```

<!-- TODO A terminer -->

## Convolution

Si l'on dispose d'une image $A$ et d'un noyau de convolution $M=(M_{p,q})_{-d\leq p,q\leq d}$, les coefficients de la convolée $B=A\star M$ de la matrice $A$ par le noyau $M$ sont donnés par la formule :

$$
B_{i,j}=\sum_{-d\leq p,q\leq d}A_{i+p,j+q}\,M_{p,q}
$$

<!-- TODO Parler des bords, taille impaire -->

On utilisera la fonction `convolve2d` de la bibliothèque `scipy.signal`.

```{code-cell}
from scipy.signal import convolve2d
```

### Floutage

La convolution permet de remplacer la valeur de chaque pixel d'une image par la moyenne (éventuellement pondérée) des valeurs des pixels voisins.

```{code-cell}
img = np.array(io.imread('imageio:camera.png'))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.axis('off');

taille = 5
noyau = np.array([[1]*taille]*taille)/taille**2
conv = convolve2d(img, noyau)
plt.subplot(1, 3, 2)
plt.imshow(conv, cmap='gray')
plt.axis('off');

taille = 9
noyau = np.array([[1]*taille]*taille)/taille**2
conv = convolve2d(img, noyau)
plt.subplot(1, 3, 3)
plt.imshow(conv, cmap='gray')
plt.axis('off');
```

<!-- TODO Noyau gaussien -->

### Détection de contour

Si on se donne une image $I$ sous la forme d'un tableau à deux dimensions, on peut calculer sont gradient horizontal $G_x$ et son gradient vertical $G_y$ de la manière suivante :

$$
\begin{align*}
G_x(x,y)&=I(x+1,y)-I(x-1,y)\\
G_y(x,y)&=I(x,y+1)-I(x,y-1)
\end{align*}
$$

Le gradient horizontal/vertical en un pixel est plus élevé en valeur absolue en présence d'un contour horizontal/vertical.

On peut calculer le gradient horizontal/vertical grâce à un noyau de convolution.

```{code-cell}
noyau_x = np.array([[-1, 0, 1]])
noyau_y = noyau_x.T
noyau_x, noyau_y
```

```{code-cell}
img = np.array(io.imread('imageio:checkerboard.png'))
grad_x = convolve2d(img, noyau_x)
grad_y = convolve2d(img, noyau_y)
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.axis('off');
plt.subplot(1, 3, 2)
plt.gca().set_title('Gradient horizontal')
plt.imshow(grad_x, cmap='gray')
plt.axis('off');
plt.subplot(1, 3, 3)
plt.gca().set_title('Gradient vertical')
plt.imshow(grad_y, cmap='gray')
plt.axis('off');
```

On peut prendre en compte plus de pixels voisins pour le calcul du gradient.

```{code-cell}
noyau_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
noyau_y = noyau_x.T
noyau_x, noyau_y
```

```{code-cell}
img = np.array(io.imread('imageio:camera.png'))
grad_x = convolve2d(img, noyau_x)
grad_y = convolve2d(img, noyau_y)
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.axis('off');
plt.subplot(1, 3, 2)
plt.gca().set_title('Gradient horizontal')
plt.imshow(grad_x, cmap='gray')
plt.axis('off');
plt.subplot(1, 3, 3)
plt.gca().set_title('Gradient vertical')
plt.imshow(grad_y, cmap='gray')
plt.axis('off');
```

On peut alors calculer la norme du gradient.

```{code-cell}
grad=np.sqrt(grad_x**2+grad_y**2)
plt.imshow(grad, cmap='gray')
plt.axis('off');
```

On peut enfin fixer un seuil sur la norme du gradient pour décider des pixels faisant partie d'un contour.

```{code-cell}
def seuillage(image, seuil):
  image[image<seuil]=0
  image[image>=seuil]=255
```

```{code-cell}
seuillage(grad, np.max(grad)/4)
plt.imshow(grad, cmap='gray')
plt.axis('off');
```

<!-- TODO Peut-être avec laplacien (mais pas génial) -->
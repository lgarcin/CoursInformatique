from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy.random import permutation, choice
import numpy as np

rc('animation', html='jshtml')


class TriRapide:
    def __init__(self, tab):
        self.tab = tab
        self.width = 10
        self.fig = plt.figure(figsize=(len(tab), 3))
        plt.axis('off')
        plt.axis('equal')
        plt.axis([0, len(tab) * self.width, 0, self.width])

        self.rectangles = [plt.gca().add_patch(plt.Rectangle(np.array([i*self.width, 0]), self.width-1, self.width-1, fc='b'))
                           for i in range(N)]
        self.annotations = [plt.gca().annotate(tab[i], np.array([i*self.width, 0])+np.array([(self.width-1)*.5, (self.width-1)*.5]), color='w',
                                               weight='bold', fontsize=20,
                                               ha='center',
                                               va='center') for i in range(N)]

    def change_colors(self, left, mid, right):
        for r in [self.rectangles[i] for i in left]:
            r.set_color('g')
        for r in [self.rectangles[i] for i in right]:
            r.set_color('r')
        for r in [self.rectangles[i] for i in mid]:
            r.set_color('y')
        yield

    def unchange_colors(self, left, mid, right):
        for r in [self.rectangles[i] for i in left]:
            r.set_color('b')
        for r in [self.rectangles[i] for i in right]:
            r.set_color('b')
        for r in [self.rectangles[i] for i in mid]:
            r.set_color('brown')
        yield

    def move_vertical(self, left, right):
        for _ in range(self.width):
            for r in [self.rectangles[i] for i in left]:
                r.set_xy(np.array(r.get_xy())+np.array([0, 1]))
            for r in [self.rectangles[i] for i in right]:
                r.set_xy(np.array(r.get_xy())-np.array([0, 1]))
            for a in [self.annotations[i] for i in left]:
                a.set_position(np.array(a.get_position())+np.array([0, 1]))
            for a in [self.annotations[i] for i in right]:
                a.set_position(np.array(a.get_position())-np.array([0, 1]))
            yield

    def move_horizontal(self, move_list):
        for _ in range(10):
            for (i, move) in move_list:
                self.rectangles[i].set_xy(
                    np.array(self.rectangles[i].get_xy())+np.array([move*self.width/10, 0]))
                self.annotations[i].set_position(
                    np.array(self.annotations[i].get_position())+np.array([move*self.width/10, 0]))
            yield

    def tri(self, indices):
        yield
        if len(indices) > 0:
            piv = choice(indices)
            left = [i for i in indices if tab[i] < tab[piv]]
            mid = [i for i in indices if tab[i] == tab[piv]]
            right = [i for i in indices if tab[i] > tab[piv]]
            yield from self.change_colors(left, mid, right)
            if len(left) > 0 or len(right) > 0:
                yield from self.move_vertical(left, right)
                yield from self.move_horizontal([(i, (left+mid+right).index(i)-indices.index(i)) for i in indices])
                yield from self.move_vertical(right, left)
            yield from self.unchange_colors(left, mid, right)
            yield from self.tri(left)
            yield from self.tri(right)

    def gen(self):
        yield from self.tri([n for n in range(N)])

    def animate(self, i):
        pass

    def get_animation(self):
        ani = FuncAnimation(self.fig, self.animate,
                            frames=self.gen, save_count=1000)
        plt.close()
        return ani

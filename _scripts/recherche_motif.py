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

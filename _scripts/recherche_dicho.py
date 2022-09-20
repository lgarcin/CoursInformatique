import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc

rc('animation', html='jshtml')


class RechercheDicho:

    def __init__(self, elt, tab):
        self.elt = elt
        self.tab = tab
        self.width = 10

        self.fig = plt.figure(figsize=(len(tab), 3))
        plt.axis('off')
        plt.axis('equal')
        plt.axis([0, len(tab) * self.width, 0, 1.5*self.width])
        plt.title('Recherche de '+str(elt)+' dans '+str(tab), fontsize=20)

        self.rectangles = [plt.gca().add_patch(plt.Rectangle(
            [i * self.width, 0], 9, 9, color='b')) for i in range(len(tab))]
        self.annotations = [
            plt.gca().annotate(str(tab[i]), np.array([i * self.width, 0]) + np.array([(self.width - 1) * .5, (self.width - 1) * .5]), color='w',
                               weight='bold', fontsize=20,
                               ha='center',
                               va='center') for i in
            range(len(tab))]
        self.up = [False]*len(tab)

    def step(self, g, d, m):
        for i in range(len(self.tab)):
            rect = self.rectangles[i]
            annotation = self.annotations[i]
            if g <= i <= d and i != m:
                rect.set_color('cyan')
            elif i == m:
                rect.set_color('darkcyan')
            else:
                if not self.up[i]:
                    self.up[i] = True
                    rect.set_xy(np.array(rect.get_xy()) +
                                np.array([0, self.width]))
                    annotation.set_position(
                        np.array(annotation.get_position()) + np.array([0, self.width]))
                rect.set_color('blue')
        yield

    def win(self, m):
        for (i, rect) in enumerate(self.rectangles):
            if i == m:
                rect.set_color('green')
            else:
                rect.set_color('blue')
        yield

    def lose(self):
        for rect in self.rectangles:
            rect.set_color('red')
        yield

    def recherche_elt(self):
        yield
        g = 0
        d = len(self.tab) - 1
        while g <= d:
            m = (g + d) // 2
            yield from self.step(g, d, m)
            if self.tab[m] == self.elt:
                yield from self.win(m)
                return
            if self.elt < self.tab[m]:
                d = m - 1
            else:
                g = m + 1
        yield from self.lose()

    def animate(self, i):
        pass

    def get_animation(self):
        ani = FuncAnimation(
            self.fig, self.animate, frames=self.recherche_elt, save_count=500, interval=1000)
        plt.close()
        return ani

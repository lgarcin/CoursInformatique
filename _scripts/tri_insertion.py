from matplotlib import rc
from matplotlib.pyplot import gca, figure, axis, close, Rectangle
from matplotlib.animation import FuncAnimation
from numpy.random import permutation
from numpy import array

rc('animation', html='jshtml')


class TriInsertion:
    def __init__(self, tab):
        self.tab = tab.copy()
        self.width = 10
        self.fig = figure(figsize=(len(tab), 3))
        axis('off')
        axis('equal')
        axis([0, len(tab) * self.width, 0, self.width])

        self.rectangles = [gca().add_patch(Rectangle(array([i*self.width, 0]), self.width-1, self.width-1, fc='b'))
                           for i in range(N)]
        self.annotations = [gca().annotate(tab[i], array([i*self.width, 0])+array([(self.width-1)*.5, (self.width-1)*.5]), color='w',
                                           weight='bold', fontsize=20,
                                           ha='center',
                                           va='center') for i in range(N)]
        self.indices = [n for n in range(N)]

    def move_up(self, i):
        for _ in range(self.width):
            self.rectangles[i].set_xy(
                array(self.rectangles[i].get_xy())+array([0, 1]))
            self.annotations[i].set_position(
                array(self.annotations[i].get_position())+array([0, 1]))
            yield

    def move_down(self, i):
        for _ in range(self.width):
            self.rectangles[i].set_xy(
                array(self.rectangles[i].get_xy())-array([0, 1]))
            self.annotations[i].set_position(
                array(self.annotations[i].get_position())-array([0, 1]))
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

    def change_color(self, i):
        self.rectangles[i].set_color('r')
        yield

    def unchange_color(self, i):
        self.rectangles[i].set_color('b')
        yield

    def tri(self, n):
        yield
        if n > 1:
            yield from self.tri(n-1)
            yield from self.change_color(n-1)
            yield from self.move_up(n-1)
            val = self.tab[n-1]
            j = n-1
            while j > 0 and self.tab[self.indices[j-1]] > val:
                j -= 1
                yield from self.move_horizontal(self.indices[j], n-1)
                self.indices[j+1] = self.indices[j]
            yield from self.move_down(n-1)
            yield from self.unchange_color(n-1)
            self.indices[j] = n-1

    def gen(self):
        yield from self.tri(len(self.tab))

    def animate(self, i):
        pass

    def get_animation(self):
        N = len(self.tab)
        ani = FuncAnimation(self.fig, self.animate, frames=self.gen,
                            save_count=N*(N-1)//2*self.width*3)
        close()
        return ani

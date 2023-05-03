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
                            save_count=N*(N-1)//2*self.width*5)
        close()
        return ani

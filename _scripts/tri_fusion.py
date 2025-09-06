from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

rc("animation", html="jshtml")


class TriFusion:
    def __init__(self, tab):
        self.tab = tab
        self.width = 10
        N = len(tab)
        self.fig = plt.figure(figsize=(len(tab), 3))
        plt.axis("off")
        plt.axis("equal")
        plt.axis([0, len(tab) * self.width, 0, self.width])
        self.rectangles = [
            plt.gca().add_patch(
                plt.Rectangle(
                    np.array([i * self.width, 0]),
                    self.width - 1,
                    self.width - 1,
                    fc="b",
                )
            )
            for i in range(N)
        ]
        self.annotations = [
            plt.gca().annotate(
                tab[i],
                np.array([i * self.width, 0])
                + np.array([(self.width - 1) * 0.5, (self.width - 1) * 0.5]),
                color="w",
                weight="bold",
                fontsize=20,
                ha="center",
                va="center",
            )
            for i in range(N)
        ]
        self.indices = [n for n in range(N)]

    def move_vertical(self, left, right):
        for _ in range(self.width):
            for r in [self.rectangles[i] for i in left]:
                r.set_xy(np.array(r.get_xy()) + np.array([0, 1]))
            for a in [self.annotations[i] for i in left]:
                a.set_position(np.array(a.get_position()) + np.array([0, 1]))
            for r in [self.rectangles[i] for i in right]:
                r.set_xy(np.array(r.get_xy()) - np.array([0, 1]))
            for a in [self.annotations[i] for i in right]:
                a.set_position(np.array(a.get_position()) - np.array([0, 1]))
            yield

    def change(self, ind):
        for r in [self.rectangles[i] for i in ind[: len(ind) // 2]]:
            r.set_color("r")
        for r in [self.rectangles[i] for i in ind[len(ind) // 2 :]]:
            r.set_color("g")
        yield

    def unchange(self, ind):
        for r in [self.rectangles[i] for i in ind]:
            r.set_color("b")
        yield

    def move_horizontal(self, move_list):
        for _ in range(10):
            for i, move in move_list:
                self.rectangles[i].set_xy(
                    np.array(self.rectangles[i].get_xy())
                    + np.array([move * self.width / 10, 0])
                )
                self.annotations[i].set_position(
                    np.array(self.annotations[i].get_position())
                    + np.array([move * self.width / 10, 0])
                )
            yield

    def tri(self, a, b):
        if b - a > 1:
            yield
            yield from self.tri(a, (a + b) // 2)
            yield from self.tri((a + b) // 2, b)
            local_indices = self.indices[a:b]
            yield from self.change(local_indices, 0.5)
            yield from self.move_vertical(
                local_indices[: len(local_indices) // 2],
                local_indices[len(local_indices) // 2 :],
            )
            sorted_local_indices = sorted(local_indices, key=lambda i: self.tab[i])
            self.indices[a:b] = sorted_local_indices
            moves = [
                (i, sorted_local_indices.index(i) - local_indices.index(i))
                for i in local_indices
            ]
            yield from self.move_horizontal(moves)
            yield from self.move_vertical(
                local_indices[len(local_indices) // 2 :],
                local_indices[: len(local_indices) // 2],
            )
            yield from self.unchange(local_indices, None)

    def gen(self):
        yield from self.tri(0, len(self.tab))

    def animate(self, i):
        pass

    def get_animation(self):
        ani = FuncAnimation(self.fig, self.animate, frames=self.gen, save_count=1000)
        plt.close()
        return ani

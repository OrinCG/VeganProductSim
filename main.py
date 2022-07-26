import pymoo
import tkinter as tk
import matplotlib
import matplotlib.animation as animation
import time

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from tkinter import ttk


class AnimalGameGui:
    def __init__(self, no_agents):
        self.no_agents = no_agents
        self.product1_sold = 200
        self.product2_sold = 39
        self.product3_sold = 199

        self.window = tk.Tk()
        # self.middle = tk.Frame(self.window)
        # self.bottom = tk.Frame(self.window)
        # self.middle.pack()
        # self.bottom.pack()
        self.graph = None
        self.show_bar()

    def start_sim(self):
        self.window.mainloop()

    def show_bar(self):
        data = {
            'P1': self.product1_sold,
            'P2': self.product2_sold,
            'P3': self.product3_sold
        }

        figure = Figure(figsize=(6, 4), dpi=100)
        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self.window)
        # create axes
        axes = figure.add_subplot()
        # create the barchart
        rects = axes.bar(data.keys(), data.values())
        axes.set_title('Products')
        axes.set_ylabel('Num Sold')

        #   self.window.__setitem__()
        self.graph = figure_canvas.get_tk_widget()
        self.graph.pack()

        # Update the graph as the values change
        def graph_ani(frame):
            # rects[1].set_height(rects[1].get_height() + 30)
            # print(rects[1].get_height())
            # figure_canvas.draw()
            new_vals = map(lambda x: x + 10, data.values())
            rects = axes.bar(data.keys, new_vals)

        update_graph = animation.FuncAnimation(figure, graph_ani, 500)

        test_button = tk.Button(self.window, text="Increase bar 1",
                                command=lambda: increaseHeight()
                                )
        test_button.grid_anchor("s")
        test_button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui = AnimalGameGui(10)
    #  print("hi")
    gui.start_sim()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

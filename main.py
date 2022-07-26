import pymoo
import tkinter as tk
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as pyplt
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

        self._data = {
            'P1': self.get_product1_sold,
            'P2': self.get_product2_sold,
            'P3': self.get_product3_sold
        }

        self.window = tk.Tk()
        # self.middle = tk.Frame(self.window)
        # self.bottom = tk.Frame(self.window)
        # self.middle.pack()
        # self.bottom.pack()
        self.graph = None
        self.update_graph = None
        self.show_bar()

    @property
    def data(self):
        return dict(zip(self._data.keys(),list(map(lambda val: val(), self._data.values()))))

    def get_product1_sold(self):
        return self.product1_sold

    def get_product2_sold(self):
        return self.product2_sold

    def get_product3_sold(self):
        return self.product3_sold

    def start_sim(self):
        self.window.mainloop()

    def show_bar(self):
# I'm sorry

        figure = Figure(figsize=(6, 4), dpi=100)
        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self.window)
        # create axes
        axes = figure.add_subplot()
        # create the barchart
        rects = axes.bar(self.data.keys(), self.data.values())
        axes.set_title('Products')
        axes.set_ylabel('Num Sold')

        #   self.window.__setitem__()
        self.graph = figure_canvas.get_tk_widget()
        self.graph.pack()

        # Update the graph as the values change
        def graph_ani(frame):
            bar_labels = list(map(lambda x: x.get_text(),axes.get_xticklabels()))
            print(bar_labels)
            self.product1_sold += 50
            for i in range(0,len(bar_labels)):
                print(bar_labels[i] + " value" + str(self.data.get(bar_labels[i])))
                rects[i].set_height(self.data.get(bar_labels[i]))
            axes.set(ylim=(0,max(list(map(lambda x: x.get_height() + 10,rects)))))
        self.update_graph = animation.FuncAnimation(figure, graph_ani, 100)

        test_button = tk.Button(self.window, text="Increase bar 1",
                                command=lambda: graph_ani()
                                )
        test_button.grid_anchor("s")
        test_button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    # def get_P1(self):
    #     return self.product1_sold
    # def get_P1(self):
    #     return self.product1_sold
    # def get_P1(self):
    #     return self.product1_sold

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui = AnimalGameGui(10)
    #  print("hi")
    gui.start_sim()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Press the green button in the gutter to run the script.
from model import Model
from genetic import Genetic
from view import ProductSimView
import threading

if __name__ == '__main__':
    gen = Genetic(Model,8,0.1)
    gen.start_algorithm(8)

    gui = ProductSimView(10, gen.results)
    gui.start_sim()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Press the green button in the gutter to run the script.
from model import Model
from genetic import Genetic
from view import ProductSimView
import threading

if __name__ == '__main__':
    # model = Model(8, 0.1)
    # model.run()
    # gui = ProductSimView(10,model.results)
    #
    #
    # gui.start_sim()

    gen = Genetic(Model,8,0.1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

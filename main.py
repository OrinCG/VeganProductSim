# Press the green button in the gutter to run the script.
from model import Model
from view import ProductSimView
import threading

if __name__ == '__main__':
    model = Model(8, 0.1)
    gui = ProductSimView(10,model.results)
    model.initialize_data_collector(model_reporters={"Products": lambda m: m.products})
    model.run()

    gui.start_sim()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

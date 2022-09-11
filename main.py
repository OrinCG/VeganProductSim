

# Press the green button in the gutter to run the script.
from model import Model
from view import ProductSimView

if __name__ == '__main__':
    gui = ProductSimView(10)
    model = Model(8,0.1,gui)

    # print("hi")
    gui.start_sim()

    model.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

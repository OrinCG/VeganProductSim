import pymoo
import random

class Model:

    def __init__(self,no_agents):
        self.no_agents = no_agents
        self.product1_sold = 200
        self.product2_sold = 39
        self.product3_sold = 199


class Agent:

    def __init__(self):
        self.envScore = random.random()
        self.costScore = 1 - self.envScore
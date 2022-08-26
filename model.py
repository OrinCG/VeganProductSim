import pymoo
import numpy as np
import random
from mesa import Model as mesModel
from mesa import Agent as mesAgent
from mesa import time as mesTime

import pymoo.core.problem as pyProb


def normalise(products):
    avg_cost = 0
    avg_cost = sum(list(map(lambda p: getattr(p,"cost"), products)))/len(products)
    new_products = []
    for product in products:
        product.cost = product.cost / avg_cost

class Model(mesModel):

    def __init__(self, no_agents):
        self.no_agents = no_agents
        self.schedule = mesTime.RandomActivation(self)
        for i in range(self.no_agents):
            agent = Agent(i, self)
            self.schedule.add(agent)

        #Asign each agent friends who influence them
        for a in self.schedule.agents:
            i = random.randint(0, self.no_agents - 1)
            i2 = random.randint(0, self.no_agents - 1)
            a.__getattribute__("friends").extend([i, i2])
            print(a.__getattribute__("friends"))

        self.product1_sold = 0
        self.product2_sold = 0
        self.product3_sold = 0
        self.products = [Product("Organic Pea Meat",10.60,20), Product("Fake chicken",7,50), Product("Soy meat",2.50,80)]
        normalise(self.products)
        print(self.products)


    def step(self):
        self.schedule.step()


class Agent(mesAgent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.envScore = random.random()
        self.friends = []
        self.costScore = 1 - self.envScore

class Product:

    def __init__(self,name,cost,env_impact):
        self.name = name
        self.cost = cost
        self.env_impact = env_impact


    def __str__(self):
        return "Product: " + self.name + " " + str(self.cost) + " " + str(self.env_impact)

    def __unicode__(self):
        return u"Product: " + self.name + " " + str(self.cost) + " " + str(self.env_impact)

    def __repr__(self):
        return "Product: " + self.name + " " + str(self.cost) + " " + str(self.env_impact)

# def step(self):


class MyProblem(pyProb.ElementwiseProblem):

    def __init__(self):
        super().__init__(n_var=2,
                         n_obj=2,
                         n_constr=2,
                         xl=np.array([-2, -2]),
                         xu=np.array([2, 2]))

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = 100 * (x[0] ** 2 + x[1] ** 2)
        f2 = (x[0] - 1) ** 2 + x[1] ** 2

        g1 = 2 * (x[0] - 0.1) * (x[0] - 0.9) / 0.18
        g2 = - 20 * (x[0] - 0.4) * (x[0] - 0.6) / 4.8

        out["F"] = [f1, f2]
        out["G"] = [g1, g2]

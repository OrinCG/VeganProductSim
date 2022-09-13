import time

import pymoo
import numpy as np
import random
import mesa

import pymoo.core.problem as pyProb


def get_avg(item_list, attribute):
    return sum(list(map(lambda p: getattr(p, attribute), item_list))) / len(item_list)


def normalise(products):
    avg_cost = get_avg(products, "cost")
    for product in products:
        product.cost = product.cost / avg_cost


class Model(mesa.Model):

    def __init__(self, no_agents, opinion_change_rate, delay_agent_creation=False):
        self.no_agents = no_agents
        self.opinion_change_rate = opinion_change_rate
        self.results = []
        self.schedule = mesa.time.RandomActivation(self)
        if delay_agent_creation is False:
            agents = [Agent(i, self) for i in range(self.no_agents)]
            self.add_agents(agents)

        self.products = [Product("Organic Pea Meat", 7, 35), Product("Fake chicken", 2.3, 75),
                         Product("Soy meat", 2.50, 80)]
        normalise(self.products)
        #print(self.products)

    def step(self):
        self.schedule.step()
        #print(list(map(lambda p: p.sold, self.products)))
        for agent in self.schedule.agents:
            #print(agent.__getattribute__("env_score"), agent.__getattribute__("cost_score"))
            pass

    def run(self):
        for i in range(10):
            self.step()
            p_values = list(map(lambda p: p.sold, self.products))
            self.results.append(p_values)
        # self.view.update_scores(list(map(lambda p: p.sold, self.products)))

    def add_agents(self, agents):
        for a in agents:
            self.schedule.add(a)
        # Asign each agent friends who influence them
        for a in self.schedule.agents:
            i = random.randint(0, self.no_agents - 1)
            i2 = random.randint(0, self.no_agents - 1)
            a.__getattribute__("friends").extend([self.schedule.agents[i], self.schedule.agents[i2]])
            #print(a.__getattribute__("friends"))


class Agent(mesa.Agent):

    def __init__(self, unique_id, model, env_score=None):
        super().__init__(unique_id, model)
        if env_score is None:
            self.env_score = random.random()
        else:
            self.env_score = env_score
        self.friends = []
        self.cost_score = 1 - self.env_score
        self.money_spent = 0
        self.total_env_imp = 0

    def step(self) -> None:
        self.exchange_opinions()
        products = self.model.__getattribute__("products")
        product_scores = list(map(self.calcScore(), products))
        #print(product_scores, "SCORES")
        chosen_product = products[product_scores.index(max(product_scores))]
        chosen_product.sold += 1
        self.money_spent += chosen_product.cost
        self.total_env_imp += chosen_product.env_impact

    # Alter this agents scores to be a little closer to a friends
    def exchange_opinions(self):
        exchange_f = self.friends[random.randint(0, len(self.friends) - 1)]
        ex_f_env = exchange_f.__getattribute__("env_score")
        ex_f_cost = exchange_f.__getattribute__("cost_score")
        op_change_rate = self.model.__getattribute__("opinion_change_rate")
        env_change = abs(ex_f_env - self.env_score) / op_change_rate
        cost_change = abs(ex_f_cost - self.cost_score) / op_change_rate
        if self.cost_score < ex_f_cost:
            self.cost_score += cost_change
        else:
            self.cost_score -= cost_change
        if self.env_score < ex_f_env:
            self.env_score += env_change
        else:
            self.env_score -= env_change

    def calcScore(self):
        return lambda prod: ((- prod.env_impact) * self.env_score) / 100 + (
                -prod.cost * self.cost_score)  # Max env impact is 100 , should change to not be hard coded


class Product:

    def __init__(self, name, cost, env_impact):
        self.name = name
        self.cost = cost
        self.env_impact = env_impact
        self.sold = 0

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

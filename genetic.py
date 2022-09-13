from model import Agent, Model
import random
class Genetic:

    def __init__(self, Model, *args):
        self.model = Model(*args)
        self.results = []

    def start_algorithm(self,no_runs):
        for run in range(no_runs):
            print ("new run -------------------------------------------------------------")
            self.model.run()
            self.results.append(self.model.results)
            agents = list(self.model.schedule.agents)
            agents.sort(key=self.choose_fit)
            fittest = agents[0:2]
            print("fittest",fittest)
            next_mod = self.make_next_model(fittest)
            self.model = next_mod

    def choose_fit(self,agent):
        return  agent.money_spent + agent.total_env_imp

    def cross_scores(self,parents):
        parent1_weight = random.random()
        return parents[0].cost_score * parent1_weight + parents[1].cost_score * (1-parent1_weight)

    def make_next_model(self,parents):
        new_model = Model(self.model.no_agents,self.model.opinion_change_rate, delay_agent_creation=True)
        agents = []
        for i in range(self.model.no_agents):
            agents.append(Agent(i,new_model, env_score=self.cross_scores(parents)))

        mutatee = agents[random.randint(0,self.model.no_agents-1)]
        mutatee_dif = 1 - mutatee.env_score
        mutatee.env_score = mutatee.env_score + random.uniform(-mutatee_dif,mutatee_dif) # Alter the value a little bit
        new_model.add_agents(agents)
        return new_model
        


from deap import creator, base, tools, gp
from operator import and_, or_, xor, neg
from operator import add, sub, mul
from operator import lt, gt, eq
from random import random

def safe_division(a, b):
    try: 
        return a / b
    except:
        return 1

class TI():
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def get_technical_indicator(i, x):
        return data[i-int(x)]

def eval_pattern(individual, times):
    matches = 0
    log_gain = 1
    for i in range(times):
        try:
            if individual(i):
                






class GP():
    def __init__(self, gen, pop, data):
        self.data = data
        self.gen = gen
        self.pop = pop

    
    def _creator(self):
        creator.create("FitnessMin", base.Fitness, weights=(1.0,))
        creator.create("Individual", gp.PrimitiveSetTyped, fitness=creator.FitnessMin)

        self.pset = gp.PrimitiveSetTyped("main", [int], bool)
        self.pset.addPrimitive(and_, [bool, bool], bool)
        self.pset.addPrimitive(or_, [bool, bool], bool)
        self.pset.addPrimitive(xor, [bool, bool], bool)
        self.pset.addPrimitive(neg, [bool], bool)

        self.pset.addPrimiti4ve(add, [float, float], float)
        self.pset.addPrimitive(sub, [float, float], float)
        self.pset.addPrimitive(mul, [float, float], float)
        self.pset.addPrimitive(safe_division [float, float], float)

        self.pset.addPrimitive(lt, [float, float], bool)
        self.pset.addPrimitive(gt, [float, float], bool)
        self.pset.addPrimitive(eq, [float, float], bool)

        self.pset.renameArguments(ARG0="i")

        tis = []

        for i, ti in enumerate(data.colums):
            tis.append(TI(ti, data[ti]))
            self.pset.addPrimitive(tis[i].get_technical_indicator, [int, float], float)
        
        self.pset.addEphemeralConstant("prev", lambda: random.randint(0, 15) * 1.0, float)
    
        toolbox = base.Toolbox()
        toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
        toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)
        toolbox.register("compile", gp.compile, pset=pset)



        

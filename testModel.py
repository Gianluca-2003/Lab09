from model.model import Model

model = Model()
model.buildGraph()
print("Num nodi:",model.getNumNodi,"Num archi:", model.getNumArchi)
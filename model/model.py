import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.connessioni = None#DAO.getConnessioni(950)
        self._grafo = nx.Graph()



    def getAllConnessioni(self,distanza):
        self.connessioni = DAO.getConnessioni(distanza)



    def buildGraph(self):
        for connessioni in self.connessioni:
            self._grafo.add_edge(connessioni[0], connessioni[1], weight=connessioni[2])


    @property
    def getNumNodi(self):
        return len(self._grafo.nodes)


    @property
    def getNumArchi(self):
        return self._grafo.number_of_edges()










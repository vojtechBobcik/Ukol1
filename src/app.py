from platform import node
import sys
import re
from tokenize import String
from typing import List

class Node:
    def __init__(self,name) -> None:
        self.nodeName = name
        self.inputEdges = []
        self.outputEdges = []
        self.nodeValue = None
    
    def assignInputEdgeToNode(self, edge):
        self.inputEdges.append(edge)

    def assignOutputEdgeToNode(self, edge):
        self.outputEdges.append(edge)


class Edge:
    edgeFrom=None
    edgeTo=None
    value=None

    def __init__(self, edgeFrom, edgeTo) -> None:
        self.edgeFrom = edgeFrom
        self.edgeTo =edgeTo

class Graph:
    def __init__(self) -> None:
        self.graphNodes = []
        self.graphEdges = []
    

    def zjistiPocetZnamychProVsechnyUzly(self):
        pocetNavazujicichUzlu={}
        max = 0
        for x in self.graphNodes:
            name=x.nodeName
            numberOfNeighbours = 0
            for y in self.graphEdges:
                #pri pruchodu mi na konci radku pridavalo \r
                if (y.edgeFrom == x.nodeName or y.edgeTo[:-1] == x.nodeName):
                    numberOfNeighbours= numberOfNeighbours +1
            
            pocetNavazujicichUzlu[name]=numberOfNeighbours
            if(numberOfNeighbours>max): max=numberOfNeighbours

        for i in pocetNavazujicichUzlu:
            if pocetNavazujicichUzlu[i]==max:
                print(i+"("+repr(pocetNavazujicichUzlu.get(i))+")")

g = Graph()
nodes = []

#precteni radku uzlu
gr = input()
groups = re.match(r"^Group:\s(.*)$", gr)
if groups:
    nodes = groups.group(1).split(", ")
    nodes[-1] = nodes[-1][:-1]


#pridani vsech uzlu ktere jsme nasli v cyklu do objektu graf. Pridavame vsechno najednou na konci cteni.
for x in nodes:

    g.graphNodes.append(Node(x))

# Cteni vstupniho seznamu hran
for line in sys.stdin:
    #precteni radku hrany
    edgeGroup = re.match(r"^(.*)\s\-\s(.*)", line)
    if edgeGroup:
        g.graphEdges.append(Edge(edgeGroup.group(1), edgeGroup.group(2)))


g.zjistiPocetZnamychProVsechnyUzly()





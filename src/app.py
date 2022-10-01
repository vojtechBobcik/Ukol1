from platform import node
import sys
import re
from tokenize import String
from typing import List


class Graph:
    graphNodes: List
    graphEdges: List

    def __init__(self) -> None:
        self.graphNodes = []
        self.graphEdges = []

    def zjistiPocetZnamychProVsechnyUzly(self):
        for x in self.graphNodes:
            self.zjistiPocetZnamychProUzelZeSeznamuHran(x.nodeName,self.graphEdges)

    def zjistiPocetZnamychProUzelZeSeznamuHran(self, name, edgeList):
        print("hledam pocet znamych")

        numberOfNeighbours = 0
        for y in edgeList:
            if (y.edgeFrom == name or y.edgeTo == name):
                print(y.edgeFrom+" - "+ y.edgeTo)
                numberOfNeighbours+=1
                print(numberOfNeighbours)
        print(x.nodeName+"("+repr(numberOfNeighbours)+")")



class Node:
    def __init__(self,name) -> None:
        self.nodeName = name
        self.inputEdges = []
        self.outputEdges = []
        self.nodeValue = None


class Edge:
    edgeFrom : str
    edgeTo: str
    value: int

    def __init__(self, edgeFrom, edgeTo) -> None:
        self.edgeFrom = edgeFrom
        self.edgeTo = edgeTo
  

g = Graph()
nodes = []

# Cteni vstupniho seznamu uzlu ukol 1
for line in sys.stdin:
    #precteni radku uzlu
    groups = re.match(r"^Group:\s(.*)$", line)
    if groups:
        nodes = groups.group(1).split(", ")
        
    #precteni radku hrany
    edgeGroup = re.match(r"^(.*)\s\-\s(.*)", line)
    if edgeGroup:
        g.graphEdges.append(Edge(edgeGroup.group(1), edgeGroup.group(2)))

#pridani vsech uzlu ktere jsme nasli v cyklu do objektu graf. Pridavame vsechno najednou na konci cteni.
for x in nodes:
    g.graphNodes.append(Node(x))


g.zjistiPocetZnamychProVsechnyUzly()





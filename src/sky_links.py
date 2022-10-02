from operator import index
from os import link
from platform import node
import sys
import re
from tokenize import String
from typing import List

class Graph:
    def __init__(self) -> None:
        self.graphNodes = []
        self.graphEdges = []
    
    def checkSameEdge(self, edge, listOfEdges):
        numberOfSameEdges = 0
        for x in listOfEdges:
            if x.edgeTo == edge.edgeTo and x.edgeFrom == edge.edgeFrom:
                numberOfSameEdges+=1
        return numberOfSameEdges

    def findRedundatEdges(self):
        redundantEdges = set()
        for x in self.graphEdges:
            if(self.checkSameEdge(x, self.graphEdges)>1):
                redundantEdges.add(x.edgeFrom + " -> " + x.edgeTo)
        for x in redundantEdges:
            print(x)
    

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

g = Graph()
nodes = []

#precteni radku uzlu
gr = input()
groups = re.match(r"^City:\s(.*)$", gr)
if groups:
    nodes = groups.group(1).split(", ")
    nodes[-1] = nodes[-1][:-1]

#pridani vsech uzlu ktere jsme nasli v cyklu do objektu graf. Pridavame vsechno najednou na konci cteni.
for x in nodes:
    g.graphNodes.append(Node(x))

seznamLinek=[]
# Cteni vstupniho seznamu hran
for line in sys.stdin:
    #precteni nazvu linky
    linka = re.match(r"^(.*)\:\s",line)
    pripravaHran = line.split(linka.group(1))
    #oseknutí mezery a dvojtečky zepředu a znaku konce radku zezadu
    pripravaHran = pripravaHran[1][2:-2]
    edgeParts = re.split(r"\s\-\>\s", pripravaHran)
    seznamLinek.append(edgeParts)

# naplneni struktury grafu hranama
for x in seznamLinek:
    for y in range(len(x)-1):
        g.graphEdges.append(Edge(x[y],x[y+1]))

g.findRedundatEdges()
        

    
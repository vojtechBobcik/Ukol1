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

    def addNodeToGraph(self, node):
        if not self.checkNodeInGraph(node):
            self.graphNodes.append(node)

    def checkNodeInGraph(self, node):
        for x in self.graphNodes:
            return x.nodeName == node

    def findEdgeToEdgeLoop(self, nodeSequence):
        for x in range(len(nodeSequence)-1):
            if nodeSequence[x] == nodeSequence[x+1]:
                duplicateNodes.append(nodeSequence[x])

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
duplicateNodes =[]

#precteni radku uzlu
gr = input()
groups = re.match(r"^Guideposts::\s(.*)$", gr)
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

for x in seznamLinek:
    g.findEdgeToEdgeLoop(x)

for x in duplicateNodes:
    print(x)
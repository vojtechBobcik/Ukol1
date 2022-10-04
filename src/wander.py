from operator import index
from os import link
from platform import node
import sys
import re

class Graph:
    def __init__(self):
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
    def __init__(self,name):
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

    def __init__(self, edgeFrom, edgeTo):
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

checkpointy=[]
# Cteni vstupniho seznamu uzlu
for line in sys.stdin:
    #precteni nazvu checkpointu
    checkpointy = re.match(r"^(.*)\:\s",line)
    pripravaCheckpointu = line.split(checkpointy.group(1))
    #oseknutí mezery a dvojtečky zepředu a znaku konce radku zezadu
    pripravaCheckpointu = pripravaCheckpointu[1][2:-2]
    edgeParts = re.split(r"\s\-\>\s", pripravaCheckpointu)
    checkpointy.append(edgeParts)

for x in checkpointy:
    g.findEdgeToEdgeLoop(x)

for x in duplicateNodes:
    print(x)
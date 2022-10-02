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

    def addNode(self, node):
        if self.checkNodeInGraph(node):
            self.graphNodes.append(node)

    def checkNodeInGraph(self, node):
        for x in self.graphNodes:
            # print(x.nodeName + " - " + node)
            if x.nodeName == node:
                return True
            else:
                return False

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
groups = re.match(r"^Places:\s(.*)$", gr)
if groups:
    nodes = groups.group(1).split(", ")
    nodes[-1] = nodes[-1][:-1]
rozdilSetu = set()
#pridani vsech uzlu ktere jsme nasli v cyklu do objektu graf. Pridavame vsechno najednou na konci cteni.
#update: pridani do setu
for x in nodes:
    #g.graphNodes.append(Node(x))
    rozdilSetu.add(x)

seznamNavstivenychDestinaci=set()
# Cteni vstupniho seznamu hran
for line in sys.stdin:
    #precteni nazvu linky
    rok = re.match(r"^(.*)\:\s",line)
    destinace = line.split(rok.group(1))
    #oseknutí mezery a dvojtečky zepředu a znaku konce radku zezadu
    destinace = destinace[1][2:-2]
    edgeParts = re.split(r"\s\-\>\s", destinace)
    for x in edgeParts:
        seznamNavstivenychDestinaci.add(x)

rozdil = rozdilSetu.difference(seznamNavstivenychDestinaci)
for x in rozdil:
    print(x)





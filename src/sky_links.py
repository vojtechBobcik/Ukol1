from operator import index
from os import link
from platform import node
import sys
import re


class Graph:
    def __init__(self):
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
i = True
#precteni radku uzlu
# gr = input()
# groups = re.match(r"^City:\s(.*)$", gr)
# if groups:
#     nodes = groups.group(1).split(", ")
#     nodes[-1] = nodes[-1][:-1]

# #pridani vsech uzlu ktere jsme nasli v cyklu do objektu graf. Pridavame vsechno najednou na konci cteni.
# for x in nodes:
#     g.graphNodes.append(Node(x))

seznamLinek=[]
# Cteni vstupniho seznamu hran
for line in sys.stdin:
    if i:
        groups = re.match(r"^City:\s(.*)$", line)
        if groups:
            nodes = groups.group(1).split(", ")
            #nodes[-1] = nodes[-1][:-1]

        #pridani vsech uzlu ktere jsme nasli v cyklu do objektu graf. Pridavame vsechno najednou na konci cteni.
        for x in nodes:
            g.graphNodes.append(Node(x))
        i=False
        continue
    #precteni nazvu linky
    linka = re.match(r"^(.*)\:\s",line)
    pripravaHran = line.split(linka.group(1))
    #oseknutí mezery a dvojtečky zepředu a znaku konce radku zezadu
    
    #print(pripravaHran[1])
    pripravaHran = pripravaHran[1]
    edgeParts = re.split(r"\s\-\>\s", pripravaHran)
    #print(edgeParts)
    edgePartsStriped=[]
    for x in edgeParts:
        #print(x)
        x = x.strip(": \r\n")
        edgePartsStriped.append(x)
        #print(x)
    edgeParts = edgePartsStriped
    #print(edgeParts)
    seznamLinek.append(edgeParts)


# naplneni struktury grafu hranama
#print("//////////////")
for x in seznamLinek:
    for y in range(len(x)-1):
        #print(x[y],x[y+1])
        g.graphEdges.append(Edge(x[y],x[y+1]))

g.findRedundatEdges()
        

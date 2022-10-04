from operator import index
from os import link
from platform import node
import sys
import re


class Graph:
    def __init__(self):
        self.graphNodes = []
        self.graphEdges = []
    
    def isNodeInList(self, node, list):
        return node.name in list
    def findNodeByName(self, name):
        for node in self.graphNodes:
            if node.name == name:
                return node
            else:
                pass

class Node:
    def __init__(self,name):
        self.name = name
        self.outputEdges = []
        self.inputEdges = []
    
    def assignInputEdgeToNode(self, edge):
        self.inputEdges.append(edge)

    def assignOutputEdgeToNode(self, edge):
        self.outputEdges.append(edge)

g = Graph()
nodes = []

#precteni radku uzlu
gr = input()
groups = re.match(r"^Store\:(.*)$", gr)
if groups:
    nodes = groups.group(1).split(", ")
    nodes[-1] = nodes[-1][:-1]

for x in nodes:
    stripedNodeName=x.strip()
    g.graphNodes.append(Node(stripedNodeName))

# Cteni vstupniho seznamu hran
for line in sys.stdin:
    #precteni nazvu linky
    nazevTrasy = re.match(r"^(.*)\:\s",line)
    distribuce = line.split(nazevTrasy.group(1))
    
    #oseknutí mezery a dvojtečky zepředu a znaku konce radku zezadu
    distribuce = distribuce[1][2:-2]
    edgeParts = re.split(r"\s\-\>\s", distribuce)
    g.findNodeByName(edgeParts[0]).assignOutputEdgeToNode(g.findNodeByName(edgeParts[1]))
    g.findNodeByName(edgeParts[1]).assignInputEdgeToNode(g.findNodeByName(edgeParts[0]))

maxImport = 0
maxExport = 0
for x in g.graphNodes:
    if len(x.outputEdges)>maxExport:
        maxExport=len(x.outputEdges)
    if len(x.inputEdges)>maxImport:
        maxImport=len(x.inputEdges)

for x in g.graphNodes:
    if len(x.outputEdges)==maxExport:
        print("Export: " + x.name + "(" + repr(len(x.outputEdges)) + ")")
    if len(x.inputEdges)==maxImport:
        print("Import: " + x.name + "(" + repr(len(x.inputEdges)) + ")")



    
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
    
    def isNodeInList(self, node, list):
        return node.name in list
    def findNodeByName(self, name):
        for node in self.graphNodes:
            if node.name == name:
                return node
            else:
                pass


class Node:
    def __init__(self,name) -> None:
        self.name = name
        self.outputEdges = []
    
    def assignInputEdgeToNode(self, edge):
        self.inputEdges.append(edge)

    def assignOutputEdgeToNode(self, edge):
        self.outputEdges.append(edge)

g = Graph()
nodes = []

#precteni radku uzlu
gr = input()
groups = re.match(r"^Employ\:(.*)$", gr)
if groups:
    nodes = groups.group(1).split(", ")
    nodes[-1] = nodes[-1][:-1]

for x in nodes:
    stripedNodeName=x.strip()
    g.graphNodes.append(Node(stripedNodeName))

# Cteni vstupniho seznamu hran
for line in sys.stdin:
    edgeParts = re.split(r"\s\-\>\s", line)
    secondEdgeStriped = edgeParts[1].strip()
    #g.graphEdges.append(Edge(edgeParts[0], secondEdgeStriped))
    g.findNodeByName(edgeParts[0]).assignOutputEdgeToNode(g.findNodeByName(secondEdgeStriped))
    

for actualNode in g.graphNodes:
    for pointNode in actualNode.outputEdges:
        if not actualNode in pointNode.outputEdges:
            print(pointNode.name + " -> " + actualNode.name)
    #print(x.nodeName + " - " + repr(x.outputEdges))
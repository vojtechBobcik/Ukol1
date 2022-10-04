import sys
import re

class Graph:
    def __init__(self):
        self.graphNodes = []
        self.graphEdges = []
    
    def isNodeInList(self, node, list):
        return node.name in list

    def isNodeWithNameInList(self, nodeName, list):
        for x in list:
            if x.name == nodeName:
                return True
    
    def isNodeWithNameInListToLower(self, nodeName, list):
        for x in list:
            if x.name.lower() == nodeName.lower():
                return True

    def findNodeByName(self, name):
        for node in self.graphNodes:
            if node.name == name:
                return node
            else:
                pass
    def findNodeByNameInLowerCase(self, name):
        for node in self.graphNodes:
            if node.name.lower() == name.lower():
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
h = Graph()
nodes = []

#precteni radku uzlu
velke = input()
nodes = velke.split(", ")
stripedVelke=[]
for node in nodes:
    node=node.strip()
    stripedVelke.append(node)

male = input()
nodes = male.split(", ")
stripedMale=[]
for node in nodes:
    node=node.strip()
    stripedMale.append(node)


for node in stripedVelke:
    g.graphNodes.append(Node(node))
for node in stripedMale:
    h.graphNodes.append(Node(node))

# # Cteni vstupniho seznamu hran
for line in sys.stdin:
    edgeParts = re.split(r"\s\-\>\s", line)
    stripedParts =[]
    for node in edgeParts: 
        stripedParts.append(node.strip())

    if stripedParts[0].isupper() and stripedParts[1].isupper():
        g.findNodeByNameInLowerCase(stripedParts[0]).assignOutputEdgeToNode(g.findNodeByNameInLowerCase(stripedParts[1]))
    else:
        h.findNodeByNameInLowerCase(stripedParts[0]).assignOutputEdgeToNode(h.findNodeByNameInLowerCase(stripedParts[1]))


    # g.graphEdges.append(Edge(stripedParts[0],stripedParts[1]))

for node in g.graphNodes:
    for edge in node.outputEdges:
        print(node.name + " -> " + edge.name)
for node in h.graphNodes:
    for edge in node.outputEdges:
        tmp = g.findNodeByNameInLowerCase(node.name)
        if tmp is not None :
            #print("taduy/"+ node.name + " -> " + edge.name)
            if h.isNodeWithNameInListToLower(edge.name,tmp.outputEdges):
                #print("SNOFNAIF")
                continue
        else:
            print(node.name + " -> " + edge.name)



from operator import index
from os import link
from platform import node
import sys
import re

class Graph:
    def __init__(self):
        self.graphNodes = []
        self.graphEdges = []
    
    def findNodeInList(self, node, list):
        return node.nodeName in list

    sadySpolupracovniku = []
    def kontrolaSpoluprace(self, projekty):
        
        for zkoumany in self.graphNodes:
            spolupracovali = set()
            #print("zkoumany: " + zkoumany.nodeName)
            for pracovniciProjektu in projekty:
                #print("pracovnici na projektu: " + repr(pracovniciProjektu))
                if self.findNodeInList(zkoumany,pracovniciProjektu):
                    for pracovnik in pracovniciProjektu:
                        spolupracovali.add(pracovnik)
            #print("pocet spolupracovniku: " + repr(len(spolupracovali)))
            if len(spolupracovali) != len(self.graphNodes):
                #print("False")
                return False
                       
        #print("True")
        return True

        

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

    def __init__(self, edgeFrom, edgeTo) -> None:
        self.edgeFrom = edgeFrom
        self.edgeTo =edgeTo

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
    

#pridani vsech uzlu ktere jsme nasli v cyklu do objektu graf. Pridavame vsechno najednou na konci cteni.
#update: pridani do setu


pracovniciNaProjektu = []
# Cteni vstupniho seznamu hran
for line in sys.stdin:
    #precteni nazvu linky
    projekt = re.match(r"^(.*)\:\s",line)
    pracovnikNaProjektu = line.split(projekt.group(1))
    #oseknutí mezery a dvojtečky zepředu a znaku konce radku zezadu
    pracovnikNaProjektu = pracovnikNaProjektu[1][2:-2]
    edgeParts = re.split(r"\,\s", pracovnikNaProjektu)
    pracovniciNaProjektu.append(edgeParts)

print(g.kontrolaSpoluprace(pracovniciNaProjektu))




    
    
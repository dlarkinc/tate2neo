'''
Import the top level in the subjects hierarchy. By default, this will be from the level0.json file.
'''
import json
import sys

from py2neo import Graph
from py2neo import Node

graph = Graph()

level0_f = sys.argv[1]  # accept subjects level 0 json file from cli

print level0_f

subjects = json.loads(open(level0_f).read())

for i in subjects.items():
    print "Node: " + i[0] + "--" + i[1]
    n = Node("Subject", id=i[0], name=i[1], level=0)
    graph.create(n)



import json
import os

from py2neo import Graph
graph = Graph()
from py2neo import Node
from py2neo import watch

watch("httpstream")

level0_f = "/home/larkin/Dropbox/DAH PhD/Neo4J/Metadata/tate/collection/processed/subjects/level0.json"

subjects = json.loads(open(level0_f).read())

for i in subjects.items():
	print "Node: " + i[0] + "--" + i[1]
	n = Node("Subject", id = i[0], name = i[1], level = 0)
	graph.create(n)



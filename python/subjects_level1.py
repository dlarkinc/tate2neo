import json
import os

from py2neo import Graph
graph = Graph()
from py2neo import Node, Relationship

#from py2neo import watch
#watch("httpstream")
	
level1_f = "/home/larkin/Dropbox/DAH PhD/Neo4J/Metadata/tate/collection/processed/subjects/level1list.json"

subjects = json.loads(open(level1_f).read())

for d in subjects:
	parent = graph.merge_one("Subject", "id", str(d["parent0"]))
	print str(d["id"]) + ":" +  d["name"] + "--" + parent["name"]
	n = Node("Subject", id = d["id"], name = d["name"], level = 1)
	r = Relationship(n, "TYPE_OF", parent)
	graph.create(r)



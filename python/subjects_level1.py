'''
Import the second level in the subjects hierarchy. By default, this will be from the level1list.json file.
'''
import json
import sys

from py2neo import Graph
graph = Graph()
from py2neo import Node, Relationship

level1_f = sys.argv[1]

subjects = json.loads(open(level1_f).read())

for d in subjects:
    parent = graph.merge_one("Subject", "id", str(d["parent0"]))
    print str(d["id"]) + ":" + d["name"] + "--" + parent["name"]
    n = Node("Subject", id=d["id"], name=d["name"], level=1)
    r = Relationship(n, "TYPE_OF", parent)
    graph.create(r)



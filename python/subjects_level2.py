'''
Import the third level in the subjects hierarchy. By default, this will be from the level2list.json file.

CLI parameters:
argv[1] - full path to json file, including filename
argv[2] - optional flag to print or not
'''
import json
import sys

from py2neo import Graph
graph = Graph()
from py2neo import Node, Relationship

level2_f = sys.argv[1]
verbose = sys.argv[2]

subjects = json.loads(open(level2_f).read())

for d in subjects:
    parent = graph.merge_one("Subject", "id", d["parent1"])
    if verbose:
        print str(d["id"]) + ":" + d["name"] + "--" + parent["name"]
    n = Node("Subject", id=d["id"], name=d["name"], level=2)
    r = Relationship(n, "TYPE_OF", parent)
    graph.create(r)
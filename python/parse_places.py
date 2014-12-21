import json
import os
import time
from py2neo import Graph
from py2neo import Node

start_time = time.time()
graph = Graph()

fileDir = "/home/larkin/Dropbox/DAH PhD/Neo4J/Metadata/tate/collection/artworks/"

mediums = []

for root, dirs, filenames in os.walk(fileDir):
	for f in filenames:
		artwork = json.loads(open(os.path.join(root, f)).read())
		
		try: 
			if artwork["medium"]:
				for m in artwork["medium"].split(","):
					for n in m.split(" and "):
						for o in n.split(" on "):
							s = ''.join([i for i in o if not i.isdigit()])
							if s.strip().lower() not in mediums:
								mediums.append(s.strip().lower())
		except AttributeError:
			print artwork["acno"]

print mediums
print len(mediums)

for m in mediums:
	n = Node("Medium", id=m, name=m)
	graph.create(n)

print("--- %s seconds ---" % (time.time() - start_time))


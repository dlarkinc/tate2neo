import json
import os
from py2neo import Graph
from py2neo import Node, Relationship

graph = Graph()

fileDir = "/home/larkin/Dropbox/DAH PhD/Neo4J/Metadata/tate/collection/artworks/"
total = 0

mediums = []
subjects = []

for root, dirs, filenames in os.walk(fileDir):
	for f in filenames:
		artwork = json.loads(open(os.path.join(root, f)).read())
		total = total + 1
		 
		#for c in artwork["contributors"]:
		#	print c["id"]

		if artwork["subjectCount"] > 0:
			if "children" in artwork["subjects"]:
				for sl1 in artwork["subjects"]["children"]:
					#print sl1["name"]
					if "children" in sl1:
						for sl2 in sl1["children"]:
							#print "-" + sl2["name"]
							if "children" in sl2:
								for sl3 in sl2["children"]:
									#print "--" + sl3["name"]
									subjects.append(sl3["id"])
		
		node = Node("Artwork", id=artwork["id"], title=artwork["title"], acno=artwork["acno"])		
		graph.create(node)

		for s in subjects:
			subject = graph.merge_one("Subject", "id", s)
			r = Relationship(node, "FEATURES", subject)
			graph.create(r)

		if artwork["medium"]:
			for m in artwork["medium"].split(","):
				for n in m.split(" and "):
					for o in n.split(" on "):
						s = ''.join([i for i in o if not i.isdigit()])
						if s.strip().lower() not in mediums:
							mediums.append(s.strip().lower())
		
		for m in mediums:
			medium = graph.merge_one("Medium", "id", m)
			r = Relationship(node, "MADE_OF", medium)
			graph.create(r)

import json
import os

fileDir = "/home/larkin/Dropbox/DAH PhD/Neo4J/Metadata/tate/collection/artists/"
total = 0

for root, dirs, filenames in os.walk(fileDir):
	for f in filenames:
		artist = json.loads(open(os.path.join(root, f)).read())

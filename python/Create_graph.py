'''
    Script to create some sample nodes and edges, purely for illustration purposes. Does not align with the
    nodes, edges and properties in other scripts.
'''

from py2neo import Graph
graph = Graph()
from py2neo import Node, Relationship
magdalena = Node("Artist", name="Abakanowicz, Magdalena", id=10093, gender="Female", birthYear=1930)
polska=Node("Place", name="Polska")
magdalena_born_in_polska = Relationship(magdalena, "BORN_IN", polska)
graph.create(magdalena_born_in_polska)
polska.properties["id"]="Polska"
polska.push()
magdalena_born_in_polska.properties["date"]=1930

magdalena_born_in_polska.push()
t12979 = Node("Artwork", title="Abakan Red", date=1969, acno="T12979", id=102938)
magdalena_contributed_to_t12979 = Relationship(magdalena, "CONTRIBUTED_TO", t12979)
graph.create(magdalena_contributed_to_t12979)
metal = Node("Medium", name="metal")
sisal = Node("Medium", name="sisal")
abakan_made_of_metal = Relationship(t12979, "MADE_OF", metal)
abakan_made_of_sisal = Relationship(t12979, "MADE_OF", sisal)
graph.create(abakan_made_of_metal, abakan_made_of_sisal)

cities = Node("Place Types", name="cities, towns, villages (non-UK)")
countries = Node("Place Types", name="countries and continents")
abakan = Node("Place", name="Abakan")
abakan = Node("Place", name="Russia, Khakassia")
abakan = Node("Place", name="Abakan")
russia = Node("Place", name="Russia, Khakassia")
abakan_in_russia = Relationship(abakan, "FEATURES", russia)
abakan_in_russia = Relationship(t12979, "FEATURES", abakan)
abakan_in_russia = Relationship(t12979, "FEATURES", russia)
abakan_in_abakan = Relationship(t12979, "FEATURES", abakan)
graph.create(abakan_in_russia, abakan_in_abakan)
a = Node("Year", id="1930", value="1930")
b = Node("Year", id="1969", value="1969")
t12979_1969 = Relationship(t12979, "CREATED_IN", b)
magdalena_1930 = Relationship(magdalena, "BORN_IN", a)
graph.create(t12979_1969, magdalena_1930)

classif = Node("Classification", name="installation")
t12979_class = Relationship(t12979, "CLASSED_AS", classif)
graph.create(t12979_class)

t12958 = Node("Artwork", id=102939, title="Embryology", acno="T12958", date="1978-1980")
magda_t12958 = Relationship(magdalena, "CONTRIBUTED_TO", t12958)

graph.create(magda_t12958)

t12958_class = Relationship(t12958, "CLASSED_AS", classif) 
graph.create(t12958_class)
sixties = Node("Decade", name="1960s")
b_sixties = Relationship(b, "IS_DURING", sixties)
thirties = Node("Decade", name="1930s")
a_thirties = Relationship(a, "IS_DURING", thirties)
graph.create(a_thirties, b_sixties)

burlap = Node("Medium", name="burlap")
cotton_gauze = Node("Medium", name="cotton gauze")
hemp_rope = Node("Medium", name="hemp rope")
nylon = Node("Medium", name="nylon")
t12958_burlap = Relationship(t12958, "MADE_OF", burlap)
t12958_nylon = Relationship(t12958, "MADE_OF", nylon)
t12958_hemp = Relationship(t12958, "MADE_OF", hemp_rope)
t12958_cotton = Relationship(t12958, "MADE_OF", cotton_gauze)
t12958_sisal = Relationship(t12958, "MADE_OF", sisal)
graph.create(t12958_burlap, t12958_cotton, t12958_sisal, t12958_hemp, t12958_nylon)


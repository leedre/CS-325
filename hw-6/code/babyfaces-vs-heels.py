'''
Jon-Eric Cook
CS-325
Homework #5
This program demonstrates a BFS algorithm being utilized to determine whether 
it is possible to designate some of the wrestlers as Babyfaces and the remainder 
as Heels such that each rivalry is between a Babyface and a Heel. It does this 
by processing an input file, creating a graph and then running the BFS algorithm 
on said graph. The results will be:
Yes, if possible followed by a list of the Babyface wrestlers and a list of the Heels.
No, if impossible.
'''

import sys

# vertex class that contains all the information about a vertex
# a vertex represents a wrestler
class Vertex:
    # initializes the variables of the vertex
    def __init__(self, n):
        # name of the wrestler
        self.name = n
        # will be either a babyface or heel
        self.type_of_wrestler = ''
        # creates a list of neighbors
        self.neighbors = list()
        # initializes to a large distance
        self.distance = 9999
        # the color black represents an unvisited vertex
        self.color = 'black'

    # adds a neighbor to the vertex
    def add_neighbor(self, v):
        # confirms the vertex is not already a neighbor
        if v not in self.neighbors:
            # adds the vertex
            self.neighbors.append(v)
            # sorts the list of neighbors
            self.neighbors.sort()

# graph class that contains all the information about a graph
class Graph:
    # dict that holds all the vertecies
    vertices = {}
    # bool variable that determines if the designation can be done
    can_designate = True
    # the starting vertex of the graph
    start_vertex = None
    # bool variable indicating if the starting vertex has been set
    set_start_vertex = False

    # addes a vertex to the graph
    def add_vertex(self, vertex):
        # confirms vertex is in fact a Vertex
        # confirms vertex is not already in the vertex dict
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            # adds the vertex
            self.vertices[vertex.name] = vertex
            # sets the starting vertex
            if not self.set_start_vertex:
                self.start_vertex = vertex
                self.set_start_vertex = True

    # adds an edge to a vertex
    def add_edge(self, u, v):
        # checks if the vertecies are in the vertecies dict 
        if u in self.vertices and v in self.vertices:
            # assigns each vertex to the other's neighbor list
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)

    # prints the list of wrestlers based on the input string
    def print_wrestlers(self,wrestler_type):
        results = wrestler_type + "s: "
        for v in self.vertices:
            if self.vertices[v].type_of_wrestler == wrestler_type:
                results = results + self.vertices[v].name + ' '
        print(results)

    # breadth first search function steps through the entire graph
    def bfs(self, vert):
        # creates the needed queue
        q = list()
        # sets the starting vertex to a babyface
        vert.type_of_wrestler = 'Babyface'
        # sets its distance to 0
        vert.distance = 0
        # marks it as visited
        vert.color = 'red'
        # steps through each neighbor of the starting vertex
        for v in vert.neighbors:
            # increments their distance
            self.vertices[v].distance = vert.distance + 1
            # sets them as heels
            self.vertices[v].type_of_wrestler = 'Heel'
            # appends them to the queue
            q.append(v)
        # gets each vertex in the queue while it still contains vertecies
        while len(q) > 0:
            # get the top vertex
            u = q.pop(0)
            # get is as an object
            node_u = self.vertices[u]
            # set it as visited
            node_u.color = 'red'
            # steps through each neighbor of the popped vertex
            for v in node_u.neighbors:
                # get it as an object
                node_v = self.vertices[v]
                # check if it has been visited
                if node_v.color == 'black':
                    # put it in the queue
                    q.append(v)
                    # check if its distane is greater than that of the previous vertex plus 1
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1
                    # assign the vertex to babyface if its distance is even or heel if not
                    if node_v.distance % 2 == 0:
                        node_v.type_of_wrestler = 'Babyface'
                    else:
                        node_v.type_of_wrestler = 'Heel'
                    # check if the child parent are of the same wrestling type
                    if node_v.type_of_wrestler == node_u.type_of_wrestler:
                        self.can_designate = False

    # confirm that the graph is connected and each vertex has been visited
    def is_graph_connected(self):
        for v in self.vertices:
            if self.vertices[v].color == 'black':
                self.bfs(self.vertices[v])

# open the input file for reading
input_file = open(sys.argv[1], 'r')
# get all the contents as an indexable lines array
input_data = input_file.read().splitlines()
# get the number of wrestlers
numb_wrestlers = int(input_data[0])
# create the graph
g = Graph()
# add the vertecies to the graph
for i in range(1, numb_wrestlers + 1):
    g.add_vertex(Vertex(input_data[i]))
# get the number of rivalries
numb_rivalries = int(input_data[numb_wrestlers+1])
# add the rivalries as neighbors
for j in range(numb_wrestlers + 2, numb_wrestlers+1+numb_rivalries+1):
    riv = input_data[j]
    riv_s = riv.split()
    g.add_edge(riv_s[0],riv_s[1])
# run the breadth first search on the graph
g.bfs(g.start_vertex)
# check if it is connected
g.is_graph_connected()
# print results
if g.can_designate:
    print("Yes")
    g.print_wrestlers("Babyface")
    g.print_wrestlers("Heel")
else:
    print("No\nCannot perform designation.")
# close the file
input_file.close()

'''
-RESOURCE-
The resources below assisted me in completing this assignment.
https://www.youtube.com/watch?v=-uR7BSfNJko
https://github.com/joeyajames/Python/blob/master/bfs.py
'''
"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
       

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)  # v1 is a key and a connecting node, the neighbor is v2

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]  # returning the neighbour values of the key with specific id

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # --setup phase-- 1)make a queue; 2)make a visited set;
        # Create an empty Quene and add starting vertex to it 
        # This will keep track of all next-to-visit-vertices
        # Queue is first in first out
        queue = []
        queue.append(starting_vertex)
        # Create an empty set to keep track of visited verticies (no need for key when using set)
        visited = set()
        # While the queue is not empty
        while len(queue) > 0:
            # dequeue a vertex off the queue 
            current_vertex = queue.pop(0) # pop from the front, the first item

            # if vertex not in visited verticies: 
            if current_vertex not in visited:
                  # -- "Do something step" -- always different, depents on a problem --
                # print it
                print(current_vertex)
              # -- check is seen place --            
                 
                  # -- get neighbours add them to queue --
                # add the vertex to our visited set 
                visited.add(current_vertex)
                # add all neighbours to queue 
                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)
   

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # use a stack, stack a neighbors
        # Create an empty Quene and add starting vertex to it 
        # This will keep track of all next-to-visit-vertices
        # Queue is first in first out
        stack = []
        stack.append(starting_vertex)
        # Create an empty set to keep track of visited verticies 
        visited = set()
        # While the queue is not empty
        while len(stack) > 0:
            # dequeue a vertex off the queue 
            current_vertex = stack.pop() # pop of the last item

            # if vertex not in visited verticies: 
            if current_vertex not in visited:
                # print it
                print(current_vertex)
                # add the vertex to our visited set 
                visited.add(current_vertex)
                # add all neighbours to queue 
                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)

        #Create empty stack
        #Add starting vert
        #Create set for visited
        #while stack is not empty
            #remove vert
            #if vert not visited
                #mark as visited
                #add all neighbors to stack
        
        # s = Stack()
        # # add starting vertex to the stack
        # s.push(starting_vertex)

        # visited = set()

        # while s.size():
        #     v = s.pop()

        #     # if this vertex is not in visited set
        #     if v not in visited:
        #         # add it to visited
        #         visited.add(v)
        #         print(v)

        #         # add the neighbors to the stack
        #         neighbors = self.get_neighbors(v)
        #         for neighbor in neighbors:
        #             s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # create visited set if instantiated at None
        if visited is None:
            visited = set()

        # check if starting index is in visited
        if starting_vertex not in visited:
            # add to visited
            visited.add(starting_vertex)
            print(starting_vertex)

            # call recursively for each neighbor of the starting index
            for vrtx in self.get_neighbors(starting_vertex):
                self.dft_recursive(vrtx, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #Create empty queue and enqueue A PATH To the starting vert id
        #Create a set for visited
        #while queue is not empty
            #dequeue the first PATH
            #grab the last vert from the PATh
            #if vert not visited
                #CHECK IF ITS THE TARGET
                    #if so return path
                #Mark it as visited
                #Add the path to its neighbors to the back of the queue
                    #copy the path
                    #APPEND THE NEIGHBOR TO THE BACK

        visited = set()
        q = Queue()
        # add starting vertex to the queue as a list
        q.enqueue([starting_vertex])

        while q.size():
            # dequeue the current path
            path = q.dequeue()
            # store the last vertex in the path
            node = path[-1]

            # check if it is in visited
            if node not in visited:
                # add to visited
                visited.add(node)
                # check for target, return path
                if node == destination_vertex:
                    return path
                else:
                    # enqueue the path to each neighbor
                    for neighbor in self.get_neighbors(node):
                        q.enqueue(path + [neighbor]) 
        return None      

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size():
            # store the next item in the stack
            path = s.pop()
            # store the last vertex in the path
            node = path[-1]

            if node not in visited:
                # add to visited
                visited.add(node)
                # if current node is our target, return the path
                if node == destination_vertex:
                    return path

                # loop over neighbors
                for neighbor in self.get_neighbors(node):
                    # add a path to each neighbor to the stack
                    s.push(path + [neighbor])

        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path == []:
            path = [starting_vertex]

        # base case, if we have visited all nodes we will not recurse
        if starting_vertex not in visited:
            visited.add(starting_vertex)

            if starting_vertex == destination_vertex:
                return path

            # loop over neighbors
            for neighbor in self.get_neighbors(starting_vertex):
                # store the depth first path of the starting vertex, recursively call passing in visited and the new path including the neighbor
                result = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path + [neighbor])
                # if our recursive call returns a path, it will be returned here
                if result:
                    return result

        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

import sys
class graph():
    def __init__(self,vertex,matrix):
        if len(matrix)==vertex and len(matrix[0])==vertex:
            self.vertex=vertex
            self.graph=matrix
        else:
            self.graph=None
            return False
    def printedges(self):
        print('The edges of Graph are:\n')
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]!=0:
                    print('{} -> {}  [Weight {}]'.format(i,j,self.graph[i][j]))
    def adjacent_vertices(self,u):
        lst=[]
        if u<self.vertex:
            for i in range(self.vertex):
                if self.graph[u][i]!=0:
                    lst.append(i)
            return lst
        else:
            return False
    def dijkstra(self,source):
        s=[False]*self.vertex
        Q=list(range(self.vertex))
        distance=[sys.maxsize]*self.vertex
        distance[source]=0
        parent=[None]*self.vertex
        while(len(Q)!=0):
            minval=sys.maxsize
            for vertex in Q:
                if minval>distance[vertex]:
                    minval=distance[vertex]
                    u=vertex
            Q.remove(u)
            s[u]=True
            for v in self.adjacent_vertices(u):
                if not s[v]:
                    if distance[v]>distance[u]+self.graph[u][v]:
                        distance[v]=distance[u]+self.graph[u][v]
                parent[v]=u

        for i in range(self.vertex):
            print('Min Distance to {} from source {}: {}'.format(i,source,distance[i]))
        print(parent)
            

matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

g = graph(9,matrix)
g.printedges()
print('\n\n')
g.dijkstra(0)

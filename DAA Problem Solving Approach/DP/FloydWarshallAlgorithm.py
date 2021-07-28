#The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. 
# The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph. 
#value of graph[i][j] is 0 if i is equal to j 
#And graph[i][j] is INF (infinite) if there is no edge from vertex i to j.
import sys
class graph():
    def __init__(self,vertex=None,matrix=None):
        if vertex==len(matrix):
            self.vertex=vertex
            self.graph=matrix
        else:
            self.vertex=0
            self.graph=[]
    def path(self,v1,v2):
        self.lst=[v1]
        n=self.vertex
        while(n):
            temp=[]
            for  items in self.lst:
                for i in range(self.vertex):
                    if self.graph[items][i]!=0 and self.graph[items][i]!=sys.maxsize:
                        if i==v2:
                            return True
                        temp.append(i)
            self.lst=temp
            n-=1
        return False
    def FWA(self):
        distance=self.graph
        for i in range(self.vertex):
                for j in range(self.vertex):
                    if distance[i][j]==0 and i!=j:
                        distance[i][j]=sys.maxsize
        for i in range(self.vertex):
            for j in range(self.vertex):
                for k in range(self.vertex):
                    if self.path(i,k) and self.path(k,j):
                        if distance[i][j]>distance[i][k]+distance[k][j]:
                            distance[i][j]=distance[i][k]+distance[k][j]
        for i in range(self.vertex):
            for j in range(self.vertex):
                if distance[i][j]>=sys.maxsize:
                    print('-',end=' ')
                else:
                    print(distance[i][j],end=' ')
            print('\n')
    

# matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#         [4, 0, 8, 0, 0, 0, 0, 11, 0],
#         [0, 8, 0, 7, 0, 4, 0, 0, 2],
#         [0, 0, 7, 0, 9, 14, 0, 0, 0],
#         [0, 0, 0, 9, 0, 10, 0, 0, 0],
#         [0, 0, 4, 14, 10, 0, 2, 0, 0],
#         [0, 0, 0, 0, 0, 2, 0, 1, 6],
#         [8, 11, 0, 0, 0, 0, 1, 0, 7],
#         [0, 0, 2, 0, 0, 0, 6, 7, 0]
#         ]

matrix = [[0, 5, 0, 10],
          [0, 0, 3, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 0]]

g = graph(4,matrix)
print('\n\n')
g.FWA()

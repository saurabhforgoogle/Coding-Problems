#A Graph consists of a finite set of vertices(or nodes) and set of Edges which connect a pair of nodes.
#Bset Using Adjancy MAtrix
class Graph():
    def __init__(self,matrix):
        self.graph=matrix
    def Adjacent_Matrix(self,vertex):
        print('Adjacent Vartex are:')
        for i in range(len(self.graph[vertex])):
            if self.graph[vertex][i]!=0:
                print(i)
    def pathfinder(self,v1,v2):
        self.lst=[v1]
        n=len(self.graph)
        while(n):
            temp=[]
            for  items in self.lst:
                
                for i in range(len(self.graph)):
                    if self.graph[items][i]!=0:
                        if i==v2:
                            return True
                        temp.append(i)
            self.lst=temp
            n-=1
        return False
        



matrix=[[0,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,0]]
g=Graph(matrix)
g.Adjacent_Matrix(1)
print(g.pathfinder(1,2))
            
#Weighted Matrix can be done by replacing one with Wi[i][j]

# a graph's diameter is the largest number of vertices which 
# must be traversed in order to travel from one indirected vertex to another
#  when paths which backtrack, detour, or loop are excluded from 
#  consideration.

class graph():
    def __init__(self):
        self.vertices=[]
        self.graph=dict()
        self.TotalVertices=0
    def addedge(self,u,v):
        if u not in self.graph.keys():
            self.graph[u]={v}
        else:
            self.graph[u].add(v)
        if v not in self.graph.keys():
            self.graph[v]={u}
        else:
            self.graph[v].add(u)
        if u not in self.vertices:
            self.vertices.append(u)
            self.TotalVertices+=1
        if u not in self.vertices:
            self.vertices.append(u)
            self.TotalVertices+=1
               
    def farthestNode(self,source):
        currentNode=[[source,0]]
        self.visited=[False]*(max(self.graph.keys())+1)
        self.visited[source]=True 
        maxdistance=0
        maxdistancenode=source
        while(len(currentNode)!=0):
            UsedNode=currentNode.pop(0)
            if maxdistance<UsedNode[1]:
                maxdistance=UsedNode[1]
                maxdistancenode=UsedNode[0]
            for adjvert in self.graph[UsedNode[0]]:
                if not self.visited[adjvert]:
                    currentNode.append([adjvert,UsedNode[1]+1])
                    self.visited[adjvert]=True 
        return maxdistancenode,maxdistance

    def graphdiameter(self):
        tempnode=self.vertices[0]
        Node1,diameter=self.farthestNode(tempnode)
        Node2,diameter=self.farthestNode(Node1)
        return (Node1,Node2,diameter)

g = graph()
g.addedge(1,2)
g.addedge(2,4)
g.addedge(4,5)
g.addedge(4,6)
g.addedge(6,10)
g.addedge(1,3)
g.addedge(3,7)
g.addedge(7,9)
g.addedge(7,8)
Node1,Node2,Diameter=g.graphdiameter()
print('From {} to {}, Diameter={}'.format(Node1,Node2,Diameter))

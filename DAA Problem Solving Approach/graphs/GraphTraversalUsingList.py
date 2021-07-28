class Graph():
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=dict()
        #self.visited=[False]*self.vertex
    def addundirectededge(self,u,v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u]={v}
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v]={u}
    def addedge(self,u,v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u]={v}
            
    def printedges(self):
        for items in self.graph.keys():
            for item in self.graph[items]:
                print('{}->{}'.format(items,item))
    def adjacentvertices(self,u):
        if u not in self.graph.keys():
            return None
        return self.graph[u]
    def DFS(self,source):
        self.visited[source]=True
        print(source,end='--> ')
        for adjvert in self.adjacentvertices(source):
            if not self.visited[adjvert]:
                self.DFS(adjvert)

    def DFSTraversal(self,source):
        #Can be modified for different applicrin
        #O(V + E)
        self.visited=[False]*(max(self.graph.keys())+1)
        print('DFS Traversal \t')
        self.DFS(source)
        

    def BFSTraversal(self,source):
        currentNode=[source]
        print('BFS Traversal \t')
        self.visited=[False]*(max(self.graph.keys())+1)
        self.visited[source]=True 
        while(len(currentNode)!=0):
            UsedNode=currentNode.pop(0)
            print(UsedNode,end='-->')
            for adjvert in self.adjacentvertices(UsedNode):
                if not self.visited[adjvert]:
                    currentNode.append(adjvert)
                    self.visited[adjvert]=True 
    
    def CycleExist(self):
        source=list(self.graph.keys())[0]
        currentNode=[source]
        self.visited=[False]*(max(self.graph.keys())+1)
        self.visited[source]=True 
        while(len(currentNode)!=0):
            UsedNode=currentNode.pop(0)
            for adjvert in self.adjacentvertices(UsedNode):
                if not self.visited[adjvert]:
                    currentNode.append(adjvert)
                    self.visited[adjvert]=True 
                else:
                    print('The Graph may or may not Contains Cycle')
                    currentNode=[]
                    break



    def NodeLevel(self,source):
        print('Works Correct for indirected no loops')
        currentNode=[[source,0]]
        Levels=[]
        self.visited=[False]*(max(self.graph.keys())+1)
        self.visited[source]=True 
        while(len(currentNode)!=0):
            UsedNode=currentNode.pop(0)
            Levels.append(UsedNode)
            for adjvert in self.adjacentvertices(UsedNode[0]):
                if not self.visited[adjvert]:
                    currentNode.append([adjvert,UsedNode[1]+1])
                    self.visited[adjvert]=True 
                
        return Levels
#GRAPH 1
g = Graph(4)
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 3)
g.addedge(3, 3)
g.printedges()
g.CycleExist()
g.DFSTraversal(0)
print('\n')
g.BFSTraversal(0)
nodeslevel=g.NodeLevel(0)
print('\n\nNode->Level')
for i in nodeslevel:
    print('{}----->{}'.format(i[0],i[1]))


#GRAPGh 2
print('\n\n NEW GRAPH')
g1=Graph(10)
g1.addundirectededge(1,2)
g1.addundirectededge(2,4)
g1.addundirectededge(4,5)
g1.addundirectededge(4,6)
g1.addundirectededge(6,10)
g1.addundirectededge(1,3)
g1.addundirectededge(3,7)
g1.addundirectededge(7,9)
g1.addundirectededge(7,8)
g1.printedges()
g1.CycleExist()
g1.DFSTraversal(1)
print('\n')
g1.BFSTraversal(1)
nodeslevel=g1.NodeLevel(1)
print('\n\nNode->Level')
for i in nodeslevel:
    print('{}----->{}'.format(i[0],i[1]))
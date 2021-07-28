n=int(input("enter no. of tower.Enter number below 10 otherwise long,"))

start="Start"
end="End"
aux="Aux"

count=0
def print_move(start,end):
    global count
    #print("move from",str(start),"to",str(end))
    count+=1
def tower(n,start,end,aux):
    if n==1:
        print_move(start,end)
    else:
        tower(n-1,start,aux,end)
        tower(1,start,end,aux)
        tower(n-1,aux,end,start)
tower(n,start,end,aux)
print(count)
from heapq import *

G = {
    'S' : [('A', 2)],
    'A' : [('S', 2), ('B', 3), ('C', 13) ],
    'B' : [('A', 3), ('C', 5) ],
    'C' : [('A', 13), ('B', 5), ('M', 8)],
    'M' : [('C', 8)]
}

# Indata här: http://technox.se/pass5_pepper.txt

def dijkstra(start,end):
    
    ans = dict()
    queue = list()

    heappush(queue, (0, start))   

    while queue:
        (totdist,node) = heappop(queue)

        if node in ans:
            continue
        
        if node == end:
            return totdist

        ans[node] = totdist


        for (next_node,dist) in G[node]:
            if next_node not in ans:
                heappush(queue, (totdist+dist, next_node))

print(dijkstra('S', 'M'))












#find the sortest path. (used in map to find the sortest root to your destination)
# Undirected Graph
# Weight must be non-negative

# Floyd-Warshall(dense graph) and Johnson algorithm(sparse graphs) will be the better option

# def Dijkstras_with_Start_end(graph, start , end):
#     unvisited = []
#     unvisited = graph.keys()
#     visited = []
#     path = []

#     for key in graph.keys():


#     return sortest_path

def Dijkstras(graph, start):
    unvisited = set(graph.keys())

    dist = {node: float("inf") for node in graph}
    prev = {node : None for node in graph }

    dist[start] = 0

    while unvisited :
        current = min (unvisited, key = lambda n: dist[n])
        if dist[current] == float("inf"):
            break # unreachable node left 

        for neighbor, w in graph[current].items():
            if neighbor in unvisited : 
                nd = dist[current] + w
                if nd < dist[neighbor]:
                    dist[neighbor] = nd 
                    prev[neighbor] = current

        unvisited.remove(current)

    return dist, prev



    

def main():
    graph = {
        "A": {"B":2, "D":8},
        "B" : {"A":2, "D":5, "E":6},
        "C" : {"E":9, "F":3},
        "D" : {"A":8, "B":1, "E":3, "F":2},
        "E" :{"B":6, "C":9, "D":3, "F":1},
        "F" : {"C":3, "E":1, "D":2}
    }

    # shortest_path = Dijkstras(graph, "A", "C")

    print(f"The weight of the edge A -> B is : {graph["B"]["A"]}")
    print(f"The keys of the graph is {graph.keys()}")


    out = Dijkstras(graph, "A")
    print(f"The sortest path from A is : {out}")

if __name__ == "__main__":
    main()
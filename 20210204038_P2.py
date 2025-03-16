import heapq

def read_graph():
    filename = "Input_graph.txt"
    graph = {}
    
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3: 
                u, v, w = parts
                w = int(w)
            else:  
                u, v = parts
                w = 1
            
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            
            graph[u].append((v, w)) 
            graph[v].append((u, w))  
    
    return graph

def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))  
    came_from = {}  
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, f_score

        for neighbor, cost in graph[current]:  
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, None  

graph = read_graph()

heuristic = {
    "A": 6, "B": 4, "C": 3, "D": 5, "E": 2 
}

start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

if start in graph and goal in graph:
    path, f_score = a_star(graph, start, goal, heuristic)
    if path:
        print("\nShortest Path:", " -> ".join(path))
        print("\nf(n) values:")
        for node in path:
            print(f"{node}: {f_score[node]}")
    else:
        print("\nNo path found!")
else:
    print("\nInvalid nodes entered! Make sure they exist in the graph.")

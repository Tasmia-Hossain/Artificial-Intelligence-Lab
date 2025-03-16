'''
Write a Python program that takes a graph as input from the user and write the graph inputs in a file named "Input_graph".  
Read the file and print all the edges (u,v) of the graph.
'''

def write_graph_to_file():
    filename = "Input_graph.txt"
    
    n = int(input("Enter the number of edges: "))
    edges = []
    
    print("Enter the edges in the format 'u v w' :")
    

    for _ in range(n):
        line = input().split()
        if len(line) == 2:
            u, v = line
            w = 1  
        elif len(line) == 3:
            u, v, w = line
        else:
            print("Invalid input. Please enter in the format 'u v' or 'u v w'.")
            continue
        
        edges.append((u, v, int(w))) 
    
    with open(filename, "w") as file:
        for u, v, w in edges:
            file.write(f"{u} {v} {w}\n")
    
    print(f"Graph edges written to {filename}")

def read_graph_from_file():
    filename = "Input_graph.txt"
    edges = []
    
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2: 
                u, v = parts
                w = 1
            elif len(parts) == 3:
                u, v, w = parts
            else:
                continue  
            
            edges.append((u, v, int(w)))  
    
    print("Edges in the graph :")
    for u, v, w in edges:
        print(f"({u}, {v})")

write_graph_to_file()
read_graph_from_file()


''' 5 edges
A B 2
A C 1
B D 4
C D 1
D E 3
'''

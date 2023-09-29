# De La Salle University – Dasmariñas
# Luis Anton P. Imperial
# BCS22

# mapSchool
# Tuesday, August 29, 2023

# heapq is a Python module that implements queue implementation using binary heap (Dijkstra algo and Prim algo)
import heapq

# Create a dictionary to represent the weighted graph
graph = {
    "Home": [("Store A", 7), ("Store B", 14), ("Intersection", 25)],
    "Store A": [("Home", 7), ("Store B", 5)],
    "Store B": [("School", 7)],
    "School": [("Store B", 7), ("Intersection", 7)],
    "Intersection": [("School", 7)]
}

# Vertices (locations) and the values are list of tuples representing neighbors along with the edges weights

# This function represents Dijkstra's algo to find shortest distances and path
def short_path(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    # distance holds the shortest distances from the start vertex, which is set to 0
    distances[start] = 0
    # priority_queue is a min-heap used to select the vertex with the smallest distance
    priority_queue = [(0, start)]
    # previous_vertices tracks the previous vertex that leads to the current vertex
    previous_vertices = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue
    
        for neighbor_vertex, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor_vertex]:
                distances[neighbor_vertex] = distance
                heapq.heappush(priority_queue, (distance, neighbor_vertex))
                previous_vertices[neighbor_vertex] = current_vertex

    shortest_path = []
    while end:
        shortest_path.insert(0, end)
        end = previous_vertices[end]
    
    return distances, shortest_path

start_vertex = "Home"
end_vertex = "School"
shortest_distance, shortest_path = short_path(graph, start_vertex, end_vertex)

print("Shortest Distances:", shortest_distance[end_vertex])
print("Shortest Path:", shortest_path)

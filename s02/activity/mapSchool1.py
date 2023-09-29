# De La Salle University – Dasmariñas
# Luis Anton P. Imperial
# BCS22

# mapSchool1
# Tuesday, August 29, 2023

import heapq

destination_list = {
    "Home": [("Store A", 7), ("Store B", 14), ("Intersection", 25)],
    "Store A": [("Home", 7), ("Store B", 5)],
    "Store B": [("School", 7)],
    "School": [("Store B", 7), ("Intersection", 7)],
    "Intersection": [("School", 7)]
}

def find_destination(destination_list, start_location, end_location):
    dist = {vertex: float('inf') for vertex in destination_list}
    dist[start_location] = 0
    go_here_next = [(0, start_location)]
    previous_vertices = {vertex: None for vertex in destination_list}

    while go_here_next:
        current_distance, current_pathway = heapq.heappop(go_here_next)

        if current_distance > dist[current_pathway]:
            continue

        for neighbor_vertex, weight in destination_list[current_pathway]:
            distance = current_distance + weight

            if distance < dist[neighbor_vertex]:
                dist[neighbor_vertex] = distance
                heapq.heappush(go_here_next, (distance, neighbor_vertex))
                previous_vertices[neighbor_vertex] = current_pathway

    end_goal = []
    while end_location:
        end_goal.insert(0, end_location)
        end_location = previous_vertices[end_location]

    return dist, end_goal

print("Welcome to School Maps!",end="\n")
print("Enter a starting point from any of these choices: ")

for key in destination_list:
    print("- ", key)

point_a = input("Type your Point A: ")
point_b = input("Type your Point B: ")
path_least_traveled, quickest_path = find_destination(destination_list, point_a, point_b)

print("You have chosen", point_a, "as your Starting Point.")
print("You are going to", point_b, "as your End Point. Here are some details.", end="\n\n")
print("Kilometers Left to Destination:", path_least_traveled[point_b], sep = " ")
print("Go Here:", quickest_path, sep=" ")

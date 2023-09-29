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
    while end_location is not None:
        end_goal.insert(0, end_location)
        end_location = previous_vertices[end_location]

    return dist[end_goal[0]]  # Return the shortest distance for the specific journey

## Define variables for output
journeys = []
Prompt = "y"

## Print output
## == Intro ==
print("Welcome to School Maps!", end="\n")
print("Enter a starting point from any of these choices: ")
for key in destination_list:
    print("- ", key)

## == Request input ==
while Prompt == "y":
    point_a = input("Type your Point A: ")
    point_b = input("Type your Point B: ")

    if point_a not in destination_list or point_b not in destination_list:
        print("Invalid starting or ending location. Please choose from the available locations.")
        continue

    path_least_traveled = find_destination(destination_list, point_a, point_b)
    journeys.append((point_a, point_b, path_least_traveled))

    Prompt = input("Do you wish to continue? Answer with y or n:")

print("\n")

for i, journey in enumerate(journeys, start=1):
    point_a, point_b, path_least_traveled = journey  # Unpack the journey tuple
    print(f"Your Journey No. {i} is: {point_a} → {point_b}")
    print(f"- Kilometers Left to Destination: {path_least_traveled}")
    print()  # Print a new line for better formatting

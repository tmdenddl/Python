from collections import deque


# Define Class Station
class Station:
    # Initialize Station's name
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    # Add each other on the neighbours list
    def add_connection(self, another_station):
        self.neighbors.append(another_station)
        another_station.neighbors.append(self)


# Breadth-First Search Algorithm
def bfs(start, goal):
    # Initialize variables
    previous = {}
    queue = deque()
    current = None

    # Initialize
    previous[start] = None
    queue.append(start)

    # Search
    while len(queue) > 0 and current != goal:
        current = queue.popleft()

        # Search through current's neighbors
        for neighbor in current.neighbors:
            # If not seen, add it to the queue and dictionary
            if neighbor not in previous.keys():
                queue.append(neighbor)
                previous[neighbor] = current

    # If path exist
    if current == goal:
        # Make a path and return it
        path = [goal]
        x = goal

        while previous[x] != None:
            x = previous[x]
            path.append(x)

        return path

    # If path does not exist
    return None


# Read stations.txt and save it as dictionary
stations = {}
in_file = open('stations.txt')

# For each station_line
for line in in_file:
    previous_station = None
    data = line.strip().split("-")

    for name in data:
        station_name = name.strip()
        # If station is not defined already
        if station_name not in stations.keys():
            # Make a new instance of the station and add it to stations dictionary
            current_station = Station(station_name)
            stations[station_name] = current_station
        else:
            # If station is defined already
            current_station = stations[station_name]

        # If the previous station has not been declared
        if previous_station != None:
            # Add connection to previous and current stations
            current_station.add_connection(previous_station)

        # Before moving onto the next station
        previous_station = current_station

in_file.close()

# Test
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)

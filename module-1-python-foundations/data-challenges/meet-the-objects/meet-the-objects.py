#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
# TODO: assign `names` and `bikes` to two empty lists
# TODO: loop over `stations`; append each one's "name" to `names`
# TODO: append the same station's "bikes_available" to `bikes`
names = []
bikes = []
for station in stations:
    names.append(station["name"])
    bikes.append(station["bikes_available"])

names.pop(2)

print("stations in the file:", len(stations))
# TODO: loop over range(len(names)); print names[i], "|", bikes[i], "bikes"
for i in range(len(names)):
    print(names[i], "|", bikes[i], "bikes")

# Step 1, answer 1:
# One record contains station_id (text), name (text), capacity, bikes_available (integers), and needs_maintenance (boolean). Separate parallel lists for names and counts can cause them to be easily desynchronized if tampered with.
# Step 1, answer 2:
# .pop(2) removes the element at index 2 from "names". It hands back the string. It shifts the following elements in "names" one position to the left.
# Step 1, answer 3:
# Every station since index 2 gets a bike count that was never theirs (the one after each). "W 52  St & 11 Ave" has a real count that nobody sees.


# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    def __init__(self, name, capacity, bikes_available, station_id, needs_maintenance):
        self.name = name
        self.capacity = int(capacity)
        self.bikes_available = int(bikes_available)
        self.station_id = station_id
        self.needs_maintenance = needs_maintenance

    # TODO: add __init__ with name (str), capacity and bikes_available (int)
    # TODO: in __init__, assign each parameter to self.<same name>
    # TODO: add a parameter and self.<name> for each extra field you agreed
    # TODO: add needs_restock(self): True if bikes_available < capacity / 4
    def needs_restock(self):
        if self.bikes_available < self.capacity/4:
            return True
        else:
            return False
    pass

# TODO: assign `fleet` to []; loop over `stations` as `s`
# TODO: append Station(s["name"], s["capacity"], s["bikes_available"])
# TODO: assign `busy`, `quiet` to two stations with equal needs_restock()
# TODO: print both needs_restock() answers
# TODO: set busy.bikes_available to 0, then print both answers again

fleet = []
for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s["station_id"], s["needs_maintenance"]))
busy = fleet[1]
quiet = fleet[-1]
print(busy.needs_restock(), quiet.needs_restock())

busy.bikes_available = 0



# Step 2, answer 1:
#
# Step 2, answer 2:
#
# Step 2, answer 3:
#
# Step 2, answer 4:
#


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0])
print(fleet[:2])


# TODO: copy your Station class from Step 2 here
# TODO: add __str__(self) to return text like "Grand Army Plaza: 6 of 48 bikes"
# TODO: build it from self.name, self.bikes_available and self.capacity
# TODO: rebuild `fleet` from this class with the same loop as Step 2

class Station:
    def __init__(self, name, capacity, bikes_available, station_id, needs_maintenance):
        self.name = name
        self.capacity = int(capacity)
        self.bikes_available = int(bikes_available)
        self.station_id = station_id
        self.needs_maintenance = needs_maintenance

    # TODO: add __init__ with name (str), capacity and bikes_available (int)
    # TODO: in __init__, assign each parameter to self.<same name>
    # TODO: add a parameter and self.<name> for each extra field you agreed
    # TODO: add needs_restock(self): True if bikes_available < capacity / 4
    def needs_restock(self):
        if self.bikes_available < self.capacity/4:
            return True
        else:
            return False
        return self.bikes_available < self.capacity/4
    def __str__(self):
        return f"{self.name}:{self.bikes_available} of {self.capacity} bikes"

# TODO: assign `fleet` to []; loop over `stations` as `s`
# TODO: append Station(s["name"], s["capacity"], s["bikes_available"])
# TODO: assign `busy`, `quiet` to two stations with equal needs_restock()
# TODO: print both needs_restock() answers
# TODO: set busy.bikes_available to 0, then print both answers again

fleet = []
for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s["station_id"], s["needs_maintenance"]))
busy = fleet[1]
quiet = fleet[-1]
print("before:", busy.needs_restock(), quiet.needs_restock())
busy.bikes_available = 0
print("after:", busy.needs_restock(), quiet.needs_restock())





print(fleet[0])
print(fleet[:2])

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
# TODO: copy your Station class from Step 3 here
# TODO: add __repr__(self) to return text like "Station('Grand Army Plaza', 6)"
# TODO: rebuild `fleet` from this class with the same loop as Step 2
# TODO: assign `van_list` to []; loop over `fleet`
# TODO: append each station whose needs_restock() returns True to `van_list`

class Station:
    def __init__(self, name, capacity, bikes_available, station_id, needs_maintenance):
        self.name = name
        self.capacity = int(capacity)
        self.bikes_available = int(bikes_available)
        self.station_id = station_id
        self.needs_maintenance = needs_maintenance

    def needs_restock(self):
        return self.bikes_available < self.capacity/4
    def __str__(self):
        return f"{self.name}:{self.bikes_available} of {self.capacity} bikes"
    def __repr__(self):
        return f"Station({self.name}, {self.bikes_available})"

fleet = []
for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s["station_id"], s["needs_maintenance"]))
van_list = []
for i in fleet:
    if i.needs_restock():
        van_list.append(i)

busy = fleet[1]
quiet = fleet[-1]
print("before:", busy.needs_restock(), quiet.needs_restock())
busy.bikes_available = 0
print("after:", busy.needs_restock(), quiet.needs_restock())
print(fleet[0])
print(fleet[:2])

print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1:
# 4 stations land in van_list. "print(van_list)" will use __repr__.
# Step 4, answer 2:
# __str__ provides readable text for regular users, whilst __repr__ provides exact strings for programmers.
# Step 4, answer 3:
# I would hand the dispatcher the __str__ format because they could easily read and understand the data that is being provided. If I used __repr__, they'd most likely be confused.

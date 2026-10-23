#!/usr/bin/env python3
"""Data Challenge: Meet the Objects.

Steps, hints and the scenario are in DataChallengeOverview&Steps.md.
"""

import json

DATA_FILE = "bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
# TODO: assign `names` and `bikes` to two empty lists
# TODO: loop over `stations`; append each station's "name" to `names`
#       and its "bikes_available" to `bikes`
# TODO: remove the third station from `names` only, with names.pop(2)

print("stations in the file:", len(stations))
# TODO: loop over range(len(names)); print names[i], "|", bikes[i]
#       and "bikes" on one line

# Your answer: Describe the data file in two or three sentences. What is one
#     record? Which fields are numbers, and which are text? What looks
#     wrong?
# Your answer: What `.pop(2)` removes, what it hands back, and what happens
#     to the positions after it.
# Your answer: Which stations got a bike count that was never theirs? Whose
#     real count does nobody see?


# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    # TODO: add an __init__ that takes name (str), capacity (int) and
    #       bikes_available (int), and assigns each to self.<same name>
    # TODO: add one parameter and one self.<name> line for each other
    #       field your agreed attribute list keeps
    # TODO: add a method needs_restock(self) that returns True when
    #       self.bikes_available is less than self.capacity / 4
    pass


# TODO: assign `fleet` to an empty list; loop over `stations` and
#       append Station(s["name"], s["capacity"], s["bikes_available"])
#       for each one, plus any field you added
# TODO: assign `busy` and `quiet` to two stations in `fleet` whose
#       needs_restock() answers are the same right now
# TODO: print both answers; set busy.bikes_available to 0; then print
#       both answers again

# Your answer: Your own list, made before you compared. Put the dispatcher's
#     words beside each attribute.
# Your answer: Where your two lists differed, what each of you argued, and
#     which list you kept.
# Your answer: Which field from the file you left out, and why the
#     dispatcher does not need it.
# Your answer: Why your two stations prove independence, with their answers
#     before and after.


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0])
print(fleet[:2])


# TODO: copy your Station class from Step 2 here, then add a method
#       __str__(self) that returns text like
#       "Grand Army Plaza: 6 of 48 bikes", built from self.name,
#       self.bikes_available and self.capacity
# TODO: rebuild `fleet` from this class with the same loop as Step 2

print(fleet[0])
print(fleet[:2])

# Your answer: Before you run: the shape you expect from each of the four
#     prints, in order.
# Your answer: Which prediction was wrong, and which method does a list use
#     instead of `__str__`?


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
# TODO: copy your Station class from Step 3 here, then add a method
#       __repr__(self) that returns text like
#       "Station('Grand Army Plaza', 6)"
# TODO: rebuild `fleet` from this class with the same loop as Step 2
# TODO: assign `van_list` to an empty list; loop over `fleet` and
#       append every station whose needs_restock() returns True

print(van_list)
for station in van_list:
    print(station)

# Your answer: Before you run: how many stations land in `van_list`, and
#     which method `print(van_list)` will use.
# Your answer: What each display method is for, and who reads it.
# Your answer: Which printout you would hand the dispatcher, and why.

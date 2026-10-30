#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json

DATA_FILE = "station_taps.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====

# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs

def scan_for(tap_id, records):
    comparisons = 0
    for row in records:
        comparisons += 1
        if row[0] == tap_id:
            return comparisons
    return comparisons
print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Step 1, answer 1:
# T001 should display with a 1, as it appears once. Both T040 and T999 should appear with a 40 because the maximum rows of data is 40, it cannot go higher if there is not more data.
# Step 1, answer 2:
# You should plan around 40, because this is the total amount of rows of data that there are, encapsulating the csv file's content.


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop

for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
    print("rows:", size, "| worst-case comparisons:", worst)
pairs = 0
for x in taps:
    for tap in taps:
        pairs += 1
print(len(taps), pairs) 
big = len(taps) * 10
print("worst case:", big, "pair loop:", big * big)

# Step 2, answer 1:
# I expect there to be a count of 40, 1600 (400 worst case and 160000 pair loop). 40 x 40 = 1600, 400 x 400 = 160000
# Step 2, answer 2:
# The scan goes through every row and counts it one by one. As it increases, so does the pair loop, multiplied.


# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons
card_ids = []
tap_counts = []
comparisons = 0
for row in taps:
    card = row[1]
    found = False
    for i in range(len(card_ids)):
        comparisons += 1
        if card_ids[i] == card:
            tap_counts[i] += 1
            found = True
            break
    if not found:
        card_ids.append(card)
        tap_counts.append(1)
busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# Step 3, answer 1:
# It has to be less than 480 (40 rows x 12) due the potential aspect of there being repeats
# Step 3, answer 2:
# I got an output of 190, and it is bigger than the number of rows because there are 40 rows - but some don't count.


# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set

taps_by_card = {}
lookups = 0
for row in taps:
    lookups += 1
    card_id = row[1]
    if row[1] in taps_by_card:
        taps_by_card[row[1]] += 1
    else:
        taps_by_card[row[1]] = 1
stations = set()
for row in taps:
    stations.add(row[2])
repeat_riders = 0
for row in taps_by_card.values():
    if row > 1:
        repeat_riders += 1
print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1:
# A dict has to look at each row. Since there are 40 rows, I predict that 40 will be the output.
# Step 4, answer 2:
# As the Input Size grows, parallel lists depend on the amount of unique cards. As the Input Size grows, so will the dict with each lookup.
# Step 4, answer 3:
# Parallel lists pair a card with its count, and it goes through the list until it finds what it looks for. Sets show the amount of stations there are without duplicates. Dict uses key identification to match cards with count.
# Step 4, answer 4:
# The card that is only tapped once, which is C012.


# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes

summary = {
    "service_day": "2026-03-02",
    "total_taps": len(taps),
    "distinct_cards": len(taps_by_card),
    "stations": stations,
    "taps_by_card": taps_by_card,
}
print("about to serialize", len(summary), "keys")
text = json.dumps(summary, indent=2)
print(text)

# Step 5, answer 1:
# TypeError: Object of type set is not JSON serializable
# Step 5, answer 2:
# What caused the TypeError was the set because JSON files don't support set.
# Step 5, answer 3:
# Yes it did, and this tells me that the dict was working, the issue falls onto the set that isn't supported by the JSON file.


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived

summary["stations"] = sorted(stations)
with open("tap_summary.json", "w") as f:
    json.dump(summary, f)
with open("tap_summary.json", "r") as f:
    reloaded = json.load(f)
print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1:
# Yes they can, and this is because we were able to get outputs on the total amount of taps a card has previously (C001 had 6).
# Step 6, answer 2:
# 'taps_by_card' survived the round trip, while stations changed from a set (didn't work) to a list.

#!/usr/bin/env python3
"""Data Challenge: Pick the Right Container.

Steps, hints and the scenario are in DataChallengeOverview&Steps.md.
"""

import json

DATA_FILE = "station_taps.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====

# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs
def scan_for(tap_id, records):
    # TODO: assign `comparisons` to 0
    # TODO: loop over `records`; add 1 to `comparisons` for every row
    # TODO: inside the loop, return `comparisons` when row[0] == tap_id
    # TODO: after the loop, return `comparisons`
    pass


print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Your answer: Before you run: your predicted counts for T001, T040 and
#     T999, and how you got each.
# Your answer: Which of the three counts should you plan around, and why?


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
# TODO: loop over the sizes [5, 10, 20, 40]; assign `worst` to
#       scan_for("T999", taps[:size]) and print `size` and `worst`
# TODO: assign `pairs` to 0; loop over `taps` with a second loop over
#       `taps` inside it, adding 1 to `pairs` for every pair
# TODO: print len(taps) and `pairs`
# TODO: assign `big` to len(taps) * 10; print what the scan and the
#       pair loop would each cost on `big` rows

# Your answer: Before you run: every count you expect, with the arithmetic
#     beside it.
# Your answer: The scan's pattern in one sentence, then the pair loop's,
#     with no notation.


# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons
# TODO: assign `card_ids` to an empty list (each card, first-seen order)
# TODO: assign `tap_counts` to an empty list (the count for card_ids[i])
# TODO: assign `comparisons` to 0
# TODO: loop over `taps`; assign `card` to row[1] and `found` to False
# TODO: inside it, loop over range(len(card_ids)); add 1 to
#       `comparisons`; when card_ids[i] == card, add 1 to
#       tap_counts[i], set `found` to True and break
# TODO: after the inner loop, if not found, append `card` to card_ids
#       and 1 to tap_counts

busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# Your answer: Before you run: how many comparisons do you expect?
# Your answer: After: the real count, and why it is bigger than the number
#     of rows.


# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set
# TODO: assign `taps_by_card` to an empty dict (card ID: tap count)
# TODO: assign `lookups` to 0
# TODO: loop over `taps`; add 1 to `lookups`, then add 1 to row[1]'s
#       count in `taps_by_card`, or set it to 1 if it is not there yet
# TODO: assign `stations` to set(); loop over `taps` and .add() row[2]
# TODO: assign `repeat_riders` to 0; loop over `taps_by_card` and add 1
#       for every card whose count is more than 1

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Your answer: Before you run: your `lookups` prediction and the rule behind
#     it.
# Your answer: Finish "As the Input Size grows..." for the parallel lists,
#     then for the dictionary.
# Your answer: For each container, name its job and how it finds what it
#     needs. What would a list have cost you for `stations`?
# Your answer: Which card explains the gap between distinct cards and repeat
#     riders?


# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes
# TODO: replace each None: the row count, the distinct-card count,
#       `stations` exactly as you built it, and `taps_by_card`
summary = {
    "service_day": "2026-03-02",
    "total_taps": None,
    "distinct_cards": None,
    "stations": None,
    "taps_by_card": None,
}

print("about to serialize", len(summary), "keys")
# TODO: run the file and answer below before you change anything
# TODO: then put # in front of the next two lines so Step 6 can run
text = json.dumps(summary, indent=2)
print(text)

# Your answer: The last line of the error, exactly as printed.
# Your answer: Which key caused it, and why, in your own words.
# Your answer: Did `about to serialize` print before the error? What does
#     that tell you?


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived
# TODO: assign summary["stations"] to a type JSON can hold; keep the key
# TODO: write `summary` to "tap_summary.json" with json.dump(), inside
#       a with open("tap_summary.json", "w") block
# TODO: replace None with json.load() of "tap_summary.json", inside a
#       second with open(...) block
reloaded = None

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Your answer: Can the overnight job get one card's count from this file
#     without the raw log? How do you know?
# Your answer: Which container survived the round trip, and which came back
#     as something else?

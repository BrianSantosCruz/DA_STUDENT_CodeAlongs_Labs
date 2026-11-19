#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    comparisons = 0
    for member in members:
        comparisons += 1
        if member["member_id"] == member_id:
            return member, comparisons
    return None, comparisons
    # TODO: assign `comparisons` to 0
    # TODO: loop over `members`; add 1 to `comparisons` for every row
    # TODO: inside the loop, return row, comparisons on a member_id match
    # TODO: after the loop, return None, comparisons
    pass


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
# My predicted count of M1150 is 150 because a linear search would mean that since M1150 is the 150th entry, it will also have the exact count of 150.


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
# TODO: open CHECKINS_FILE in a with block as `f`
# TODO: inside it, assign `swipes` to f.read().splitlines()
# TODO: assign `linear_total` and `not_members` to 0
# TODO: loop over `swipes`; call find_linear(members, member_id)
# TODO: print the ID, the name or "NOT A MEMBER", and the comparisons
# TODO: add each count to `linear_total`
# TODO: add 1 to `not_members` for every swipe with no row
with open(CHECKINS_FILE) as f:
    swipes = f.read().splitlines()
linear_total = 0
not_members = 0
for member_id in swipes:
    row, count = find_linear(members, member_id)
    if row is None:
        print(member_id, "NOT A MEMBER", count)
        not_members += 1
    else:
        print(member_id, row["name"], count)
        linear_total += count


print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Step 2, answer 1:
# The cost of the first three swipes would be 4 + 12 + 27 which would equal to 43. The cost of a swipe
# that is not a member would be 312 because the linear search would go through the entire csv file to search (and not find).
# Step 2, answer 2:
# The non member swipes of M1313 and M2041 both cost the most at 312 because they linear search went through the entire csv file
# to search.


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
# TODO: assign `members_by_id` to an empty dict and `build_steps` to 0
# TODO: loop over `members`; store each row under row["member_id"]
# TODO: add 1 to `build_steps` for every row
# TODO: write find_dict(members_by_id, member_id)
# TODO: make find_dict() return members_by_id.get(member_id), 1

members_by_id = {}
build_steps = 0
for row in members:
    members_by_id[row["member_id"]] = row
    build_steps += 1

def find_dict(members_by_id, member_id):
    return members_by_id.get(member_id), 1

print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

# TODO: assign `linear_running` to 0 and `dict_running` to build_steps
# TODO: assign `pays_off_at` to None and `swipe_number` to 0
linear_running = 0
dict_running = build_steps
pays_off_at = None
swipe_number = 0


for member_id in swipes:
    # TODO: add 1 to `swipe_number`
    swipe_number += 1
    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)
    linear_running += linear_count
    dict_running += dict_count
    print(swipe_number, member_id, linear_running, dict_running)
    # TODO: add each search's count to its running total
    # TODO: print swipe_number, the ID and both running totals
    # TODO: the first time dict_running < linear_running, set `pays_off_at'
    if pays_off_at is None and dict_running < linear_running:
        pays_off_at = swipe_number

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
# The dict total first drops below the linear total at swipe 6.
# Step 3, answer 2:
# It fits the door's job because a dictionary allows for a member to be matched to their ID at once, as well as those that
# aren't members. There is no search throughout the entire database. 6 M1313 574 318 is where it pulled ahead.
# Step 3, answer 3:
# A morning that isn't busy and has barely any visitors would make a plain list the better choice, as the 312-row dictionary would be unnecessary.


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
# TODO: replace the text below with your AI's claim, word for word
ai_claim = "A dictionary lookup is roughly 100 to 150 times faster than a linear search for 20 lookups in a 312-row list—though in real-world wall-clock time, both finish in well under a millisecond. How the Math Breaks Down • Linear search (O(n)): To find an item in a 312-row list, Python checks roughly half the list on average (156 comparisons) if the item exists, or all 312 if it doesn't. Across 20 lookups, that is 3,120 to 6,240 comparisons. • Dict lookup (O(1)): A dictionary hashes the key and jumps straight to the memory slot in a single step. Across 20 lookups, that is just 20 operations. The Practical Catch (Setup Cost) If you already have a dictionary, it wins easily. However, if your data starts as a list and you only need to do 20 lookups once, converting the list into a dictionary first actually takes longer than just scanning the list 20 times: • Building the dict: Requires reading all 312 rows once, hashing every key, and allocating memory (~312+ operations with higher per-step overhead). • Rule of thumb: Stick with a simple list scan if you are doing fewer than ~50–100 lookups on a 312-row list. Switch to a dictionary if the list is reused across multiple calls, sits inside a loop, or might grow larger later. If you share how the 312-row list is structured (e.g., list of dicts, tuples, or objects) and whether it's reused, I can show you the cleanest way to optimize your lookup code."
print("AI CLAIM:", ai_claim)

# TODO: unpack find_linear() for swipes[0] into `_, front_count`
# TODO: unpack find_linear() for "M1313" into `_, absent_count`
# TODO: assign `ratio` to round(linear_running / dict_running, 1)
_, front_count = find_linear(members, swipes[0])
_, absent_count = find_linear(members, "M1313")
ratio = round(linear_running / dict_running, 1)


print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

# TODO: replace the text below with your own verdict
verdict = "The real speed was 8.8x faster instead of the 100-150x claim of the AI, based on the ratio that the output provided."
print("VERDICT:", verdict)

# Step 4, answer 1:
# The missing ID prediction matched at 312 with the non-member swipes (absent_count). It missed the ratio/times faster, giving me
# 100-150x speed whilst the output gave me a 8.8x ratio.
# Step 4, answer 2:
# No, it did not account for the build cost, but this was acknowledged in the AI's response under The Practical Catch. After
# pasting, the AI confirmed that the speed would be a ratio of 8.8x when taking into consideration the build cost.

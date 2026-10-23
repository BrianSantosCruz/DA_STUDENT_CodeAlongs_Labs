#!/usr/bin/env python3
"""Data Challenge: Lookups Matter.

Steps, hints and the scenario are in DataChallengeOverview&Steps.md.
"""

import csv

DATA_FILE = "member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    # TODO: assign `comparisons` to 0
    # TODO: loop over `members`; add 1 to `comparisons` for every row
    # TODO: inside the loop, when row["member_id"] == member_id,
    #       return two things: row, comparisons
    # TODO: after the loop, return None, comparisons
    pass


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Your answer: Before you run: your predicted count for `M1150`, and how you
#     got it.


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
# TODO: inside a with open(CHECKINS_FILE) block, assign `swipes` to
#       f.read().splitlines()
# TODO: assign `linear_total` and `not_members` to 0
# TODO: loop over `swipes`; call find_linear(members, member_id) and
#       print a line like M1004 | Dev Okafor | comparisons: 4, or
#       M1313 | NOT A MEMBER | comparisons: 312 when there is no row
# TODO: add each count to `linear_total`; add 1 to `not_members` for
#       every swipe with no row

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Your answer: Before you run: the cost of each of the first three swipes,
#     their sum, and the cost of a swipe that is not a member.
# Your answer: Which swipe cost the most, and why?


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
# TODO: assign `members_by_id` to an empty dict and `build_steps` to 0
# TODO: loop over `members`; store each row under row["member_id"] and
#       add 1 to `build_steps`
# TODO: write find_dict(members_by_id, member_id) that returns two
#       things: members_by_id.get(member_id), 1

print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

# TODO: assign `linear_running` to 0, `dict_running` to build_steps,
#       `pays_off_at` to None and `swipe_number` to 0
# TODO: loop over `swipes`; add 1 to `swipe_number`, add each search's
#       count to its running total, and print a line like
#       swipe 1 M1004 | linear so far: 4 | dict so far: 313
# TODO: the first time dict_running < linear_running, set
#       `pays_off_at` to swipe_number

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Your answer: Before you run: at which swipe does the dict total first drop
#     below the linear total?
# Your answer: Why a dictionary keyed on `member_id` fits the door's job.
#     Quote the swipe where it pulled ahead.
# Your answer: A morning where the plain list would be the better choice.


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
# TODO: replace the text below with your AI's claim, word for word
ai_claim = "TODO: paste what your AI actually told you"
print("AI CLAIM:", ai_claim)

# TODO: assign `front_count` to the count find_linear() gives for the
#       first swipe, swipes[0]
# TODO: assign `absent_count` to the count it gives for "M1313"
# TODO: assign `ratio` to linear_running / dict_running, rounded to
#       1 decimal place

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

# TODO: replace the text below with your own verdict: name O(n) and
#       O(1) Average-Case, and quote at least one of your counts
verdict = "REPLACE ME"
print("VERDICT:", verdict)

# Your answer: Hold the AI's claim against your three comparisons. Which one
#     did it match, and which did it miss?
# Your answer: Did its number count the cost of building the dictionary?
#     What did it say when you pasted your totals back?

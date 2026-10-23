#!/usr/bin/env python3
"""Data Challenge: One Job at a Time.

Steps, hints and the scenario are in DataChallengeOverview&Steps.md.
"""

import json

DATA_FILE = "pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    # TODO: replace this line with a one-sentence docstring
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `parts` to `record` split on commas
    # TODO: if `parts` does not hold 5 fields, return False and
    #       "wrong field count"
    # TODO: if parts[2] is empty after .strip(), return False and
    #       "missing category"
    # TODO: in a try, call float(parts[3]); in except ValueError,
    #       return False and "pounds is not a number"
    # TODO: return True and ""
    pass


# TODO: assign `records` to read_donations(DATA_FILE), `valid` to []
# TODO: loop over `records`; unpack validate_donation(record) into
#       `ok` and `reason`; append good records to `valid`, else
#       print "rejected", the ID plus ":", and `reason`
print(len(valid), "usable records out of", len(records))

# Your answer: Before you code: what does one record hold, and which records
#     already look wrong?
# Your answer: Name three things your validator promises about each record
#     it keeps.


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `by_category` to {} and `total_pounds` to 0.0
    # TODO: loop over `valid_records`; split each record and assign
    #       `category` to parts[2] and `pounds` to float(parts[3])
    # TODO: if `category` is not in `by_category`, set its entry to
    #       {"donations": 0, "pounds": 0.0}
    # TODO: add 1 to its "donations", add `pounds` to its "pounds",
    #       and add `pounds` to `total_pounds`
    # TODO: return a dict with "records" (len(valid_records)),
    #       "total_pounds" and "by_category"
    pass


# TODO: assign `summary` to summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Your answer: Hand-count one category's pounds off the CSV. Which category,
#     what did you get, and does it match your printed line?


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    # TODO: add a one-sentence docstring naming its one job
    # TODO: inside a with open(path, "w") block, write `summary` with
    #       json.dump(summary, f, indent=2)
    # TODO: return `path`
    pass


def run_pipeline(in_path, out_path, summarize):
    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `kept` to the records from read_donations(in_path)
    #       that validate_donation() passes
    # TODO: return export_summary() of summarize(kept) and `out_path`
    pass


written = run_pipeline(DATA_FILE, "donation_summary.json",
                       summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])

# Your answer: What did `print(len)` and `print(len("abc"))` each print, and
#     what do the parentheses do?
# Your answer: Read the four printed docstring lines with your partner. Does
#     any one need "and" twice?


# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    # TODO: add a one-sentence docstring naming its one job
    # TODO: return the same shape as summarize_donations(), keyed by
    #       the date in parts[4] under "by_day" instead of category
    pass


# TODO: call run_pipeline() with DATA_FILE, "donation_summary.json"
#       and summarize_by_day
# TODO: replace None with json.load() of "donation_summary.json",
#       inside a with open(...) block
reloaded = None

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

# Your answer: How many of your other functions did you edit for the swap?
#     If any, what was the summarizer reaching into?
# Your answer: Three dates show only 1 donation. Why, and what should the
#     coordinator see?

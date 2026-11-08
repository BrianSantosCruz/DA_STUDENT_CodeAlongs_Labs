#!/usr/bin/env python3
"""One Job at a Time: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    """Read the donation log into one raw string per record."""
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    # TODO: add a one-sentence docstring naming its one job
    """Returns a verdict or reason of a record"""
    # TODO: assign `parts` to `record` split on commas
    parts = record.split(",")
    # TODO: return False, "wrong field count" if `parts` lacks 5 fields
    if len(parts) != 5:
        return (False, "wrong field count")
    # TODO: return False, "missing category" if parts[2].strip() is ""
    if parts[2].strip() == "":
        return(False, "missing category")
    # TODO: in a try, call float(parts[3])
    try:
        float(parts[3])
    except ValueError:
        return (False, "pounds is not a number")
    return (True, "")
    # TODO: in except ValueError, return False, "pounds is not a number"
    # TODO: return True and ""
    pass


# TODO: assign `records` to read_donations(DATA_FILE), `valid` to []
records = read_donations(DATA_FILE)
valid = []
# TODO: loop over `records`; unpack validate_donation(record) as ok, reason
for record in records:
    ok, reason = validate_donation(record)
    if ok:
        valid.append(record)
    else:
        print("rejected", record.split(",")[0] + ":", reason)
# TODO: if `ok`, append `record` to `valid`
# TODO: else print "rejected", the record's ID plus ":", and `reason`
print(len(valid), "usable records out of", len(records))

# Step 1, answer 1:
# One record holds the donation_id, item, category, pounds, and received_on. I see that some records are missing an entire data value, or a whole column.
# Step 1, answer 2:
# Three things the validator promises are the 5 fields, non empty category, and string grounds value.


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    """One function, `summarize_donations()`, with one loop and one dict that totals pounds per category."""
    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `by_category` to {} and `total_pounds` to 0.0
    by_category = {}
    total_pounds = 0.0
    # TODO: loop over `valid_records`; split each record on commas into `parts`
    for row in valid_records:
        parts = row.split(",")
        category = parts[2]
        pounds = float(parts[3])
        if category not in by_category:
            by_category[category] = {"donations" : 0, "pounds": 0.0}
        by_category[category]["donations"] += 1
        by_category[category]["pounds"] += pounds
        total_pounds += pounds
        
    # TODO: start that entry as {"donations": 0, "pounds": 0.0}
    # TODO: add 1 to its "donations" and `pounds` to its "pounds"
    # TODO: add `pounds` to `total_pounds`
    

    # TODO: return a dict of "records", "total_pounds" and "by_category"
    return {"records": len(valid_records),
            "total_pounds": total_pounds,
            "by_category": by_category
    }

summary = summarize_donations(valid)
# TODO: assign `summary` to summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Step 2, answer 1:
# I chose dairy and I counted 20.0 lbs, which matches my output.


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    # TODO: add a one-sentence docstring naming its one job
    """One function, `export_summary()`, that writes a summary to a JSON file."""
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
    return path
    # TODO: in a with open(path, "w") block, json.dump `summary`, indent=2
    # TODO: return `path`
    pass


def run_pipeline(in_path, out_path, summarize):
    """One function, `run_pipeline()`, that calls the others in order. The summarizer is one of its parameters."""
    # TODO: add a one-sentence docstring naming its one job
    kept = []
    for x in read_donations(in_path):
        valid, reason = validate_donation(x)
        if valid:
            kept.append(x)
    return export_summary(summarize(kept), out_path)
    # TODO: assign `kept` to [] and loop over read_donations(in_path)
    # TODO: append each record that validate_donation() passes to `kept`
    # TODO: return export_summary() of summarize(kept) and `out_path`
    pass


written = run_pipeline(DATA_FILE, "donation_summary.json",
                      summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])

# Step 3, answer 1:
# print(len) gave me the function reference object, whilst print(len("abc")) calls the function with parentheses and returns the integer 3.
# Step 3, answer 2:
# My partner and I came to the conclusion that no, there is no need for "and" twice.


# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    """Summarizes valid records by records, total pounds and per day
    This function does not validate records."""
    by_day = {}
    total_pounds = 0.0
    for x in valid_records:
        parts = x.split(',')
        day = parts[4]
        pounds = float(parts[3])
        if day not in by_day:
            by_day[day] = {"donations": 0, "pounds": 0.0}
        by_day[day]["donations"] += 1
        by_day[day]["pounds"] += pounds
        total_pounds += pounds
    return {"records" : len(valid_records),
            "total_pounds" : total_pounds,
            "by_day" : by_day
        }

summary = summarize_by_day(valid)
# TODO: assign `summary` to summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for day, stats in summary["by_day"].items():
    print(day, stats["donations"], "donations,", stats["pounds"],
          "lbs")



# Step 4, answer 1:
# I edited quite a few functions (I didn't count) and the summarizer was reaching into the amount of times an item was counted for each date. 
# Step 4, answer 2:
# The three dates showing one donation each (2026-09-05, 2026-09-07, and 2026-09-09) because there is missing data values or columns, which is something the coordinator should see.

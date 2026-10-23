#!/usr/bin/env python3
"""Data Challenge: Validate, Catch, Keep Going.

Steps, hints and the scenario are in DataChallengeOverview&Steps.md.
"""

DATA_FILE = "service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason
# TODO: assign `EXPECTED_FIELDS` to 5
# TODO: assign `ALLOWED_STATUS` to a list of "Open", "In Progress"
#       and "Closed"


def validate_request(row):
    # TODO: assign `fields` to `row` split on commas
    # TODO: if len(fields) is not EXPECTED_FIELDS, return False and
    #       "wrong field count: " plus the count as text
    # TODO: unpack `fields` into request_id, complaint_type, borough,
    #       days_open and status
    # TODO: if `borough` is empty, return False and "borough is empty"
    # TODO: if `status` is not in ALLOWED_STATUS, return False and
    #       "status not allowed: " plus `status`
    # TODO: return True and "ok"
    pass


print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Your answer: Before you code: two or three sentences on what is in the
#     file. What does one row hold, and what already looks wrong?
# Your answer: How does the caller take the two returned values apart in one
#     line, and what is the function really handing back?


# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection
# TODO: assign `valid` to 0
# TODO: loop over `rows`; unpack validate_request(row) into `ok` and
#       `reason`; add 1 to `valid` when `ok` is True, else print the
#       row's ID (row.split(",")[0]), "REJECTED -" and `reason`

print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Your answer: Before you run: how many rows fail your three rules by your
#     own hand count, and which rule does each break?
# Your answer: Read the rows that passed. Which ones got through that should
#     not have, and why can your validator not see them?


# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash
# TODO: assign `total_days` and `counted` to 0
# TODO: loop over `rows`; skip any row validate_request() rejects
#       with `continue`
# TODO: assign `days_open` to int() of the row's fourth field; add it
#       to `total_days`, add 1 to `counted`, then print the row's ID,
#       "days open:" and `days_open`
# TODO: once you have your answers, put # in front of every line of
#       this step so Step 4 can run

print("average days open:", total_days / counted)

# Your answer: Before you run: how many report lines print before it
#     crashes, and which row stops it?
# Your answer: The last line of the traceback, exactly as printed, and how
#     many rows were counted before it.
# Your answer: What happens to the rows the loop never reached?


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    # TODO: in a try, assign `days` to int(value); in
    #       except ValueError, return False and
    #       "days_open is not a number: " plus `value`
    # TODO: if `days` is below 0, return False and
    #       "days_open is negative: " plus `value`
    # TODO: return True and "ok"
    pass


# TODO: assign `total_days`, `counted` and `skipped` to 0
# TODO: loop over `rows`; unpack validate_request(row) into `ok` and
#       `reason`; if ok, unpack check_days_open() of the fourth field
#       into `ok` and `reason` too
# TODO: if still ok, add the days to `total_days` and 1 to `counted`;
#       else add 1 to `skipped` and print the ID, "SKIPPED -", reason

print("counted:", counted, "| skipped:", skipped)
print("average days open:", round(total_days / counted, 1))

# Your answer: Before you run: how many rows get skipped now, and which ones
#     did your Day 1 validator let through?
# Your answer: For `3 days` and for `-3`: did an `if` or a `try` catch it,
#     and could the other tool have?
# Your answer: Does `counted` plus `skipped` account for every row? Show the
#     sum.

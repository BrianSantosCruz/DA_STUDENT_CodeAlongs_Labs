#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason

EXPECTED_FIELDS = 5
ALLOWED_STATUS = ["Open", "In Progress", "Closed"]

def validate_request(row):
    fields = row.split(",")
    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong field count: " + str(len(fields))
    request_id, complaint_type, borough, days_open, status = fields
    if borough == (""): 
        return False, "borough is empty"
    if not status in ALLOWED_STATUS:
        return False, "status not allowed: " + status
    else:
        return True, "ok"


print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Step 1, answer 1:
# # The csv file contains information of specific complaints/requests made by people. Each row contains the request_id, complaint_type, borough, days_open, and status. SR-1004 already has a missing value for borough, and the -3 is confusing me in SR-1013.
# Step 1, answer 2:
# # The caller forms it into a tuple, as if 'False' and 'borough is empty' were together. What this really does is hand back a boolean of True or False with a reason, whether it be 'ok', 'borough is empty', or 'status not allowed:'.



# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection
# TODO: assign `valid` to 0
# TODO: loop over `rows`; unpack validate_request(row) into ok, reason
# TODO: if `ok`, add 1 to `valid`
# TODO: else print row.split(",")[0], "REJECTED -" and `reason`
valid = 0
for row in rows:
    ok, reason = validate_request(row)
    if ok:
        valid += 1
    else:
        print(row.split(",")[0], "REJECTED -", reason)

print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Step 2, answer 1:
# 3 rows fail - SR-1004, SR-1009, and SR-1011. This is because SR-1004 is missing a value in borough, SR-1009 is using an incorrect status, and SR-1011 only has 4 columns.
# Step 2, answer 2:
# SR-1007 should not have passed because it reads '3 days' instead of '3' for the days_open column. Similarly, SR-1013 uses -3, which makes no sense. These two passed because there was nothing set in order to reject a mistake in the days_open column, meaning that the code doesn't recognize anything wrong within that column - there is no check.

# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash

#total_days = 0
#counted = 0
#for row in rows:
#    ok, reason = validate_request(row)
#    if not ok:
#        continue
#    fields = row.split(",")
#    days_open = int(fields[3])
#    total_days += days_open
#    counted += 1
#    print(fields[0], days_open)
#print("average days open:", total_days / counted)

# Step 3, answer 1:
# SR-1007 should stop it, and it should go through SR-1001 to SR-1006 without any issue.
# Step 3, answer 2:
# ValueError: invalid literal for int() with base 10: '3 days', and SR-1001 to SR-1006 was counted with the exception of SR-1004.
# Step 3, answer 3:
# The rows the loop never reaches don't get counted.


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    try:
        days = int(value)
    except ValueError:
        reason = "days_open is not a number: " + value
        return False, reason
    if days < 0:
        reason = "days_open is negative: " + value
        return False, reason
    return True, "ok"

total_days = 0
counted = 0
skipped = 0
for row in rows:
    ok, reason = validate_request(row)
    if ok:
        ok, reason = check_days_open(row.split(",")[3])
    if ok:
        total_days += int(row.split(",")[3])
        counted += 1
    else:
        skipped += 1
        print(f"{row.split(",")[0]}, SKIPPED -", reason)

print("counted:", counted, "| skipped:", skipped)
print("average days open:", round(total_days / counted, 1))

# Step 4, answer 1:
# It should now skip 5 rows - SR-1007 and SR-1013 were not counted in Day 1.
# Step 4, answer 2:
# The if caught the -3 and the try caught the 3 days. The tools could not have caught the other one's value, because the if was meant to catch values under 0, whilst the try was meant to find a value that didn't belong (for example, the string).
# Step 4, answer 3:
# Counted and skipped account for every row. There are 15 rows in the csv file, and 'counted' got 10 rows, whilst 'skipped' got 5. 10 + 5 = 15.

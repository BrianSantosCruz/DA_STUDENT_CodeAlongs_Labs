#!/usr/bin/env python3
"""Data Challenge: Looks Right. Is It?

Steps, hints and the scenario are in DataChallengeOverview&Steps.md.
"""

DATA_FILE = "timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()


# ===== Day 1 =====

# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause
# TODO: run the file as given and read the traceback from the bottom up
# TODO: add print(repr(hours)) as the first line of add_hours(), run
#       again, and find that value in the CSV
# TODO: find the line that reads the wrong column and change the index
#       to the hours column; wrap it in int() so it adds a number
# TODO: delete the print(repr(hours)) line once Rosa's total is right
def add_hours(total, hours):
    return total + hours


def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            total = add_hours(total, parts[2])
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))

# Your answer: Before you run: Rosa's weekly hours (E101), added up by hand
#     from the CSV.
# Your answer: How to read a traceback, in 2-3 bullets: what the last line
#     tells you, what each block above it tells you, and where you found
#     that out.
# Your answer: Which function the traceback ended in, and which line really
#     held the bug.


# Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List
# TODO: run the file as given; note the last ID that printed
# TODO: compare every ID in `staff` with the IDs in the CSV
# TODO: replace the hand-typed `staff` list with an empty list and a
#       loop over lines[1:] that appends each row's employee ID once
# TODO: print "employees in the file:" and len(staff)
def days_worked(lines, emp_id):
    days = 0
    for row in lines[1:]:
        if row.split(",")[0] == emp_id:
            days = days + 1
    return days


staff = ["E101", "E102", "E103", "E106", "E105"]
for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)
    print(emp_id, "| hours:", hours, "| days:", days,
          "| average per day:", hours / days)

# Your answer: Before you run: how many employees are in the CSV, counted by
#     eye?
# Your answer: How many lines printed before the crash, and which ID did it
#     stop on?
# Your answer: Where the bug lives, in the division line or somewhere above
#     it, and why, in one sentence.


# ===== Day 2 =====

# Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong
# TODO: add up Rosa's (E101) and Mei's (E103) hours by hand first
# TODO: add print("starting", emp, "total is", total) as the first
#       line inside the outer loop; every employee should start at 0
# TODO: find the line that sets `total` in the wrong place and move it
#       inside the outer loop, so it resets for every employee
# TODO: delete the "starting" print once all five totals are right
records = []
for row in lines[1:]:
    emp_id, name, day, hours, rate = row.split(",")
    records.append({"id": emp_id, "name": name, "day": day,
                    "hours": int(hours), "rate": float(rate)})

employee_ids = []
for r in records:
    if r["id"] not in employee_ids:
        employee_ids.append(r["id"])

total = 0
for emp in employee_ids:
    name = ""
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]
    print(emp, name, "| weekly hours:", total)

# Your answer: Before you run: Rosa's and Mei's weekly hours, added up by
#     hand from the CSV.
# Your answer: What `total` held at the start of each employee's count, and
#     the one line that explains it.
# Your answer: Why is Rosa's number right while Priya's equals the whole
#     staff's hours for the week?


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week
# TODO: work out Rosa's, Darnell's and Mei's pay by hand first
# TODO: fix weekly_pay() so it follows the handbook rule word for word:
#       base rate for the first 40 hours, 1.5 times base rate only for
#       the hours beyond 40
# TODO: find the other line that compares `total` against 40 and fix
#       it the same way
def weekly_pay(hours, rate):
    if hours >= 40:
        return hours * rate * 1.5
    return hours * rate


owed_overtime = 0
payroll = 0.0
for emp in employee_ids:
    total = 0
    name = ""
    rate = 0.0
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            rate = r["rate"]
            total = total + r["hours"]
    if total >= 40:
        owed_overtime = owed_overtime + 1
    pay = weekly_pay(total, rate)
    payroll = payroll + pay
    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")

print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")

# Your answer: Before you run: Rosa's, Darnell's and Mei's weekly pay,
#     worked out by hand from the handbook rule.
# Your answer: The two bugs you found, each with its line and what you
#     changed it to.
# Your answer: Why can only Rosa's exactly-40 week catch one of the two
#     bugs?

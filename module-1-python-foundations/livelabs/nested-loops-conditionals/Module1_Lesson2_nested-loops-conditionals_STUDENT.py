#!/usr/bin/env python3
"""Day 2 code-along: Nested Loops & Conditionals. Run: python3 <file>"""

# ===== 1. Nested Loop, Live =====
# Print all six row and column pairs, starting at 0 0 and ending at 1 2.
# DISCUSS: If both loops used range(2), order: A: 1 0. B: 0 0. C: 1 1. D: 0 1.
# Your answer:
<<<<<<< HEAD

=======
>>>>>>> upstream/main
#
print('----- 1. Nested Loop, Live -----')
# TODO: write a nested loop that prints every (row, col) pair
# TODO: row goes through range(2), col through range(3)

# PREDICT before you run: Outer range(3), inner range(2): how many lines print?
# Your answer:
#
# DISCUSS: A classmate gets 3 lines instead of 6. What's the likely cause?
# Your answer:
#
<<<<<<< HEAD
#
for row in range(5):
    for col in range(4):
        print(row,col)
=======

>>>>>>> upstream/main

# ===== 2. Nested Conditional, Live =====
# Check the operation type first, then if the quantity is positive.
print('----- 2. Nested Conditional, Live -----')
# TODO: check operation first
# TODO: if it's "ADD", nest a second check that quantity is above 0
operation = "ADD"
quantity = 5

if operation == "ADD":
    if quantity > 0:
        print("valid add")
    else:
        print("invalid quantity")

# DISCUSS: If the inner quantity check never runs, what do you trace first?
# Your answer:
#


# ===== 3. Putting It Together: Loop + Nested Conditional =====
<<<<<<< HEAD
# Check each transaction line and print whether it is valid, has an invalid
# quantity, or is a remove.
print('----- 3. Putting It Together: Loop + Nested Conditional-----')
# TODO: loop over transactions; for each line, split it into
# operation and amount, then nest the ADD/quantity check
# from the nested-conditional step inside the loop
=======
# Check each line: print whether it is valid, a bad quantity, or a remove.
print('----- 3. Putting It Together: Loop + Nested Conditional -----')
# TODO: loop over transactions; split each into operation and amount
# TODO: put the nested ADD/quantity check inside the loop
>>>>>>> upstream/main
transactions = ["ADD 10", "REMOVE 3", "ADD -5"]

# PREDICT before you run: Which check flags "ADD -5" as invalid?
# Your answer:
#
<<<<<<< HEAD
#
for item in transactions:
    operation,quantity = item.split()
    quantity = int(quantity)
    if operation == "ADD":
        if quantity > 0:
            print(item, "- valid")
        else:
            print(item, "- invalid quantity")
    elif operation == "REMOVE":
        print(item, "- processing remove")
=======
>>>>>>> upstream/main

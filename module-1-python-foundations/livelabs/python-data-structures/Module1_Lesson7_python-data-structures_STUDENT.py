#!/usr/bin/env python3
"""Python Data Structures
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson7_python-data-structures_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson7_python-data-structures_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson7_python-data-structures_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Lists Let You Change Anything, Anytime =====
# Build a list of order IDs, then change it: add an order, rename the first
# one, and print the results.
print('----- 1. Lists Let You Change Anything, Anytime -----')
# TODO: create a list called pending_orders with "ORD-1001", "ORD-1002",
# and "ORD-1003"


# TODO: append "ORD-1004" to pending_orders


# TODO: use index assignment to change pending_orders[0] to "ORD-1001-R"
# (lists are mutable - this is allowed)


# TODO: print pending_orders, its length, and its last item (negative
# indexing)


# ===== 2. Once Locked In, a Tuple Can't Be Changed =====
# Store one log entry in a tuple, unpack it into three variables, then see what
# happens when you try to change it.
# This is supposed to raise TypeError: run it, read the traceback, then comment
# out the raising line so the rest of the file runs.
print("----- 2. Once Locked In, a Tuple Can't Be Changed -----")
# TODO: create a tuple called log_entry with a timestamp string,
# a level ("ERROR"), and a status code (500)


# TODO: unpack log_entry into timestamp, level, status


# TODO: print an f-string showing level, timestamp, and status


# TODO: try log_entry[0] = a new timestamp - what happens?
# (this SHOULD raise an error)


# ===== 3. Only Hashable Values Can Be Dict Keys =====
# Add and update products in a dictionary, then print every SKU with its stock
# count.
# Fill in the blank (____) below.
print('----- 3. Only Hashable Values Can Be Dict Keys -----')
product_stock = {"SKU-1001": 92, "SKU-2002": 34}
product_stock["SKU-3003"] = 8            # add a new product
product_stock["SKU-1001"] = 89           # update existing stock count

for sku, count in product_stock.____():
    print(f"{sku}: {count}")


# ===== 4. Sets Make Membership Checks Instant =====
# Track IDs in a set, see what happens when you add a duplicate, and check
# whether an ID is in the set.
print('----- 4. Sets Make Membership Checks Instant -----')
# TODO: create a set called seen_ids with 101, 102, and 103


# TODO: add 102 again - what happens? (sets have no duplicates)


# TODO: add a new id, 104


# TODO: print seen_ids, then check if 103 is in seen_ids
# (membership test)


# ===== 5. The Cost of Checking a List Adds Up =====
# This code times how long it takes to find one number in a list of 2 million
# numbers.
# Watch-only demo: the code is already here. Run it and read the output.
# NOTE: not auto-validated - Intentionally scans a 2,000,000-element list to
# demonstrate the real O(n) cost directly, not just describe it - not run by
# the automated validator to avoid slow/flaky timing checks on every build.
print('----- 5. The Cost of Checking a List Adds Up -----')
import time

# Run this and see the cost of a full scan in real time
user_id_list = list(range(2_000_000))

start = time.time()
found = 1_999_999 in user_id_list   # nearly a full scan
elapsed = time.time() - start

print(f"Found: {found}")
print(f"Took {elapsed:.4f} sec to check membership")

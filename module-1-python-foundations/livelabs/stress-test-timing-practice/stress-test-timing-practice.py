#!/usr/bin/env python3
"""Lab: Stress-Test Your Code: Timing & Efficiency
GitBook Quest 1.9: Lookups Matter

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 stress-test-timing-practice_STUDENT.py
    Or make it executable once:
        chmod +x stress-test-timing-practice_STUDENT.py
    and from then on run it directly:
        ./stress-test-timing-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it stress-test-timing-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Generate Batches of Your Own Day 15 Class at Three Sizes (10, 1,000, and 100,000) =====
# Use your own class from Day 15's lab - your batch should be full of YOUR
# objects, not a shared template's.
import random

class LibraryTool:
    def __init__(self, tool_name, quantity_available, requires_inspection):
        self.tool_name = tool_name
        self.quantity_available = quantity_available
        self.requires_inspection = requires_inspection

    def is_available(self):
        return self.quantity_available > 0

def make_batch(size):
    batch = []
    for i in range(size):
        batch.append(LibraryTool(f"Tool{i}",random.randint(0,5), random.choice([True, False])))
    return batch

small_batch = make_batch(10)
medium_batch = make_batch(1000)
large_batch = make_batch(100000)
print(len(small_batch), len(medium_batch), len(large_batch))

# TODO: Generate Batches of Your Own Day 15 Class at Three Sizes (10, 1,000, and 100,000)

# ===== Step 2: Write Two Searches Over That Batch - a Linear Scan and a Dict Lookup - and Confirm They Agree =====
# Same two functions Day 16's lecture wrote over SupplyItem - now over your
# own class and a much bigger batch.

# TODO: Write Two Searches Over That Batch - a Linear Scan and a Dict Lookup - and Confirm They Agree

def find_by_name_linear(batch, name):
    for x in batch:
        if x.tool_name == name:
            return x
    return None

def build_lookup(batch):
    return{x.tool_name: x for x in batch}

lookup = build_lookup(large_batch)
print(find_by_name_linear(large_batch, "Tool9999").tool_name)
print(lookup.get("Tool9999").tool_name)

# ===== Step 3: Put a Stopwatch on Both Searches at All Three Sizes and Record the Numbers =====
# Predict the pattern before running: which column should grow as size
# grows, and which should stay roughly flat?

import time

pairs = [(len(small_batch), small_batch),
         (len(medium_batch), medium_batch),
         (len(large_batch), large_batch)]
for size, batch in pairs:
    lookup = build_lookup(batch)
    start = time.perf_counter()
    find_by_name_linear(batch, "NotThere")
    linear_time = time.perf_counter() - start
    start = time.perf_counter()
    lookup.get("Not There")
    dict_time = time.perf_counter() - start
    print(size, linear_time, dict_time)

# TODO: Put a Stopwatch on Both Searches at All Three Sizes and Record the Numbers

# ===== Step 4: Answer Your Manager's Question in One Sentence, in Big-O Terms =====

# Your answer:
# As the batch size grew from 10 to 100000, the linear scan of O(n) slowed down from 0.000011s to 0.00163s. The dictionary lookup stayed flat
# in O(1) (constant time) at roughly 0.000002s across every size.

# ===== Step 5: Optional Stretch: Ask an AI How to Speed Up Your Linear Scan, Then Make It Prove It =====
# Stretch work only - beyond the core lab budget. Take it if you finish
# Steps 1-4 early. Same 'verify before trusting' habit from Module 0's
# AI-literacy lesson, now applied to a code-optimization claim instead of a
# chatbot fact claim.

# Your answer:
#
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Bring your numbers, not a summary of them. Specifically:
# - Your timings at each batch size, for both searches. Everyone tested a
#   different class on a different laptop, so the raw numbers won't match -
#   put yours up anyway.
# - Which column changed as the batch grew, and which one didn't. - The
#   batch size where the difference stopped being something you had to
#   squint at.
# - Whether anything surprised you. A linear scan that looked suspiciously
#   flat is worth raising - say what you found out was going on.
# - If you tried the AI stretch: what it claimed, and whether your own
#   timings actually backed it up. "It was wrong" is a good answer if you
#   can show the number that proves it.
#
# Be ready for "why does that happen?" - the timings are evidence, and the
# explanation is what's being assessed.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#

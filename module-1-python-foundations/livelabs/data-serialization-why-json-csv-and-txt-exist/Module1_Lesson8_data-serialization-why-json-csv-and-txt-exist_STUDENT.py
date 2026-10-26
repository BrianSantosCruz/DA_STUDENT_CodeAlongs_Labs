#!/usr/bin/env python3
"""Data Serialization — Why JSON, CSV, and TXT Exist
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson8_data-serialization-why-json-csv-and-txt-exist_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson8_data-serialization-why-json-csv-and-txt-exist_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson8_data-serialization-why-json-csv-and-txt-exist_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Writing to a File =====
# Write two restock reminders to a file called notes.txt, one per line.
print('----- 1. Writing to a File -----')
# TODO: use open("notes.txt", "w") with a `with` block to write two
# lines: "Restock staplers" and "Restock printer paper" (don't
# forget the "\n" at the end of each line)


# ===== 2. Reading It Back =====
# Open notes.txt again and print everything inside it.
print('----- 2. Reading It Back -----')
# TODO: use open("notes.txt") with a `with` block to open the file,
# then print its full contents with f.read()

# PREDICT before you run: If you opened notes.txt again in "w" mode and wrote
#                         one new line, like "Order toner\n", what would happen
#                         to the two Restock lines?
# Your answer:
#
#


# ===== 3. A CSV File Is Just Plain Text =====
# This code saves three rows of supply data as a CSV file, then reads the file
# back and prints it as plain text.
# Watch-only demo: the code is already here. Run it and read the output.
print('----- 3. A CSV File Is Just Plain Text -----')
csv_content = "name,count,department\nStapler,12,Office\nPaper,200,Office\n"

with open("supply.csv", "w") as f:
    f.write(csv_content)

with open("supply.csv") as f:
    print(f.read())


# ===== 4. Serializing a Record With json.dump() =====
# Save one supply record, stored as a dict, to a file called supply.json.
print('----- 4. Serializing a Record With json.dump() -----')
# TODO: import json
# TODO: create a dict called supply with name "Stapler", count 12,
# and department "Office"
# TODO: open "supply.json" in write mode and use json.dump() to
# save the dict to it


# ===== 5. Deserializing It Back With json.load() =====
# Load supply.json back into Python and check that it is a real dict again.
print('----- 5. Deserializing It Back With json.load() -----')
# TODO: import json
# TODO: open "supply.json" and use json.load() to read it back
# into a variable called supply
# TODO: print supply["name"], then print type(supply)

# PREDICT before you run: If you json.dump() a tuple, like ("Stapler", 12), and
#                         json.load() it back, what type comes back?
# Your answer:
#
#

#!/usr/bin/env python3
"""Lab: Solo Class Design Rep
GitBook Quest 1.8: Meet the Objects

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 solo-class-design-practice_STUDENT.py
    Or make it executable once:
        chmod +x solo-class-design-practice_STUDENT.py
    and from then on run it directly:
        ./solo-class-design-practice_STUDENT.py
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
    Commit this file (you may rename it solo-class-design-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS."""
import json

DATA_FILE = "utilitytools.json"

with open(DATA_FILE) as f:
    tools = json.load(f)

# ===== Step 1: Read the Stakeholder Need =====
# A new stakeholder need. Not the board-game or office-supply domain from
# lecture, and not one of the project's own 4 scenarios.

# Your answer:
# The volunteer coordinator needs to know what tools are used, if they are in need a safety check, and the amount in stock.
#

# ===== Step 2: Decide Your Attributes, Each With a Reason From the Scenario =====

# Your answer:
# tool_name, stock_available, and safety_check. tool_name because it provides the volunteer coordinator with the tool's name,
# stock_available provides them with the amount of a specific tool there is to be used, 
# and safety_check to verify if a specific tool needs a safety check before being used.

# ===== Step 3: Write __init__ and a Method, From Scratch =====
# There is no single correct design here. Your class name, your attribute
# names and your method can all differ from everyone else's and still be
# right. The test is whether each one traces back to the stakeholder
# paragraph.

class UtilityTools:
    def __init__(self, tool_name, stock_available, safety_check):
        self.tool_name = tool_name
        self.stock_available = stock_available
        self.safety_check = safety_check
    def show_status(self):
        if self.safety_check:
            status = "Needs a brief safety check."
        else:
            status = "Already had a safety check."
        print(f"Tool: {self.tool_name} | Free to borrow: {self.stock_available} | Status: {status}")

# TODO: Write __init__ and a Method, From Scratch

# ===== Step 4: Instantiate 2+ Objects, Confirm Independent Storage =====
# The same proof Day 13's lecture asked for, now on a class you designed
# yourself. Predict what each print() will show before you run it.

tool1 = UtilityTools("Adjustable Wrench", 11, False)
tool2 = UtilityTools("Staple Gun", 12, True)
# tool1.show_status()
# tool2.show_status()

tool1.stock_available = 0

tool1.show_status()
tool2.show_status()

# TODO: Instantiate 2+ Objects, Confirm Independent Storage

# ===== Step 5: Justify Your Design Choice in 2-3 Sentences =====

# Your answer:
# I decided to keep it minimal as the volunteer coordinator just asked to see three things: and these three things I had as the
# attributes tool_name, stock_available, and safety_check. The most important attribute here to determine was safety_check, as it could be
# either True or False, and in the context of what the volunteer coordinator needs, it is important for public safety. The instantiate portion
# successfully proves that both adjustable wrench and staple gun can have different outputs, as adjustable wrench had 0, but staple gun kept its 12.
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Come ready to show your class and defend it. Specifically:
# - The attribute list you chose, and for each one, the phrase in the
#   coordinator's request it came from. If you can't point at a phrase for
#   an attribute, say so - that's a real finding, not a failure.
# - One attribute you considered and rejected, and why. - Your method: what
#   question does it answer, and why would the coordinator reach for it
#   first?
# - Anything you got stuck on. Designing from a paragraph with nobody to
#   check against is genuinely hard, and naming where it was hard is worth
#   more to the room than a tidy answer.
#
# Expect to be asked "why that attribute and not another?" - there is no
# single right list here, so the reasoning IS the answer.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
# I struggled a bit with finding out how to properly format the outputs, before relying on the |. I also found it challenging to do the instantiate
# bit just because I did not fully understand what I was looking for, but once I understood I found the way to prove the differences.
#

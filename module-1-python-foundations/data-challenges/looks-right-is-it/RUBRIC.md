# Rubric: Looks Right. Is It?

Quest 1.10, Looks Right. Is It? · Days 18-19, graded together · submitted
once at the end of calendar Day 19.

Keep Day 18's work in the file when you add Day 19's. Both days are graded
from the same submission.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
3 skills x 4 points = **12 points at Meets**, more with any Exceeds earned.

Practice, not a gradebook entry. Read it before you start. Your instructor
grades from these same tables.

---

## Attention to Detail (`attention-to-detail`)

*A traceback tells you something broke. Nothing tells you a number is wrong. Can you tell anyway?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you say what makes exactly 40.00 hours the only detectable case for the boundary bug: `>=` and `>` agree on every other value in this file, so Rosa's row is the only one that can catch it. You also keep one hand-checkable case as a standing test, rather than checking once and moving on. |
| **Meets** | 4 | A hand-computed expected figure, taken from the CSV, is written before every Day 19 step and before you look at any output. All four steps land on values the CSV actually supports: Rosa's weekly hours, an average-per-day line for every employee in the file, one weekly hours figure per employee, a corrected payroll total, and an overtime headcount. Each one matches the figure you hand-computed first, for at least the employee you worked out on paper. Your Day 18 report has a line for all five employees in the file, and you checked that count against the CSV. You identify Rosa's exactly-40 week as the case that exposes the `>=` slip. A wrong prediction you then reconcile is worth more here than a right number you never predicted. Every dollar product in this file lands on an exact cent, so there is no rounding drift to chase. |
| **Approaching** | 2 | Your final numbers are right but your expectations are missing, vague, or visibly back-filled after the output. Or you find the overtime overpayment and miss that the headcount is wrong too, because the total started looking reasonable and you stopped. Reasonable is not correct. |
| **Below Expectations** | 1 | You accept the buggy payroll total, or the inflated weekly hours column, as correct because it ran without error. Or you record no expectations at all. |

## Control Flow & Loops (`control-flow-loops`)

*Where a line sits is part of what it does.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you refactor the duplicated `>=` check into one shared place instead of patching it twice. It sits in both `weekly_pay` and the `owed_overtime` counter. You also explain why a repeated condition is a bug waiting to happen, not just untidy. That is the quest's `Refactor` with a reason attached. |
| **Meets** | 4 | You locate Day 19's reset bug as a correctly spelled variable initialized in the wrong place: `total = 0` above the outer loop instead of inside it. You explain why that makes each employee's total a cumulative sum of everyone before them. You also say why the *first* employee's number comes out correct anyway, since nothing has accumulated above it yet. The last one comes out equal to the whole week's hours for the entire staff, and you say why. You also restructure overtime correctly as 40 hours at base plus the remainder at 1.5x, not the whole week at 1.5x. |
| **Approaching** | 2 | You find the reset bug by trial and error but cannot state the rule behind it. Or you fix overtime by subtracting the previous employee's total, which is a right answer from wrong logic and collapses as soon as `employee_ids` is reordered. |
| **Below Expectations** | 1 | You blame the CSV for the inflated last figure. The data is fine, and that number really is the whole week's hours for the entire staff. Or you never separate "which hours get 1.5x" from "whether that employee's week had overtime at all." |

## Problem Solving (`problem-solving`)

*Debugging is a sequence, not a hunch.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you describe a bug to your partner precisely enough (which line, which value, what it should be) that they make the edit without seeing your screen. That is the quest's Interview Arena bar, met early. |
| **Meets** | 4 | You walk expected behavior, trace, compare, locate, fix, verify in order for at least one bug on each day. Your `locate` step names a specific line, and your `verify` step re-runs a hand-checked case rather than re-reading your own fix. You tell the line the traceback reports apart from the bug's actual cause. On Day 18 the first crash ends in `add_hours`, but the bad value was picked one frame up, and the second crash names a division whose cause is a hand-typed staff list. You fix each one where the bad value was made, and you prove no employee went missing. |
| **Approaching** | 2 | You reach correct fixes but skip `verify`, or you verify by re-reading the fix rather than re-running a hand-checked case. Or you stop Day 18's second crash with `if days == 0: continue`: the run finishes and Samuel is silently missing from the report. A crash you hid is not a bug you fixed. |
| **Below Expectations** | 1 | Random edits until the output stops looking odd, and you cannot say which line was wrong or why. Or you hand in a right total with no written trace, when the method is what is graded here. Or you hand in an AI-written fix you cannot walk through line by line. A model will give you a payroll function that runs, is commented, and still overpays. |

## How this connects

- Day 18 practices reading a traceback that runs through more than one
  function, which the project's own `process_transactions` call chain will
  produce. The fix is graded on where you made it, not on the crash going
  away.
- It also preempts **common mistake #4**, only testing the happy path.
  Day 19's overtime bug leaves every employee under the 40-hour threshold
  perfectly correct, so a happy-path test passes and proves nothing.
- It is direct rehearsal for `PROJECT.md`'s Above and Beyond
  `debug_challenge.py`: 3 planted bugs, no template, on your own. That is
  objective 8's independent bar. This challenge is the same work with a
  partner, a hand-checkable file, and an instructor in the room. The
  project then hands you a 430-row file nobody can hand-check, and the
  sprint opens on calendar Day 20.
- This challenge does not reuse the quest's own Bug Hunts 1-3, so those
  checkpoints stay fresh for you to solve on their own.
- Quest 1.10 vocabulary assessed here: `Bug`, `Logic Error`, `Off-by-One
  Error`, `Scope Bug`, `Refactor`, `Expected Behavior`, `Actual Behavior`.
  (`Undefined Attribute` is named for recognition only. This challenge is
  function-and-loop shaped, so that term gets its rep in the quest's Bug
  Hunt 3 and in the project's class design.)

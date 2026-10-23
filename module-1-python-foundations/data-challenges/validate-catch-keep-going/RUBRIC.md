# Rubric: Validate, Catch, Keep Going

Quest 1.6 · Days 9-10 · submitted once at the end of Day 10. Keep Day 9's
validator in the file when you add Day 10's error handling. It is one file,
graded once, and Day 10's steps are built on top of that validator.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
3 skills x 4 points = **12 points at Meets**, more with any Exceeds earned.

Practice, not a gradebook entry. It shows you and your instructor whether you
own validation and error handling before the project asks for both unaided,
on a 430-row file. Your instructor grades from these same tables.

---

## Functions & Modular Programming (`functions-modular-programming`)

*Does your validator return something a program can use, or only something a
person can read?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you explain why the field-count check has to run before the five-name unpack, and you quote from your own run the unpacking `ValueError` that it prevents. Or you test the validator against a row shape that is not in the file at all. |
| **Meets** | 4 | `validate_request` returns a `(bool, reason)` pair and never prints it. Your caller unpacks both (`ok, reason = validate_request(row)`) and uses the reason in its report. The allowed statuses are defined once in a list, not as a chain of `!=`. Day 10's `days_open` rule lives in a separate second function rather than bolted inside the first one: two rules, two functions. You and your partner write the validator and the caller loop separately, sight unseen, so the return shape has to hold up as a contract. |
| **Approaching** | 2 | Validation works but prints instead of returning, so your step 2 loop has nothing left to print and your caller has no way to know the verdict. Or it returns only a bool with the reason printed from inside. Or the `try` is bolted into `validate_request`, so one function now does two unrelated jobs. |
| **Below Expectations** | 1 | No validation function at all, with the checks inline in the loop. Or the return value is unusable by the caller, with mixed types or nothing returned on a success path. |

## Attention to Detail (`attention-to-detail`)

*Do you notice when a number is quietly wrong?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you name a detection method that scales past reading every surviving row. Assert that `counted + skipped == len(rows)`, or print a per-reason tally, and say why eyeballing 15 rows will not work on 430. |
| **Meets** | 4 | Your submission opens with your own two or three sentences on what is actually in the file. Nobody tells you the column list, so reading the file yourself is the first part of the work. You notice that more rows passed Day 9's validation than should have, you name both of the rows that slipped through, and you say why your Day 9 validator cannot see them. Day 10's output then accounts for all 15 rows, with its counted and skipped totals adding up to the row count, and the average reconciles against the rows that survived validation. |
| **Approaching** | 2 | You reach the right Day 10 totals but never noticed the Day 9 gap yourself, or noticed it only after being told. Or your totals do not reconcile to 15 and you leave the difference unexplained. |
| **Below Expectations** | 1 | You accept Day 9's pass count as the answer. Or Day 10's report skips rows without counting them, so nothing adds up and nobody notices. |

## Problem Solving (`problem-solving`)

*Can you tell which tool a given bad row needs, and read a real traceback?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you explain the "Don't Catch Everything" principle from a real incident of your own, something a bare `except` hid from you, such as a typo it swallowed. Or you place the `try` boundary around only the risky conversion rather than the whole loop body, and explain the tradeoff. |
| **Meets** | 4 | You let step 3 crash on purpose, name the exception correctly (`ValueError`), and can say from your own output how many rows the report had already counted before it died. You sort every row you skipped into Validation or Error Handling with a reason. One of the two bad `days_open` values converts cleanly, so only an `if` can catch it. The other fails conversion, and your code catches it with `except ValueError`. Both sit in the same column, and your reasons say which gets which, and whether the other tool could have caught it. You use `except ValueError`, never a bare `except:`. |
| **Approaching** | 2 | Your code works but the Validation and Error Handling distinction is fuzzy. You treat a `days_open` value that converts cleanly as something `try` catches, when a value outside the allowed range is a business rule an `if` can check before any conversion runs. Or you cannot say why `except ValueError` beats a bare `except:` beyond "we were told to." Or a single `try` wraps the whole loop body: it skips the row, but it cannot say why it skipped, and it swallows the status bug too. |
| **Below Expectations** | 1 | You avoid the crash instead of reading it, by editing the CSV or skipping step 3. You do not get to edit the city's export, and the project's 430-row file will hold rows nobody warned you about. Or you write `except: pass` with no reason reported, or a `continue` that forgets to increment `skipped`, so the report silently loses rows. |

## How this connects

- This challenge heads off the project's common mistake #1, one long
  function doing everything. Step 1's return-not-print validator and step
  4's second function are that mistake refused twice, at 15-row stakes.
- It also heads off the project's common mistake #2, one malformed line
  crashing the whole script. Step 3 is exactly that mistake, run on purpose,
  with the damage visible: a few rows counted, the rest never reached, and
  one half-written report.
- It sets up Day 11's "Summarizing Data With a Second Function" LiveLab,
  which assumes the two-functions habit is already formed.
- Quest 1.6 vocabulary graded here: `Validation`, `Valid Input`,
  `Invalid Input`, `Malformed Input`, `Exception`, `Error Handling`, `try`,
  `except`. The quest's own checkpoints stay in the reading. This is the
  applied rep that makes your answers there mean something.

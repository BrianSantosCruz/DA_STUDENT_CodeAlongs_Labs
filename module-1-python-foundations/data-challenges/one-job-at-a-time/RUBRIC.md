# Rubric: One Job at a Time

Quest 1.7 · Days 11-12 · submitted once at the end of Day 12, with both days
of work still in the same file.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
3 skills x 4 points = **12 points at Meets**, more with any Exceeds earned.

Practice, not a gradebook entry. It shows you and your instructor whether you
can compose four separate functions into a working pipeline, well before the
project asks you to do it unaided. Your instructor grades from these same
tables.

---

## Functions & Modular Programming (`functions-modular-programming`)

*Does each of your functions do exactly one job?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you write a third summarizer nobody asked for, by item or by week, and it drops into the same `run_pipeline` with no edits anywhere else. Or you show why the field-count check has to run before the category check, by moving it last and showing that the short row D017 is then rejected for the wrong reason. |
| **Meets** | 4 | Four separate functions, one each for read, validate, summarize and export, plus a pipeline that calls them in order. Nothing inside `summarize_donations` checks whether a record is any good. Your usable-record count, your total pounds, and your category count all reconcile against the rows that survived validation, never against every row in the file. Day 12's swap is the real test: when the food bank wants a by-date breakdown instead, you write one new function and edit none of the other three, and you can say why. After your pipeline reports success, open `donation_summary.json` and read it, because a `json.dump` that wrote `{}` looks identical from the outside. |
| **Approaching** | 2 | Your functions exist but are entangled. The summarizer re-checks field counts with an `if len(parts) == 5` or a `try`/`except` of its own, which is the one long function doing everything rebuilt with extra steps, so a bad-record bug now has to be fixed in two places. Or the pipeline hardcodes which summarizer it calls, so Day 12's swap made you edit it. Output correct, separation only nominal. Write down how many of your other functions you had to edit: an honest "two, here is why" is worth more than a quiet "zero" that is not true. |
| **Below Expectations** | 1 | One long function doing all four jobs. Or Day 12's swap was done by rewriting the original summarizer instead of adding a second one. Or you edited `pantry_donations.csv` to make the bad rows go away, and those rows are the data. |

## Control Flow & Loops (`control-flow-loops`)

*Can you build an accumulator that holds more than one number?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you hand-check at least one category off the CSV yourself and record it in the file, including which category you checked and what you got. Do that before you trust your code's number. |
| **Meets** | 4 | One loop, one pass, with a dict as the accumulator. The `if key not in dict` guard is in place before you add into it. Per-category counts and pound totals all come out right. There is one entry for every category that appears in the valid rows, and none for a category that does not. The per-category pounds add back up to your overall total. The loop accumulates into both the dict and the running total without a second pass. |
| **Approaching** | 2 | You reach correct totals by looping the data more than once, with one pass per category or a pre-pass to collect the category names. Or you work around a `KeyError` with `dict.get` chains you cannot explain. |
| **Below Expectations** | 1 | Totals wrong and unreconciled, most often too high because you summarized `records` instead of `valid`. That counts the pounds from a rejected donation that has no category at all. |

## Documentation (`documentation`)

*Yes, your docstrings are graded here, not assumed. This is the topic where
they stop being a formality.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus at least one docstring states what the function refuses to be responsible for, such as "assumes every record is already valid" or "does no summarizing of its own". That one sentence is the whole argument for separate functions, and it is what makes a short function safe to be short. Or you wrote the docstring before the body and can point to where it changed your design. |
| **Meets** | 4 | Every function you write has a docstring, each one a single present-tense sentence naming that function's one job. None of them needs the word "and" twice. If you need "and" twice to describe a function, it is doing two jobs, and you have found your own bug before writing a line of it. Day 12's contract roll-call runs clean: you loop over your four functions, print each one's `__doc__` first line, and those four printed lines are in your submission. |
| **Approaching** | 2 | Docstrings are on some functions but not all. Or they are on all of them and clearly written afterward: multi-clause, describing the code line by line rather than naming a job. The roll-call runs but reads as narration. |
| **Below Expectations** | 1 | Docstrings missing, so the Day 12 roll-call raises `AttributeError: 'NoneType' object has no attribute 'splitlines'` and the program refuses to finish. Or you substituted comments for docstrings, so `__doc__` is `None` and the roll-call stops the same way. |

## How this connects

- This challenge heads off the project's common mistake #1, writing one long
  function that does everything instead of splitting reading, validation,
  and summarizing. It is that mistake's direct rehearsal, and Day 12's swap
  measures whether you avoided it. If you wrote one big function, you cannot
  do the swap without a rewrite. Better to learn that here than during the
  project sprint.
- It touches the project's common mistake #2, one malformed line crashing
  the script, only lightly, because Days 9-10 own that one. Here it shows up
  in Day 12's by-date breakdown, where a few dates come out holding just
  one donation each, because a row on that date was rejected. Think about
  what the coordinator should see: a quiet "1 donation," or a report that
  says a row was dropped. You do
  not have to build that today, but noticing it is the point.
- Your four functions map one-to-one onto the project's own named
  deliverables: `read_batch_file`, `validate_line`, `print_summary`, and
  `export_to_json`.
- Quest 1.7 vocabulary graded here: `Function`, `Parameter`,
  `Return Value`, `Accumulator`, `Validation`, `Single-Purpose Function`.
- This is the last plain-function challenge before Day 13 turns to objects,
  so it is also the module's integration rehearsal.

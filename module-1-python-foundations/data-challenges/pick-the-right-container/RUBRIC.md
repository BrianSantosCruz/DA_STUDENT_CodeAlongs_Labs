# Rubric: Pick the Right Container

Quests 1.3-1.5 (When the Crowd Grows · Pick the Right Container · Make It
Survive) · Days 6-8 · submitted once at the end of Day 8. Keep Day 6's and
Day 7's work in the file when you add Day 8's, because Day 8 cannot be
graded without Day 7's numbers sitting above it.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
4 skills x 4 points = **16 points at Meets**, more with any Exceeds earned.

Practice, not a gradebook entry. It shows you and your instructor which reps
you already own, before the project asks for them unaided. Your instructor
grades from these same tables.

---

## Algorithmic Complexity (Big-O) (`algorithmic-complexity-big-o`)

*Can you argue about cost with numbers instead of adjectives?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you project the parallel-lists count onto a log with 10 times the rows and explain why it does not simply multiply by 10, because the inner scan lengthens as the distinct-card list grows. Or you find a structural reason your count differs from another group's, such as a missing `break` in the inner loop, which raises the count while the totals stay correct. |
| **Meets** | 4 | Your file shows, side by side, the count you predicted and the count you measured for all five cases: the scan that finds the tap on the first row, the scan that finds it on the last row, the scan where the tap id is not in the file at all, the parallel-lists version, and the Dictionary version. Each of the five is reconcilable against the log by hand. Predictions stay exactly as you first wrote them, un-revised, because the gap between prediction and measurement is the assignment. You finish the sentence "as the Input Size grows..." correctly for both the scan and the nested pair loop, and you name the not-found case as a full-price worst case. Your pair-loop count accounts for the fact that the loop as written compares each row to itself. You count work rather than timing it: `time.time()` measures one run on one laptop, which is not what this is about. |
| **Approaching** | 2 | Your counts are there, but the argument stops at "the dictionary is faster" with no reference to growth. Or your reasoning is right but rests on stopwatch timings instead of counts. Or you treat the not-found case as cheap. |
| **Below Expectations** | 1 | No comparison counts at all. Or you conclude from 40 rows that the two approaches are equivalent because both finished instantly. |

## Control Flow & Loops (`control-flow-loops`)

*Can you write the same answer two ways and have both be right?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you break the parallel-lists version on purpose. Remove one entry from `card_ids` and not from `tap_counts`, then show what the counts become, with nothing raising an error anywhere. |
| **Meets** | 4 | Both of Day 2's versions run and agree on all four totals: distinct cards, the busiest card and its tap count, unique stations, and cards that tapped more than once. Distinct cards and cards that tapped more than once are two different questions, and your file names the cards that account for any gap between those two totals. A Set holds the stations rather than an `if not in` scan, so `stations.add()` runs once per row while the Set still holds only the distinct stations: uniqueness is a property of the container, not something your loop checks. The parallel-lists version actually works and is not a strawman you half-wrote. The two versions agreeing is the only check you have, so if they disagree, one of them is wrong and reconciling them is part of the work, not something to leave for the shareout. Day 3 prints `round trip identical: True`, and prints the busiest card's own tap count read back out of the reloaded file. |
| **Approaching** | 2 | One version works and the other is sketched or broken. Or you replace the nested inner loop with `.index()`, so no comparison count exists; the method does not do less work, it does it where you cannot see it. Or `tap_summary.json` is written and never reloaded. |
| **Below Expectations** | 1 | Only the dictionary version exists, so there is nothing to compare. Or the totals are wrong and left unreconciled. |

## AI Output Validation (`ai-output-validation`)

*Can you tell a correct explanation from a confident one?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you document a specific AI answer that was wrong, incomplete, or right for the wrong reason, and say exactly what was off about it. |
| **Meets** | 4 | Day 3's `TypeError` sits in your file unfixed first, with your own words on which of the five keys caused it and why JSON has no Set type. Those words come before any AI explanation appears. You convert the Set rather than deleting it. If you asked AI about performance on Day 2, your file shows how you checked that claim against your own two measured comparison counts instead of accepting it. |
| **Approaching** | 2 | You fix the error correctly, but the explanation is pasted or paraphrased with no sign you read the real message first. Or you quote an AI claim approvingly with no verification step. |
| **Below Expectations** | 1 | No error ever appears in the file, because an AI answer pre-fixed it. Or you delete the `stations` key to make the error go away. Or an unverified AI performance claim stands as your whole argument. |

## Data Structures Selection (`data-structures-selection`)

*Can you pick a container for the job it has to do, and say why?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you name when your choice stops paying off, such as a job that looks up one card once, where building the Dictionary costs more than the single scan it replaces. Or you explain what choosing a Set cost you on Day 3, at the point the summary had to leave Python and come back. |
| **Meets** | 4 | For each container in your Day 2 file, you name the job it does and how that job finds what it needs. The Dictionary goes straight to a card by its Key. The Set keeps only distinct stations with no check in your loop. The parallel lists have to be scanned to find a card. Your "As the Input Size grows..." bullets argue for the Dictionary with your own two counts, not a general rule. You say what a list would have cost you for `stations`, and name the check it would need on every row. |
| **Approaching** | 2 | You picked workable containers, but your only reason is "it is faster" or "it is better", with nothing about how each job finds what it needs. Or you argue for the Dictionary and say nothing about the Set. |
| **Below Expectations** | 1 | No reason is given for any container choice. Or `stations` is a list with an `if not in` check, and you never say what that container now makes your loop do. |

## How this connects

- This challenge rehearses the project's common mistake #3, holding item
  data in loose parallel lists instead of using one real structure. Day 2 is
  the direct rehearsal, which is why you build and count the slower
  parallel-lists version first. The project's `Item` class is the same
  argument one level up: a structure that holds related fields together so
  they cannot drift apart. The quieter half of that mistake is not slowness
  but silent desynchronization, which the Exceeds bar above asks you to
  demonstrate on purpose.
- It feeds the project's `REFLECTION.md` Big-O question, which asks you to
  compare a linear scan with a dictionary lookup in your own `find_item`.
  Days 1-2 here are that same comparison at 40-row scale.
- It feeds the project's `export_to_json` requirement. Day 3's reload and
  compare is the verification step most people skip on their own output.
- Quest vocabulary graded here: `Input Size`, `Big-O`, `Linear Scan`,
  `Lookup` (Quest 1.3); `Data Structure`, `Dictionary`, `Set` (Quest 1.4);
  `Serialization` (Quest 1.5). You will use `Deserialization`, `Format` and
  `JSON` throughout Day 3, but they are not scored separately.

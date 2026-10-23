# Rubric: Lookups Matter

Quest 1.9, Lookups Matter · calendar Day 16, a single day · submitted once
at the end of calendar Day 16.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
4 skills x 4 points = **16 points at Meets**, more with any Exceeds earned.

Practice, not a gradebook entry. Read it before you start. Your instructor
grades from these same tables.

---

## Algorithmic Complexity, Big-O (`algorithmic-complexity-big-o`)

*Can you show, from counts you produced yourself, what grows with the data and what does not?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you explain why the pay-off swipe moves. A morning of front-of-file swipes pushes it later, and a single non-member pulls it earlier. You can describe a morning where building the dict is never worth it. |
| **Meets** | 4 | All four steps run. Your output shows a comparison count for every swipe, a whole-morning linear total, the dict's build cost, both running totals, and the swipe where the dict pulled ahead. Each number is reconcilable against the files: a member's count is their ID minus 1000, and a non-member costs `len(members)`. Your verdict names `O(n)` for each linear lookup and for the dict build, and `O(1) Average-Case` for each dict lookup, and quotes at least one of your own counts. |
| **Approaching** | 2 | Your counts are right but your verdict restates the labels without quoting a count. Or you leave the build cost out of the dict total, so the dict "wins" from swipe 1. |
| **Below Expectations** | 1 | The counter sits after the `if`, so every member reports the same count, and you never notice. Or there is no verdict. Or the verdict says only "the dict was faster." |

## Critical Thinking (`critical-thinking`)

*Did you reason about the numbers before the output told you?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you separate the average case from the worst case. A random member costs roughly `n/2`, and you explain why Big-O quotes the worst case instead. |
| **Meets** | 4 | Your predictions sit under the `# Your answer:` lines, written before you ran each step: the `M1150` count, the first three swipes and their sum, the non-member cost, and the pay-off swipe. A wrong prediction you then explain is worth more than a right one you never committed to. You explain that a non-member forces a comparison against every row, because nothing lets the loop stop early. |
| **Approaching** | 2 | Predictions are present but vague, or visibly written after the fact. Or you know the non-member is the worst case without saying why. |
| **Below Expectations** | 1 | No predictions. Or you still call the non-member the fast case after seeing its count. |

## AI Output Validation (`ai-output-validation`)

*You hold your own totals. Did you use them? You are graded on the checking, never on what the claim happened to say.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you explain why no single multiplier can be right. The gap is about 4x for a cheap swipe, 312x for a non-member, and under 9x for the whole morning once the build is counted. It depends on `Input Size`, on where the match sits, and on how many lookups share the build. |
| **Meets** | 4 | The AI's claim is pasted into `ai_claim` word for word. You hold it against all three of your comparisons and say which it matched and which it missed. You asked whether it counted the build cost, and you report the answer. Your verdict says plainly which happened: the claim was overstated, understated, or gave no number to check. |
| **Approaching** | 2 | The claim is pasted with a vague "that seems right" and no count quoted. Or you tidied up the claim, so what the AI actually said can no longer be checked. |
| **Below Expectations** | 1 | You paste the claim and never evaluate it. Or you consult no AI, leave the placeholder untouched, and write no verdict about it. |

## Data Structures Selection (`data-structures-selection`)

*Can you say why the door should use a dict, and when it should not?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you name what the choice of key costs. `member_id` is unique, so every member gets an entry. A key that repeats, such as a name in a real directory, would silently overwrite records, and the door would turn away a real member. |
| **Meets** | 4 | Step 3 builds `members_by_id` keyed on `member_id`, and `len(members_by_id)` matches `len(members)`. Under step 3's `# Your answer:`, you name the door's job, asking "is this ID a member?" on every swipe, and explain why a dict fits it: each lookup goes straight to the key instead of scanning. You back the choice with your own race, quoting the swipe where the dict pulled ahead. You describe a morning where the plain list is the better choice, such as one swipe near the front of the file. |
| **Approaching** | 2 | You built the dict and it works, but your reason is only "it is faster", with nothing about the job it does or your own counts. Or you argue for the dict and never say when the list would win. |
| **Below Expectations** | 1 | No reason is given for the container. Or the dict is keyed on something other than the ID the door asks about, and you never notice what that does to the lookups. |

## How this connects

- This preempts **project common mistake #4**, only testing the happy path.
  A non-member swipe is a REMOVE for an item that was never added, and it
  is the case that forces every comparison.
- It rehearses the project's `REFLECTION.md`: a Big-O comparison tied to
  your own `find_item`, and an AI-assisted answer **with a real
  verification step**. Step 4 is that verification step at 30-minute scale.
- One project warning worth taking with you: keying the dict on `name`
  runs fine here, because every name in this file is unique. A key that is
  not unique silently drops records, and the project's data is not as
  forgiving.
- Quest 1.9 vocabulary assessed here: `Linear Search`, `Dictionary Lookup`,
  `Input Size`, `O(n)`, `O(1) Average-Case`, `Scale`, `Complexity`.
- The stress-test session that closes Quest 1.9
  (`livelabs/stress-test-timing-practice/`) takes the same two searches to a
  stopwatch. Nothing here grades timing, so you do not need `time`, and
  everyone's counts should come out the same.

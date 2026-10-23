# Rubric: Meet the Objects

Quest 1.8, Meet the Objects · Days 13-14, graded together · submitted once
at the end of calendar Day 14.

Keep Day 13's work in the file when you add Day 14's. Both days are graded
from the same submission.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
3 skills x 4 points = **12 points at Meets**, more with any Exceeds earned.

Practice, not a gradebook entry. Read it before you start. Your instructor
grades from these same tables.

---

## Object-Oriented Programming (`object-oriented-programming`)

*Can you build a class that keeps a thing's facts attached to that thing? There is no single correct attribute list, so you are graded on fit with the dispatcher's stated need, never on matching a particular field list.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you say what breaks about the two-list version when a station is *added* rather than removed. Or you defend a deliberate omission (for example dropping `station_id`) as carefully as you defend an attribute you kept. |
| **Meets** | 4 | You reproduce Day 1's parallel-list bug and name the specific stations that reported a count that was never their own. You write two or three sentences about the data file from opening it: what one row represents, which fields are numbers versus text, and anything already wrong or missing. Your `Station` class defines `__init__` with a justifying phrase from the dispatcher's request written next to every attribute you kept. One real method reads its own object's attributes through `self`. Your independence check uses two objects that gave the *same* answer before you changed one of them and different answers after. |
| **Approaching** | 2 | Your class runs and instantiates, but you added every field in the file and decided nothing. The `# TODO:` names only the three attributes `needs_restock()` and `__str__` need, on purpose: choosing the rest is the work. Or your list looks plausible but has no phrase written beside any entry: a different list that you defend scores higher than a tidy one you do not. Or your independence check uses two objects that already disagreed, so it demonstrates nothing. Or you call Day 1's output "wrong" without naming which stations. |
| **Below Expectations** | 1 | No class defined, or attributes set outside `__init__` only. Or you accept Day 1's output as correct because nothing raised. Or you paste an AI-written class you cannot justify attribute by attribute. Nobody can tell you the right answer here, which means nobody can check a borrowed one for you either. |

## Functions & Modular Programming (`functions-modular-programming`)

*Does behavior live with the data it operates on, and do your two display methods serve their two different readers?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you show the full map of which method Python reaches for when, with a written prediction before each one: a single `print()`, a list, `repr()`, an f-string. You state the rule that produces each. You predict the default display's *shape*, not a value: `<__main__.Station object at 0x...>`, meaning angle brackets, class name, `object at`, a hex number. The hex address differs on every run, so an address unlike your partner's is not an error. |
| **Meets** | 4 | Your method reaches for `self.bikes_available` and `self.capacity` instead of having them handed in, and takes no parameter it does not need. You can name which station `self` refers to on a given line. By the end of Day 2 both `__str__` and `__repr__` are defined, and you can say what each one is *for* and who reads it, not just that both exist. |
| **Approaching** | 2 | Your method works but takes values as parameters it could have read from `self`. Or both display methods are present and you describe them interchangeably ("both just print it nicely"). |
| **Below Expectations** | 1 | Logic left at module level instead of inside a method. Or only one display method is defined and you never test the list case. |

## Collaboration (`collaboration`)

*Did two people actually think, or did one person type? This skill is introduced in this module, and the Data Challenge is the pair-work block where it is taught.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus your file names which partner's attribute list you adopted, why, and what the rejected list would have been better at. |
| **Meets** | 4 | You each draft your attribute list privately before comparing. You swap driver between the two days. Your file records a moment where your lists differed and what each of you argued. On Day 2 the partner who is not typing owns the predictions and shares each one with the driver before anything runs. Both of you can justify any attribute when asked cold. |
| **Approaching** | 2 | You worked together but drafted the attribute list jointly, so only one person's design reasoning is represented. Or you never swapped driver. Or Day 2's predictions were written after the prints had already run. |
| **Below Expectations** | 1 | One of you designed and typed, and the other submitted a copy and cannot defend an attribute choice. |

## How this connects

- This preempts **project common mistake #3**: holding item data in loose
  parallel lists instead of using the class consistently. Day 1's first
  step is that mistake built on purpose, on data where you can name the
  damage station by station.
- It also preempts **common mistake #4**, only testing the happy path, in
  miniature. Day 2's `__str__`-only step passes the one test you naturally
  run and fails the one you skip.
- The project grades class design the same way (`PROJECT.md`, "Note on
  grading"), because everyone picks their own scenario. Nobody can hand you
  the correct attribute list, yours or an AI's.
- Day 15's solo class-design rep
  (`livelabs/solo-class-design-practice`) gives you neither the worked
  signature nor a partner. The habit of justifying every attribute is the
  part that carries over. The domain there is new.
- Quest 1.8 vocabulary assessed here: `Class`, `Object`, `Instance`,
  `Attribute`, `Method`, `self`, `__init__`, `__str__`, `__repr__`.
  (`Object-Oriented Programming (OOP)` is framed rather than assessed.)

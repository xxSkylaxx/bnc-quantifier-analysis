# Research Notes

This document records the exploratory process of identifying quantifiers, developing semantic categories, and refining corpus queries for the comparison of two syntactic structures:

- **Structure A:** `a/an + ADJ + QUANTIFIER + of + NOUN`
- **Structure B:** `a/an + QUANTIFIER + of + ADJ + NOUN`

The notes include preliminary corpus queries, quantifier lists, classification decisions, and initial observations.

---

## 1. Initial Corpus Query

### 1.1 First Attempt

The initial query compared the following two patterns:

- **Structure A:** `a hot cup of tea`
- **Structure B:** `a cup of hot tea`

Using the following POS-tag patterns:

```text
Structure A: _AT0 _AJ0 _NN1 of _NN1
Structure B: _AT0 _NN1 of _AJ0 _NN1
```

**Combined results:**

- Total hits: 117,597
- Different texts: 3,682

| Structure | Hits | Different texts | Proportion |
|---|---:|---:|---:|
| A: a hot cup of tea | 60,199 | 3,536 | 51% |
| B: a cup of hot tea | 57,398 | 3,328 | 49% |

### 1.2 Initial Query Limitations

The initial query did not successfully exclude certain expressions that were not relevant to the intended quantifier construction.

Examples:

- The Office of Fair Trading
- The Confederation of British Industry
- The European Court of Justice
- a clean bill of health
- a lot of hard work

**Question for further investigation:** Could quantifiers be queried directly to improve the accuracy of the search?

---

## 2. Identifying Quantifiers

### 2.1 Definition of Quantifiers

The following definitions were considered when identifying candidate quantifiers:

> A quantifier is a word or phrase used to talk about quantities, amounts or degree. They can be used with a noun (as a determiner) or without a noun (as a pronoun).

— Cambridge Dictionary

> A quantifier is a word or short phrase which indicates the amount or quantity of an object that is referred to by the noun phrase which the quantifier modifies.

— Nel, J., & Southwood, F. (2016)

### 2.2 General Quantifier List (BC)

The initial list included:

- all
- no
- some
- any
- more
- most
- a lot of
- lots of
- enough
- less
- plenty of
- heaps of
- loads of
- tons of
- many
- several
- each
- both
- either
- neither
- few
- a few
- fewer
- a couple of
- hundreds of
- thousands of
- much
- a bit of
- a little
- a great deal of
- a good deal of

### 2.3 Container and Packaging Quantifiers

The following expressions were initially collected:

- a bottle of
- a carton of
- a can of
- a jar of
- a box of
- a pack of
- a packet of
- a tube of
- a bag of
- a cup of
- a glass of
- a bowl of
- a tablespoon of
- a teaspoon of
- a pinch of
- a handful of
- a spoonful of
- a slice of
- a piece of
- a loaf of
- a bar of
- a head of
- a clove of
- a sprig of
- a bunch of
- a roll of
- a block of
- a cube of
- a drop of
- a grain of
- a flake of
- a speck of
- a blade of
- a puff of
- a ray of
- a liter of
- a milliliter of
- a kilogram of
- a gram of
- a pound of
- an ounce of
- a gallon of
- a quart of
- a meter of
- a yard of
- an inch of
- an item of
- a stroke of
- a fit of
- a glint of
- an hour of
- a day of

### 2.4 Animal Group Quantifiers

The initial collection also included:

- a murder of
- a pack of
- a pride of
- a tower of
- a shrewdness of
- a galaxy of
- a mischief of
- a huddle of
- a flock of
- a herd of
- a school of
- a pod of
- a troop of
- a bed of
- a covey of
- a litter of

---

## 3. Quantifier Classification

To organize the collected quantifiers, 13 semantic categories were established.

### 3.1 Initial Comprehensive List

| No. | Semantic Category | Quantifiers |
|---|---|---|
| 1 | Container measures | bottle, carton, can, jar, box, pack, packet, tube, bag, cup, glass, bowl |
| 2 | Portion measures | tablespoon, teaspoon, pinch, handful, spoonful, slice, piece, loaf, bar, head, clove, sprig, bunch, roll, block, cube |
| 3 | Small / discrete measures | drop, grain, flake, speck, blade, puff, ray |
| 4 | Weight measures | kilogram, gram, pound, ounce |
| 5 | Volume measures | liter, litre, milliliter, millilitre, gallon, quart |
| 6 | Length measures | meter, metre, yard, inch |
| 7 | Other countable / temporal measures | item, stroke, fit, glint |
| 8 | Numerical / counting measures | pair, couple, dozen, score, brace, set, series, batch, collection, group, cluster, string |
| 9 | Portion / quantity measures | portion, serving, dose, ration, mouthful, sip, gulp, chunk, lump, slab, strip, sheet, bundle, heap, pile, stack, load |
| 10 | Spatial measures | stretch, length, width, depth, area, patch, expanse, span |
| 11 | Temporal measures | hour, day, second, minute, week, fortnight, month, year, decade, century, period, spell, moment, interval, duration, lifetime, season |
| 12 | Abstract quantity measures | amount, quantity, measure, degree, level, extent, proportion, fraction, percentage, volume, mass, wealth |
| 13 | Animal group quantifiers | murder, pack, pride, tower, shrewdness, galaxy, mischief, huddle, flock, herd, school, pod, troop, bed, covey, litter, swarm, gaggle, colony, shoal, brood, parliament, flight, army, cloud, congregation, clutch, kennel, nest, team, cast, cete |

### 3.2 Reducing the Quantifier List

Since the BNC interface could not process queries that were too long, the initial list had to be reduced.

**Second version:**

| No. | Semantic Category | Quantifiers |
|---|---|---|
| 1 | Container measures | bottle, can, jar, box, pack, packet, bag, cup, glass, bowl |
| 2 | Portion measures | tablespoon, teaspoon, handful, spoonful, slice, piece, loaf, bar, bunch, roll |
| 3 | Small / discrete measures | drop, grain |
| 4 | Weight measures | kilogram, gram, pound, ounce |
| 5 | Volume measures | liter, litre, milliliter, millilitre, gallon |
| 6 | Length measures | meter, metre, yard, inch |
| 7 | Other countable measures | item, stroke, fit |
| 8 | Numerical / counting measures | pair, couple, dozen, set, series, batch, group, cluster, string |
| 9 | Portion / quantity measures | portion, serving, dose, mouthful, chunk, lump, strip, sheet, pile, stack, load |
| 10 | Spatial measures | stretch, length, area, patch, span |
| 11 | Temporal measures | hour, day, second, minute, week, month, year, period, moment, season |
| 12 | Abstract quantity measures | amount, quantity, measure, degree, level, extent, proportion, percentage, volume, mass, wealth |
| 13 | Animal group quantifiers | pack, pride, flock, herd, school, pod, troop, litter, swarm, gaggle, colony, shoal, brood, flight |

### 3.3 Final Reduced Quantifier List

The second list was still too long for the BNC interface. Therefore, a further reduction was made.

The following list was used as the final working list for the corpus queries:

| No. | Semantic Category | Quantifiers |
|---|---|---|
| 1 | Container measures | bottle, can, box, pack, bag, cup, glass |
| 2 | Portion measures | spoonful, handful, slice, piece, loaf, bunch |
| 3 | Small / discrete measures | drop, grain |
| 4 | Weight measures | kilogram, gram, pound, ounce |
| 5 | Volume measures | liter, litre, gallon |
| 6 | Length measures | meter, metre, inch |
| 7 | Other countable measures | item |
| 8 | Numerical / counting measures | pair, couple, dozen, group, set |
| 9 | Portion / quantity measures | portion, serving, chunk, pile, load |
| 10 | Spatial measures | stretch, length, area |
| 11 | Temporal measures | hour, day, week, month, year, period |
| 12 | Abstract quantity measures | amount, quantity, degree, level |
| 13 | Animal group quantifiers | flock, herd, swarm, school |

---

## 4. Refined Corpus Query

### 4.1 Second Attempt

Instead of searching for a single noun (`NN1`), the query was modified to search for nouns from the selected quantifier list.

The revised POS-tag patterns were:

```text
Structure A: _AT0 _AJ0 [NN1 list] of _NN1
Structure B: _AT0 [NN1 list] of _AJ0 _NN1
```

### 4.2 Results

**Combined results:**

- Total hits: 11,506
- Different texts: 2,680

| Structure | Hits | Different texts | Proportion |
|---|---:|---:|---:|
| A | 7,835 | 2,394 | 68.09% |
| B | 3,671 | 1,660 | 31.91% |

Compared with the first attempt, the revised query produced a more pronounced difference between the two structures.

---

## 5. Preliminary Observations

Based on the distribution of the 13 semantic categories, the following patterns were observed:

### 5.1 Categories with A > B

Structure A occurred more frequently than Structure B in **9 out of 13 categories**:

- Abstract quantity measures
- Animal group quantifiers
- Length measures
- Other countable measures (item)
- Portion measures
- Portion / quantity measures
- Small / discrete measures
- Spatial measures
- Temporal measures

### 5.2 Categories with B > A

Structure B occurred more frequently than Structure A in **4 out of 13 categories**:

- Container measures
- Numerical / counting measures
- Volume measures
- Weight measures

### 5.3 Initial Interpretation

Although Structure A appeared to be more frequent overall, the distribution suggests that structural preferences may vary across semantic categories.

This observation raises the possibility that the semantic properties of quantifiers may be associated with the choice between the two structures.

Further analysis is needed to investigate the relationship between quantifier categories and structural preferences.

---

*Note: These observations represent preliminary findings from the exploratory corpus analysis and should not be treated as final conclusions.*

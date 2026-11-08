# bnc-quantifier-analysis

## Overview

This project investigates the distribution of quantifiers in two syntactic structures using the **British National Corpus (BNC)**.

The study focuses on comparing the following structures:

- **Structure A:** *a + adjective + quantifier + of + noun* (e.g., *a hot cup of tea*)
- **Structure B:** *a + quantifier + of + adjective + noun* (e.g., *a cup of hot tea*)

The research aims to compare the overall frequencies of the two structures and examine how different semantic categories of quantifiers are distributed across them.

## Research Methods

This study selects **53 quantifiers** and classifies them into **13 semantic categories** for analysis.

The selection is intended to reduce irrelevant search results, such as proper nouns (e.g., *the Office of Fair Trading*) and idiomatic expressions (e.g., *a lot of hard work*).

The following BNC query patterns are used to retrieve the two structures:

**Structure A**
```text
_AT0 _AJ0 [NN1 list] of _NN1
```

**Structure B**
```text
_AT0 [NN1 list] of _AJ0 _NN1
```

**Combined Query**
```text
(_AT0 _AJ0 [NN1 list] of _NN1 |
 _AT0 [NN1 list] of _AJ0 _NN1)
```

The analysis includes:

1. Comparing the relative frequencies of Structures A and B.
2. Examining the frequency distributions of the 13 semantic categories and individual quantifiers across the two structures.
3. Conducting a chi-square test to determine whether the distribution of the two structures differs significantly across semantic categories.

## Repository Structure

```text
quantifier-analysis/
│
├── data/
│   ├── category_comparison.txt
│   ├── quantifier_frequency.csv
│   ├── frequency_list_structure_a.txt
│   ├── frequency_list_structure_b.txt
│   ├── structure_a_parsed.csv
│   └── structure_b_parsed.csv
│
├── scripts/
│   └── frequency_analysis.py
│
└── README.md
```

### Data

Contains the original frequency lists retrieved from the BNC, processed CSV datasets, and category comparison results.

### Scripts

Contains Python scripts for processing frequency data and conducting quantitative analysis.

## Tools

- British National Corpus (BNC)
- Python
- pandas

## Reference

Cambridge Dictionary. (n.d.). Quantifiers. https://dictionary.cambridge.org/grammar/british-grammar/quantifiers


# bnc-quantifier-analysis

## Overview

This project investigates the distribution and usage patterns of quantifier structures in the **British National Corpus (BNC)**. It focuses on comparing two syntactic structures and examining their frequency distributions across different categories.

## Repository Structure

```text
quantifier-analysis/
│
├── data/
│   ├── category_comparison.txt
│   ├── quantifier_frequency.csv
│   ├── frequency_list structure A.txt
│   ├── frequency_list structure_B.txt
│   ├── structure_A_parsed.csv
│   └── structure_B_parsed.csv
│
├── scripts/
│   └── frequency_analysis.py
│
└── README.md
```

### `data/`

Contains the datasets and frequency analysis results used in this project.

| File | Description |
|---|---|
| `category_comparison.txt` | Comparison of the distribution of quantifier categories |
| `quantifier_frequency.csv` | Frequency data of identified quantifiers |
| `frequency_list structure A.txt` | Original frequency list for Structure A |
| `frequency_list structure_B.txt` | Original frequency list for Structure B |
| `structure_A_parsed.csv` | Parsed and structured frequency data for Structure A |
| `structure_B_parsed.csv` | Parsed and structured frequency data for Structure B |

### `scripts/`

Contains Python scripts used for data processing and analysis.

- `frequency_analysis.py`: Processes frequency data and performs quantitative comparisons between the two structures.

## Methods

The analysis involves:

1. **Data collection:** Retrieving instances of the two target structures from the BNC.
2. **Data processing:** Parsing frequency lists and organizing lexical items into structured datasets.
3. **Categorization:** Identifying and classifying quantifiers into semantic or functional categories.
4. **Frequency analysis:** Comparing the distributions and normalized frequencies of the two structures.
5. **Statistical analysis:** Examining differences in category distributions using statistical methods, including the chi-square test.

## Tools

- Python
- pandas
- BNC (British National Corpus)

## Research Focus

The project aims to explore how quantifier categories are distributed across two syntactic structures and whether the observed differences suggest distinct usage patterns.



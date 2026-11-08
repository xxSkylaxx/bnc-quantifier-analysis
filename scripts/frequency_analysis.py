
import re
import pandas as pd
from pathlib import Path

# =========================================
# 1. Quantifier categories
# =========================================

categories = {
    "Container": [
        "bottle", "can", "box", "pack", "bag", "cup", "glass"
    ],
    "Portion": [
        "spoonful", "handful", "slice", "piece",
        "loaf", "bunch"
    ],
    "Small / discrete": [
        "drop", "grain"
    ],
    "Weight": [
        "kilogram", "gram", "pound", "ounce"
    ],
    "Volume": [
        "liter", "litre", "gallon"
    ],
    "Length": [
        "meter", "metre", "inch"
    ],
    "Other countable": [
        "item"
    ],
    "Numerical / counting": [
        "pair", "couple", "dozen", "group", "set"
    ],
    "Portion / quantity": [
        "portion", "serving", "chunk", "pile", "load"
    ],
    "Spatial": [
        "stretch", "length", "area"
    ],
    "Temporal": [
        "hour", "day", "week", "month",
        "year", "period"
    ],
    "Abstract quantity": [
        "amount", "quantity", "degree", "level"
    ],
    "Animal group": [
        "flock", "herd", "swarm", "school"
    ]
}


# =========================================
# 2. Build quantifier lookup
# =========================================

quantifier_lookup = {}

for category, words in categories.items():

    for word in words:

        if word in quantifier_lookup:
            print(
                f"WARNING: Overlapping quantifier: {word} "
                f"(keeping {quantifier_lookup[word]}, "
                f"ignoring {category})"
            )

        else:
            quantifier_lookup[word] = category


# =========================================
# 3. Read BNC frequency breakdown TXT
# =========================================

def read_bnc_txt(file_path):

    records = []

    skipped_no_match = []
    skipped_no_quantifier = []
    skipped_ambiguous = []

    text = Path(file_path).read_text(
        encoding="utf-8",
        errors="replace"
    )

    for line_number, line in enumerate(
        text.splitlines(), start=1
    ):

        # Match:
        # rank + lexical item + frequency + percentage

        match = re.match(
            r"^\s*(\d+)\s+(.+?)\s+(\d+)\s+([\d.]+%)\s*$",
            line
        )

        if not match:
            skipped_no_match.append({
                "Line": line_number,
                "Content": line
            })
            continue

        rank = int(match.group(1))

        lexical_item = match.group(2).strip()

        frequency = int(match.group(3))

        percentage = float(
            match.group(4).replace("%", "")
        )

        words = lexical_item.lower().split()

        # Find "of"

        if "of" not in words:
            skipped_no_quantifier.append({
                "Line": line_number,
                "Lexical item": lexical_item,
                "Frequency": frequency,
                "Reason": "No 'of' found"
            })
            continue

        of_index = words.index("of")

        # Search for quantifiers before "of"
        # No determiner restriction

        candidates = [
            word
            for word in words[:of_index]
            if word in quantifier_lookup
        ]

        # Remove duplicate candidates while preserving order

        candidates = list(dict.fromkeys(candidates))

        if len(candidates) == 0:

            skipped_no_quantifier.append({
                "Line": line_number,
                "Lexical item": lexical_item,
                "Frequency": frequency,
                "Reason": "No recognized quantifier before 'of'"
            })

            continue

        if len(candidates) > 1:

            skipped_ambiguous.append({
                "Line": line_number,
                "Lexical item": lexical_item,
                "Frequency": frequency,
                "Candidates": ", ".join(candidates)
            })

            continue

        quantifier = candidates[0]

        records.append({
            "Rank": rank,
            "Lexical item": lexical_item,
            "Quantifier": quantifier,
            "Category": quantifier_lookup[quantifier],
            "Frequency": frequency,
            "Percentage": percentage
        })

    df = pd.DataFrame(records)

    # =====================================
    # Diagnostic report
    # =====================================

    print("\n" + "=" * 50)
    print(f"FILE: {file_path}")
    print("=" * 50)

    print("Successfully parsed items:", len(records))

    print(
        "Successfully parsed frequency:",
        df["Frequency"].sum() if not df.empty else 0
    )

    print("Failed regex:", len(skipped_no_match))

    print("No quantifier found:", len(skipped_no_quantifier))

    print("Ambiguous quantifier:", len(skipped_ambiguous))

    # Export skipped records for inspection

    base_path = Path(file_path).parent
    file_stem = Path(file_path).stem

    if skipped_no_match:
        pd.DataFrame(skipped_no_match).to_csv(
            base_path / f"{file_stem}_failed_regex.csv",
            index=False,
            encoding="utf-8-sig"
        )

    if skipped_no_quantifier:
        pd.DataFrame(skipped_no_quantifier).to_csv(
            base_path / f"{file_stem}_no_quantifier.csv",
            index=False,
            encoding="utf-8-sig"
        )

    if skipped_ambiguous:
        pd.DataFrame(skipped_ambiguous).to_csv(
            base_path / f"{file_stem}_ambiguous.csv",
            index=False,
            encoding="utf-8-sig"
        )

    return df


# =========================================
# 4. Import A and B
# =========================================

A = read_bnc_txt(
    r"D:\\Corpus Midterm\\structure A & B tables\\frequency_list structure A.txt"
)

B = read_bnc_txt(
    r"D:\\Corpus Midterm\\structure A & B tables\\frequency_list structure B.txt"
)

A = A.rename(columns={"Frequency": "A"})

B = B.rename(columns={"Frequency": "B"})


# =========================================
# 5. Compare parsed frequency
# =========================================

print("\n" + "=" * 50)
print("FREQUENCY COMPARISON")
print("=" * 50)

print("Structure A parsed frequency:", A["A"].sum())

print("Structure B parsed frequency:", B["B"].sum())


# =========================================
# 6. Aggregate by quantifier
# =========================================

A_quant = A.groupby(
    ["Quantifier", "Category"]
)["A"].sum()

B_quant = B.groupby(
    ["Quantifier", "Category"]
)["B"].sum()

quantifier_table = pd.concat(
    [A_quant, B_quant],
    axis=1
).fillna(0)

quantifier_table = quantifier_table.reset_index()

quantifier_table["Total"] = (
    quantifier_table["A"] +
    quantifier_table["B"]
)

quantifier_table["A %"] = (
    quantifier_table["A"] /
    quantifier_table["Total"] * 100
)

quantifier_table["B %"] = (
    quantifier_table["B"] /
    quantifier_table["Total"] * 100
)


# =========================================
# 7. Aggregate by category
# =========================================

category_table = quantifier_table.groupby(
    "Category"
)[["A", "B"]].sum()

category_table["Total"] = (
    category_table["A"] +
    category_table["B"]
)

category_table["A %"] = (
    category_table["A"] /
    category_table["Total"] * 100
)

category_table["B %"] = (
    category_table["B"] /
    category_table["Total"] * 100
)

category_table = category_table.reset_index()


# =========================================
# 8. Export CSV
# =========================================

output_dir = Path(r"D:\Corpus Midterm")

quantifier_table.to_csv(
    output_dir / "quantifier_frequency.csv",
    index=False,
    encoding="utf-8-sig"
)

category_table.to_csv(
    output_dir / "category_comparison.csv",
    index=False,
    encoding="utf-8-sig"
)

A.to_csv(
    output_dir / "structure_A_parsed.csv",
    index=False,
    encoding="utf-8-sig"
)

B.to_csv(
    output_dir / "structure_B_parsed.csv",
    index=False,
    encoding="utf-8-sig"
)


# =========================================
# 9. Final summary
# =========================================

print("\n" + "=" * 50)
print("PROCESSING COMPLETED!")
print("=" * 50)

print("\nQuantifier comparison:")
print(quantifier_table.to_string(index=False))

print("\nCategory comparison:")
print(category_table.to_string(index=False))

print("\nFinal frequency totals:")

print("A:", category_table["A"].sum())

print("B:", category_table["B"].sum())

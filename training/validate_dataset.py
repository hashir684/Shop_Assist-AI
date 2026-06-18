import json
from pathlib import Path
from collections import Counter

DATA_PATH = Path("data/dataset.jsonl")

required_fields = {"instruction", "input", "output", "category"}

category_counts = Counter()
total = 0

with open(DATA_PATH, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        data = json.loads(line)
        total += 1

        missing = required_fields - data.keys()

        if missing:
            print(f"Line {line_number} missing fields: {missing}")
        else:
            print(f"Line {line_number} OK")

        category_counts[data["category"]] += 1

print("\nValidation completed.")
print(f"Total examples: {total}")

print("\nCategory counts:")
for category, count in category_counts.items():
    print(f"{category}: {count}")
import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/dataset.jsonl")
OUTPUT_PATH = Path("data/support_sft.jsonl")

df = pd.read_json(INPUT_PATH, lines=True)

def make_prompt(row):
    return f"""### Instruction:
{row['instruction']}

### Customer Query:
{row['input']}

### Category:
{row['category']}

### Response:
{row['output']}"""

df["text"] = df.apply(make_prompt, axis=1)

df[["text"]].to_json(
    OUTPUT_PATH,
    orient="records",
    lines=True,
    force_ascii=False
)

print("SFT dataset created successfully.")
print(f"Saved at: {OUTPUT_PATH}")
print(f"Total examples: {len(df)}")

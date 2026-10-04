from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
p = BASE / "data" / "a320_ac.txt"
text = p.read_text(encoding="utf-8")

positions = []
start = 0
while True:
    idx = text.find("5-4-3", start)
    if idx == -1:
        break
    positions.append(idx)
    start = idx + 1

print(f"Found {len(positions)} occurrences of '5-4-3'\n")

for i, idx in enumerate(positions):
    snippet = text[idx:idx+80].replace("\n", " ")
    print(f"[{i}] pos {idx}: {snippet}")
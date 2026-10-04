from pathlib import Path

BASE = Path(__file__).resolve().parent.parent  # Airbus folder
p = BASE / "data" / "a320_ac.txt"

if not p.exists():
    print("FILE NOT FOUND at:", p)
    print("\nFiles that DO exist in data/:")
    for f in (BASE / "data").iterdir():
        print(" -", f.name)
else:
    text = p.read_text(encoding="utf-8")
    print("Total characters:", len(text))
    print('Occurrences of "5-4-3":', text.count("5-4-3"))
    print('Occurrences of "Hydraulic System":', text.count("Hydraulic System"))

    idx = text.find("5-4-3")
    print("\n--- Context around first 5-4-3 ---\n")
    if idx != -1:
        print(text[max(0, idx - 100): idx + 800])
    else:
        print("NOT FOUND IN FILE")
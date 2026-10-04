import json
from pathlib import Path

# UPDATE this path once we know where it actually lives (see Step 1)
STORAGE_PATH = Path("rag_storage_real_test/kv_store_text_chunks.json")

if not STORAGE_PATH.exists():
    print("NOT FOUND at:", STORAGE_PATH.resolve())
else:
    data = json.load(open(STORAGE_PATH, encoding="utf-8"))
    print(f"Total chunks: {len(data)}\n")
    for i, (k, v) in enumerate(data.items()):
        content = v.get("content", "")
        print(f"--- Chunk {i} ({len(content)} chars) ---")
        print(content[:200])
        print()
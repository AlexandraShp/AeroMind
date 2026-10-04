import json
from pathlib import Path

storage = Path("./rag_storage_real_test")

chunks_file = storage / "kv_store_text_chunks.json"

print("Looking for:")
print(chunks_file)

if not chunks_file.exists():
    print("\nFile not found.")
    print("\nFiles in storage:")
    for file in storage.iterdir():
        print(file.name)
    raise SystemExit

with open(chunks_file, "r", encoding="utf-8") as f:
    chunks = json.load(f)

print("\n==============================")
print("NUMBER OF CHUNKS:", len(chunks))
print("==============================\n")

for i, (chunk_id, chunk) in enumerate(chunks.items(), 1):

    print(f"\n========== CHUNK {i} ==========")
    print("ID:", chunk_id)

    if isinstance(chunk, dict):
        print("Keys:", list(chunk.keys()))

        content = (
            chunk.get("content")
            or chunk.get("text")
            or chunk.get("chunk")
            or ""
        )

        print("\nCONTENT:")
        print(content[:2000])

    else:
        print(chunk[:2000] if isinstance(chunk, str) else chunk)
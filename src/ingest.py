import asyncio, sys
from pathlib import Path
from rag_factory import get_rag, BASE

async def main(aircraft_id, txt_name):
    rag = await get_rag(aircraft_id)
    path = BASE / "data" / txt_name
    await rag.ainsert(path.read_text(encoding="utf-8"), file_paths=path.name)
    await rag.finalize_storages()
    print("Ingestion done")

asyncio.run(main(sys.argv[1], sys.argv[2]))
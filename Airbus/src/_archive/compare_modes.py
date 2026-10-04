import asyncio, time
from lightrag import QueryParam
from rag_factory import get_rag

QUESTIONS = [
    "What are the main dimensions of the A320?",
    "What ground service connections does the aircraft have?",
    "What are the maximum weights of the aircraft?",
]

async def main():
    rag = await get_rag("a320_test")
    for q in QUESTIONS:
        print("\n" + "=" * 70 + f"\nQ: {q}")
        for mode in ["naive", "local", "global", "hybrid", "mix"]:
            t = time.time()
            ans = await rag.aquery(q, param=QueryParam(mode=mode))
            print(f"\n--- {mode} ({time.time()-t:.1f}s) ---\n{ans}")

asyncio.run(main())
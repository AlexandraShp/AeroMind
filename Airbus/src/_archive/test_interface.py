import asyncio

from lightrag_service import AeroMindLightRAG


async def main():

    lightrag = AeroMindLightRAG()

    await lightrag.initialize()

    result = await lightrag.ask(
        question="What are hydraulic systems used for?"
    )

    print("\n================ RESULT ================\n")
    print(result)

    print("\n================ ANSWER ================\n")
    print(result["answer"])

    print("\n================ SOURCES ================\n")
    print(result["sources"])

    print("\n================ METADATA ================\n")
    print(result["metadata"])


if __name__ == "__main__":
    asyncio.run(main())
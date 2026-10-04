import asyncio
import json
from lightrag_service import ask

async def main():
    result = await ask(
        aircraft_id="a320",
        question="What is the procedure for hydraulic ground servicing on the A320?",
        conversation_id="conversation_001",
    )
    print(json.dumps(result, indent=2))

asyncio.run(main())
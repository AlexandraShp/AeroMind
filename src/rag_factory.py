from pathlib import Path
from dotenv import load_dotenv

BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")
STORAGE = BASE / "rug_storage"          # rename here if you rename the folder

from lightrag import LightRAG
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status

async def get_rag(aircraft_id: str) -> LightRAG:
    rag = LightRAG(
        working_dir=str(STORAGE / aircraft_id),
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete,
    )
    await rag.initialize_storages()
    await initialize_pipeline_status()
    return rag
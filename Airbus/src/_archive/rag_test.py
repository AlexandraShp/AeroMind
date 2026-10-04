import os
import asyncio
from dotenv import load_dotenv

from lightrag import LightRAG
from lightrag.llm.openai import openai_complete_if_cache
from lightrag.utils import EmbeddingFunc
from lightrag.llm.openai import openai_embed


load_dotenv()


# --------------------------------------------------
# 1. Gemini through OpenRouter
# --------------------------------------------------

async def llm_model_func(
    prompt,
    system_prompt=None,
    history_messages=[],
    **kwargs
):
    return await openai_complete_if_cache(
        model=os.getenv("LLM_MODEL"),
        prompt=prompt,
        system_prompt=system_prompt,
        history_messages=history_messages,
        api_key=os.getenv("LLM_BINDING_API_KEY"),
        base_url=os.getenv("LLM_BINDING_HOST"),
        **kwargs
    )


# --------------------------------------------------
# 2. Embedding model through OpenRouter
# --------------------------------------------------

async def embedding_func(texts):
    return await openai_embed(
        texts,
        model=os.getenv("EMBEDDING_MODEL"),
        api_key=os.getenv("EMBEDDING_BINDING_API_KEY"),
        base_url=os.getenv("EMBEDDING_BINDING_HOST"),
    )


# --------------------------------------------------
# 3. Create LightRAG
# --------------------------------------------------

async def main():

    rag = LightRAG(
        working_dir="./rag_storage",
        llm_model_func=llm_model_func,
        embedding_func=EmbeddingFunc(
            embedding_dim=int(os.getenv("EMBEDDING_DIM")),
            max_token_size=8192,
            func=embedding_func,
        ),
    )

    await rag.initialize_storages()

    print("LightRAG initialized successfully!")


if __name__ == "__main__":
    asyncio.run(main())
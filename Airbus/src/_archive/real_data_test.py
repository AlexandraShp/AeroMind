import os
import asyncio
from dotenv import load_dotenv

from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import openai_complete_if_cache
from lightrag.llm.openai import openai_embed
from lightrag.utils import EmbeddingFunc


load_dotenv()


# ----------------------------------------
# LLM
# ----------------------------------------

async def llm_model_func(
    prompt,
    system_prompt=None,
    history_messages=None,
    **kwargs
):
    kwargs["max_tokens"] = 1000

    return await openai_complete_if_cache(
        model=os.getenv("LLM_MODEL"),
        prompt=prompt,
        system_prompt=system_prompt,
        history_messages=history_messages or [],
        api_key=os.getenv("LLM_BINDING_API_KEY"),
        base_url=os.getenv("LLM_BINDING_HOST"),
        **kwargs
    )


# ----------------------------------------
# Embeddings
# ----------------------------------------

async def embedding_func(texts):
    return await openai_embed(
        texts,
        model=os.getenv("EMBEDDING_MODEL"),
        api_key=os.getenv("EMBEDDING_BINDING_API_KEY"),
        base_url=os.getenv("EMBEDDING_BINDING_HOST"),
    )


# ----------------------------------------
# Main
# ----------------------------------------

async def main():

    rag = LightRAG(
        working_dir="./rag_storage_real_test",
        llm_model_func=llm_model_func,
        embedding_func=EmbeddingFunc(
            embedding_dim=int(os.getenv("EMBEDDING_DIM")),
            max_token_size=8192,
            func=embedding_func,
        ),
    )

    await rag.initialize_storages()

    # ----------------------------------------
    # Load real Airbus TXT
    # ----------------------------------------

    data_path = "Airbus/data/a320_ac_test.txt"

    with open(data_path, "r", encoding="utf-8") as f:
        full_text = f.read()

    print("Full document loaded.")
    print("Characters:", len(full_text))

    # ----------------------------------------
    # Take only a small sample
    # ----------------------------------------

    sample_text = full_text[:20000]

    print("Using sample of:", len(sample_text), "characters")

    # ----------------------------------------
    # Insert into RAG
    # ----------------------------------------

    print("\nInserting real Airbus data...")

    await rag.ainsert(sample_text)

    print("Real Airbus sample inserted successfully!")

    # ----------------------------------------
    # Ask question
    # ----------------------------------------

    question = input(
        "\nAsk a question about the Airbus data: "
    )

    response = await rag.aquery(
        question,
        param=QueryParam(mode="hybrid")
    )

    print("\nAnswer:")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
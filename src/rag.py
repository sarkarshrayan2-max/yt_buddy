from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from src.chunker import split_transcript
from src.config import groq_llm


def create_vector_store(transcript):
    chunks = split_transcript(
        transcript,
        chunk_size=500,
        overlap=100
    )

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store


def answer_question(vector_store, question):
    relevant_docs = vector_store.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in relevant_docs]
    )

    prompt = f"""
        You are answering questions about a YouTube video.

        ONLY use the provided context.

        If the answer is not explicitly mentioned,
        reply exactly:

        "I could not find this information in the video."

        Context:
        {context}

        Question:
        {question}
"""

    response = groq_llm.invoke(prompt)

    return response.content

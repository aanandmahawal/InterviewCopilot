from langchain_community.vectorstores import FAISS

from rag.embeddings import embeddings


def create_vector_store(chunks):

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store
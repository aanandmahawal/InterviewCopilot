from rag.vector_store import create_vector_store


def get_relevant_context(chunks, query):

    vector_store = create_vector_store(chunks)

    docs = vector_store.similarity_search(
        query,
        k=5
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context
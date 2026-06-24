from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma


embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)


def retrieve_context(query):

    docs = vectordb.similarity_search(
        query,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context
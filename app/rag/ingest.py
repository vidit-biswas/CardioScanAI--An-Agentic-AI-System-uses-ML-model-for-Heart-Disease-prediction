import os

from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma


KNOWLEDGE_PATH = "data/knowledge"


def build_vector_db():

    documents = []

    for file in os.listdir(KNOWLEDGE_PATH):

        if file.endswith(".txt"):

            loader = TextLoader(
                os.path.join(KNOWLEDGE_PATH, file),
                encoding="utf-8"
            )

            documents.extend(
                loader.load()
            )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(
        documents
    )

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    print(
        f"Stored {len(chunks)} chunks."
    )


if __name__ == "__main__":
    build_vector_db()
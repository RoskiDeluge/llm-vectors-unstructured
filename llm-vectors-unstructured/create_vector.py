from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os
from dotenv import load_dotenv
load_dotenv()


COURSES_PATH = "llm-vectors-unstructured/data/asciidoc"

# Load lesson documents
loader = DirectoryLoader(
    COURSES_PATH, glob="**/lesson.adoc", loader_cls=TextLoader)
docs = loader.load()

# Create a text splitter
text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1500,
    chunk_overlap=200,
)

# Split documents into chunks
chunks = text_splitter.split_documents(docs)

print(chunks)

# Create a Neo4j vector store
# neo4j_db =

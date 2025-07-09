import os
from langchain_community.document_loaders import DorectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings

# Settings
SOURCE_DIR = 'kb_docs'
VECTOR_INDEX_PATH = 'faiss_index'
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

def load_documents():
  loaders = [
    DirectoryLoader(SOURCE_DIR, glob='**/*.txt', loader_cls=TextLoader),
    DirectoryLoader(SOURCE_DIR, glob='**/*.md', loader_cls=TextLoader),
    DirectoryLoader(SOURCE_DIR, glob='**/*.pdf', loader_cls=PyPDFLoader)

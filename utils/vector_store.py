from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings

def get_vector_store():
  return FAISS.load_local('faiss_index', embeddings=Ollamambeddings(model='nomic-embed-text'))

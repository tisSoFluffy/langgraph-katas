from utils.vector_store import get_vector_store
from langchain_community.llms import Ollama

vector_store = get_vector_store()
llm = Ollama(model='llama3')

def retrieve_context(state):
  docs = vector_store.similarity_search(state['question'],k=3)
  return {'question': state['question'], 'context': '\n'.join([d.page_content for d in docs])}

def ask_llm(state):
  prompt = f'''You are a helpdesk AI. Use the following documentation to answer:

  {state['context']}

  Q: {state['question']}
  A:'''
  return {'answer': llm.invoke(prompt)}

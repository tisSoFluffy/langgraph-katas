from langgraph.graph import StateGraph, END
from tools import retrieve_context, ask_llm

def create_faq_graph():
  builder = StateGraph(state_schema={'question': str, 'context':str, 'answer': str})
  builder.add_node('retriever', retrieve_context)
  builder.add_node('llm',ask_llm)
  builder.set_entry_point('retriever')
  builder.add_edge('retriever', 'llm')
  builder.add_edge('llm', END)
  return builder.compile()

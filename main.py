from graph import create_faq_graph

if __name__ == "__main__":
  graph = create_faq_graph()
  user_question = input('Ask a support question: ')
  result = graph.ivoke({"question": user_question})
  print(result['answer'])

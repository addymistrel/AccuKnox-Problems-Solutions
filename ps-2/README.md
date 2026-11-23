## 1. Where would you rate yourself on (LLM, Deep Learning, AI, ML). A, B, C [A = can code independently; B = can code under supervision; C = have little or no understanding]

#### Ans: A

## 2. What are the key architectural components to create a chatbot based on LLM? Please explain the approach on a high-level

#### Ans: Major key architectural components to create a chatbots are: Apis, authentication layers, LLM orchestration, rag, memory and context management, tool calls and finally fallbacks and exception handlings.

#### On high level the architecture first involves a client app which serve as an interface to communicate with the user. Once the user provides an input the search chat input is carried by apis over a network. The request is then validated and authenticated and goes into LLM orchestration layers. Here in this layer LLM first decide the category of the question it belongs to and once it is clarified it tokenizes and matches with any FAQs whose answers are already prewritten in the software. If it matches the answer returns immedeiately else LLM decides to run an agentic loop which involves RAG and tool calls procedurally. Once a final answer is achieved it returns back the final answer in proper format back to the user.

## 3. Please explain vector databases. If you were to select a vector database for a hypothetical problem (you may define the problem) which one will you choose, and why?

#### Ans: A vector database is used to store and search data in the form of vectors (numerical representations called embeddings). It helps to find similar data based on meaning instead of matching exact words. For example, if a user asks "How can I get my money back?", it can find a document about the "Refund Policy" even if the exact words are different. It is mainly used in RAG based chatbots to retrieve relevant information and provide better answers using an LLM.

#### If I have to choose a vector database for an enterprise chatbot which contains thousands of company documents, I would choose Qdrant. The main reason is that it provides fast similarity search, supports metadata filtering, is open source and can be self hosted. It also integrates easily with Python and frameworks like LangChain. I think it is a good choice for this problem because it provides good performance and flexibility without depending completely on a paid managed service.

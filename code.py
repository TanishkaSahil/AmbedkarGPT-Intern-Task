# main.py

"""
Command-line Q&A System for Dr. B.R. Ambedkar's Speech
"""

# Import necessary libraries
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

# Step 1: Load speech text from file
with open('speech.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Step 2: Split text into manageable chunks for embeddings
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_text(text)

# Step 3: Create embeddings 
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 4: Store embeddings in ChromaDB (local vector store)
db = Chroma.from_texts(texts, embedding_model)

# Step 5: Set up LangChain RetrievalQA using Ollama (Mistral 7B locally)
llm = Ollama(model="mistral")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# --- Command-line Q&A loop ---
def ask_question():
    print("Ask questions about Dr. Ambedkar's speech (type 'exit' to quit):")
    while True:
        query = input("Question: ")
        if query.lower().strip() == 'exit':
            break
        answer = qa_chain.run(query)
        print(f"Answer: {answer}\n")

if __name__ == '__main__':
    ask_question()

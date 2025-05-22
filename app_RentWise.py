# streamlit_app.py

import os
import yaml
import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables.history import RunnableWithMessageHistory

# -------------------------------------------------------
# ✅ APP CONFIG
# -------------------------------------------------------

st.set_page_config(page_title="RentWise AI - California Tenant Rights Chatbot")
st.title("🏡 RentWise: California Tenant Rights Chatbot")

# Load API key
os.environ["OPENAI_API_KEY"] = yaml.safe_load(open("credentials.yml"))['openai']

# Chat memory
msgs = StreamlitChatMessageHistory(key="langchain_messages")
if len(msgs.messages) == 0:
    msgs.add_ai_message("Hi! Ask me anything about your tenant rights in California.")

# -------------------------------------------------------
# ✅ MODEL SELECTION
# -------------------------------------------------------

LLM = "gpt-4o-mini"

llm = ChatOpenAI(
    model=LLM,
    temperature=0.3  # or 0.7 if you prefer a bit more creativity
)

# -------------------------------------------------------
# ✅ VECTOR DB SETUP
# -------------------------------------------------------

vectorstore = Chroma(
    persist_directory="challenges/solution_03_RentWise/db/chroma_rentwise.db",
    embedding_function=OpenAIEmbeddings(model="text-embedding-ada-002")
)
retriever = vectorstore.as_retriever()

# -------------------------------------------------------
# ✅ RAG WITH MEMORY
# -------------------------------------------------------

contextual_prompt = ChatPromptTemplate.from_messages([
    ("system", "Refactor the user input to a standalone question."),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])
history_aware_retriever = create_history_aware_retriever(llm, retriever, contextual_prompt)

qa_system_prompt = """You are a legal assistant for tenant rights in California. 
Use the retrieved context to answer the user's question. 
Respond strictly in the following JSON format without deviation:

{
    "answer": "...",
    "source_type": "...",
    "source_file": "..."
}
"""

response_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a legal assistant for tenant rights in California. 
Use the following context to answer the user's question. 
Respond strictly in the following JSON format without deviation:

{{  
    "answer": "...",  
    "source_type": "...",  
    "source_file": "..."  
}}

If you do not know the answer, say "I don't know" as the value for "answer".
Only output valid JSON, no extra text.

{context}"""),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

response_chain = create_stuff_documents_chain(llm, response_prompt)

rag_chain = create_retrieval_chain(history_aware_retriever, response_chain)
chat_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    lambda session_id: msgs,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)

# -------------------------------------------------------
# ✅ DISPLAY CHAT
# -------------------------------------------------------

import json

for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

if question := st.chat_input("Ask me anything about rent, eviction, or housing laws:"):
    st.chat_message("human").write(question)
    with st.spinner("Thinking..."):
        response = chat_rag_chain.invoke(
            {"input": question},
            config={"configurable": {"session_id": "user-session"}}
        )
        
        # ✅ Try to parse JSON string into a dict
        try:
            parsed = json.loads(response["answer"]) if isinstance(response["answer"], str) else response["answer"]
            
            # ✅ Display as structured content
            st.chat_message("ai").markdown(f"""
            📘 **Answer:** {parsed.get("answer", "N/A")}

            📄 **Source:** `{parsed.get('source_file', 'N/A')}`  
            🔖 **Type:** `{parsed.get('source_type', 'N/A')}`
            """)

        except Exception as e:
            st.chat_message("ai").write("⚠️ Failed to parse structured response:")
            st.chat_message("ai").write(response["answer"])


# -------------------------------------------------------
# ✅ DEBUG (Optional)
# -------------------------------------------------------

#with st.expander("🔍 Debug: Message History"):
    #st.json(st.session_state.langchain_messages)

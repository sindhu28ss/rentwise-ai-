# 🏡 RentWise AI: Empowering Tenants with Generative AI

RentWise AI is a Generative AI-powered chatbot designed to simplify California tenant laws. Built during the 5-Day Gen AI Intensive Course with Google, this project was inspired by the real challenges faced by international students and first-time renters trying to navigate complex legal documents.

## 📌 Why This Project?
As a first-time renter in California, I found tenant rights information scattered across lengthy PDFs and government websites—often buried in legal jargon. The lack of accessible, clear guidance sparked the idea for RentWise AI: an intelligent assistant to help renters understand their rights in simple language.

## ❗The Problem

Many tenants struggle with:
- Understanding eviction notices  
- Rent increase limits  
- Security deposit disputes  
- Habitability standards  
- City-specific housing ordinances

Legal resources are often inaccessible, fragmented, and difficult to interpret—especially for non-native English speakers or those without legal backgrounds.

## ✅ The Solution
RentWise AI helps tenants get clear, reliable answers to questions like:
- `“Can my landlord raise rent this year?”`
- `“What are my rights during an eviction?”`

It leverages:
- Uses RAG to pull information directly from trusted legal documents
- Embeds content using a Text Embedding Model and stores it in a Vector Database (Chroma)
- Leverages an LLM with chat memory and contextual awareness
- Delivers structured outputs through a friendly Streamlit UI

## 🧠 Architecture Overview

<p align="center">
  <img src="https://github.com/sindhu28ss/rentwise-ai-/blob/main/images/RentWise.png" width="1000">
</p>

## How It Works:

RentWise AI combines document understanding, semantic retrieval, and structured response generation to make California housing laws accessible through a conversational interface. 

**1. Document Processing & Chunking:**
Multiple tenant related PDFs — including tenant rights guides, rent control laws, and eviction notices from the official California government sources — are loaded using custom loaders. Narrative sections are split into overlapping text chunks using a recursive character-based splitter. This preserves sentence context and improves semantic relevance during retrieval. Tabular data are parsed, cleaned, and converted into natural language snippets with metadata like source_file and type for traceability.

**2. Embeddings + Vector Store:**
Each processed chunk is converted into high-dimensional semantic vectors using a text embedding model. This step captures the contextual meaning of legal phrases and clauses.
The resulting vectors are stored in a vector database (Chroma DB), enabling efficient similarity-based retrieval of relevant chunks during user queries.

**3. Retrieval-Augmented Generation (RAG):**
When a user submits a question, the system performs a semantic search across the vector database to retrieve the most relevant chunks from the knowledge base.
These chunks are inserted into a carefully structured prompt, which helps the language model generate grounded and contextually accurate responses.

**4. Structured LLM Response:**
A custom prompting system ensures that every response is returned in a consistent JSON format, with keys like:
- ` "answer"` — the legal explanation
- ` "source_file"` — the originating document
- ` "source_type"` — the category (e.g., rent law, eviction guide)

This structured output makes it easy to display in the app, log for future analysis, or even extend into external APIs.

**5. Contextual Awareness with Chat Memory:**
The system retains chat history to support multi-turn conversations, allowing users to ask follow-up questions naturally. When needed, it reformulates those follow-ups into standalone questions to maintain relevance and coherence.

**6. Streamlit-Based Chat Interface:**
A web interface allows users to type in open-ended questions and receive clean, structured responses. Responses are broken down into human-readable blocks: Answer, Source File, and Source Type. The app preserves chat history and delivers real-time responses, creating a seamless and interactive user experience.

## Sample Interactions with RentWise AI:

<p align="center">
  <img src="https://github.com/sindhu28ss/rentwise-ai-/blob/main/images/sample%20interaction.png" width="600">
</p>

## Final Thoughts
RentWise AI shows how Generative AI can transform complex legal material into accessible, real-time support. It's more than a chatbot—it's a step toward equitable, informed renting.



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
- Retrieval-Augmented Generation (RAG) to retrieve trusted legal content
- Embeddings to represent document semantics
- Chroma DB as a vector store
- Streamlit for an intuitive, chat-based web interface

## 🧠 Architecture Overview

### Document Processing & Chunking
- Parses narrative + tabular content from government PDFs  
- Splits text into meaningful chunks with metadata (e.g., source, type)

### Embeddings + Vector Database
- Converts chunks to vectors using a text embedding model  
- Stores them in Chroma DB for semantic search

### RAG Pipeline
- Retrieves relevant document chunks for a given question  
- Inserts them into prompts for context-grounded LLM responses

### Structured LLM Output
- Returns responses in a JSON format with fields like `answer`, `source_file`, and `source_type`

### Contextual Awareness
- Maintains chat memory for multi-turn conversations

### Streamlit UI
- Clean, chat-based frontend  
- Supports natural language questions and displays structured responses

## Final Thoughts
RentWise AI shows how Generative AI can transform complex legal material into accessible, real-time support. It's more than a chatbot—it's a step toward equitable, informed renting.



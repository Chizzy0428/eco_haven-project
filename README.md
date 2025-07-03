# EcoHaven Mart Chatbot

A smart chatbot for a fictional eco-friendly store using LangChain + Streamlit.

## Features
- Answers store-related questions
- Uses a RAG system (OpenAI + FAISS)
- Deployable as a local or web app

## Run Locally
1. Create a virtual environment
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Add your OpenAI key:
   ```
   export OPENAI_API_KEY=your_key_here
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

## Files
- `store_data/about_us.md`: Store & owner info
- `store_data/products.json`: Sample products
# 🛒 EcoHaven Mart Chatbot

An AI-powered chatbot for EcoHaven Mart a fictional sustainable store built with **LangChain**, **OpenAI**, **FAISS**, and **Streamlit**. It provides customers with fast, intelligent answers to any question about the store, its owners, policies, and products.

 **Live App:**  
 [Launch EcoHaven Chatbot](https://ecohaven-project-9kxelogxagfx7m4na3eggr.streamlit.app/)



## About the Project

EcoHaven Mart promotes eco-friendly living by offering sustainable products like bamboo toothbrushes, reusable bags, and solar-powered gadgets. This chatbot acts as a **24/7 intelligent store assistant**, capable of handling:

- Product lookup
- Pricing and availability
- Store policies
- Owner background
- General inquiries



## Key Features

- ✅ **RAG-based chatbot** using LangChain and OpenAI
- ✅ Integrated with a custom store knowledge base
- ✅ Powered by FAISS for semantic search
- ✅ Secure API access with `st.secrets`
- ✅ Streamlit frontend for easy interaction
- ✅ Hosted and accessible via public URL



## Tech Stack

| Layer        | Tool / Library           |
|--------------|---------------------------|
| LLM          | OpenAI GPT (via LangChain) |
| Embeddings   | OpenAIEmbeddings          |
| Vector Store | FAISS                     |
| Frontend     | Streamlit                 |
| Backend      | Python                    |



## Project Structure

```

eco\_haven-project/
│
├── app.py                    # Streamlit frontend interface
├── chatbot.py                # Chatbot logic (RAG pipeline)
├── store\_data/
│   ├── about\_us.md           # Store and owner background
│   └── products.json         # Product catalog (JSON format)
├── .streamlit/
│   └── secrets.toml          # Secure API key config (Streamlit Cloud)
├── requirements.txt          # Python dependencies
└── README.md                 # This file

````



## Running the App Locally

### 1. Clone the repository

```bash
git clone https://github.com/Chizzy0428/eco_haven-project.git
cd eco_haven-project
````

### 2. Create a virtual environment and activate

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up secrets

Create a `.streamlit/secrets.toml` file with your OpenAI key:

```toml
openai_api_key = "your_actual_openai_key_here"
```

### 5. Run the app

```bash
streamlit run app.py
```



## Example Questions to Try

* "What do you sell?"
* "Who owns EcoHaven Mart?"
* "Tell me about Chinelo Adigwe."
* "What's the return policy?"
* "How much does a solar lantern cost?"



## Deploying to Streamlit Cloud

This app is already deployed here:
➡️ [https://ecohaven-project-9kxelogxagfx7m4na3eggr.streamlit.app/](https://ecohaven-project-9kxelogxagfx7m4na3eggr.streamlit.app/)

To deploy your fork:

1. Push to GitHub
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Add your API key under **Settings → Secrets**:

   ```
   openai_api_key = your_actual_key_here
   ```


## License

MIT License — feel free to reuse and modify this project for your own store or brand.



##  About the Creator

Built by [Chizzy](https://github.com/Chizzy0428) — a data scientist passionate about real-world AI applications.
Connect on GitHub or reach out for collaboration ideas.








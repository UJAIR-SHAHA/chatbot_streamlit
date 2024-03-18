import streamlit as st
from llama_index.core import VectorStoreIndex, ServiceContext, Document
from llama_index.llms.openai import OpenAI
import openai
from llama_index.core import SimpleDirectoryReader
import random


secret= "secret.toml"
st.set_page_config(page_title="Chat with our Ai virtaul assistant", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets.openai_key
st.title("Chat with our virtaul assistant.")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome. I am here to help you with buying a mobile phone."}
    ]
    
predefined_queries = [
    "Can you tell me more about the camera specifications?",
    "What are the available color options?",
    "I'd like to know about the battery life of this phone.",
    # Add more queries as needed
]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Processing please wait. This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are a virtaul assistant for mobile shop which help customers to buy a mobile phones. Also make converstion with customers regarding their choice and recommend them mobile phone to buy."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
            
# Add a button below the chat response
if st.session_state.messages[-1]["role"] == "assistant":
    if st.button("Request More Information"):
        # Select a predefined query randomly
        predefined_query = random.choice(predefined_queries)
        # Respond with the predefined query
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(predefined_query)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)
import streamlit as st
import webbrowser
import time

def button_responses(messages):
    for message in messages:
        if message["role"] == "assistant":
            if "product page" in message["content"]:
                if st.button("Visit product page"):
        # Define the URL of the product page
                    product_page_url = "https://github.com/UJAIR-SHAHA/chatbot_streamlit"  # Replace this with the actual URL

                    st.markdown(f'<meta http-equiv="refresh" content="0;URL={product_page_url}">', unsafe_allow_html=True)
                    
                    # Add a short delay to allow redirection
                    time.sleep(1)
            
            # Add more conditions as needed for other responses

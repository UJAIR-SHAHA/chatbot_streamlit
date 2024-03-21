import streamlit as st
import webbrowser

def button_responses(messages):
    for message in messages:
        if message["role"] == "assistant":
            if "product page" in message["content"]:
                if st.button("Visit product page"):
        # Define the URL of the product page
                    product_page_url = "https://github.com/UJAIR-SHAHA/chatbot_streamlit"  # Replace this with the actual URL

                    st.write(
                        f'<script>window.open("{product_page_url}");</script>',
                        unsafe_allow_html=True
                    )
            
            # Add more conditions as needed for other responses

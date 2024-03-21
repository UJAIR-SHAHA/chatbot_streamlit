import streamlit as st

def button_responses(messages):
    for message in messages:
        if message["role"] == "assistant":
            if "product page" in message["content"]:
                if st.button("Visit product page"):
        # Define the URL of the product page
                    product_page_url = "https://example.com/product-page"  # Replace this with the actual URL

        # Display a clickable hyperlink to the product page
                    st.markdown(f"[Click here to visit the product page]({product_page_url})")
            elif "color options" in message["content"]:
                if st.button("Request Color Options"):
                    predefined_query = "Can you tell me more about the available color options?"
                    with st.spinner("Thinking..."):
                        st.write(predefined_query)
                        message = {"role": "assistant", "content": predefined_query}
                        messages.append(message)
            # Add more conditions as needed for other responses

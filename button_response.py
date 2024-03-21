import streamlit as st
import webbrowser
import time

def button_responses(messages):
    for message in messages:
        if message["role"] == "assistant":
            if "product page" in message["content"]:
                if st.button("Visit product page"):
        # Define the URL of the product page
                    product_page_url = "https://www.flipkart.com/realme-5-crystal-purple-128-gb/p/itmfj9twbwfznhyk?pid=MOBFJ9TWDQNYX8VZ&lid=LSTMOBFJ9TWDQNYX8VZJOD8VK&marketplace=FLIPKART&q=realme+5&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=52c9bc4a-902e-4156-83ed-414c736434b4.MOBFJ9TWDQNYX8VZ.SEARCH&ppt=sp&ppn=sp&ssid=wfy9czky8g0000001711007175517&qH=47703f7036714a82"  # Replace this with the actual URL

                    st.markdown(f'<meta http-equiv="refresh" content="0;URL={product_page_url}">', unsafe_allow_html=True)
                    
                    # Add a short delay to allow redirection
                    time.sleep(1)
            
            # Add more conditions as needed for other responses

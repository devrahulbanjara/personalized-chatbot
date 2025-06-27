import streamlit as st
import requests

st.title("Personal Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is your question?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/chat", json={"query": prompt}
            )
            response.raise_for_status()  # Raise an exception for bad status codes
            full_response = response.json().get("response", "No response from the bot.")
        except requests.exceptions.RequestException as e:
            full_response = f"Error: {e}"

        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

import streamlit as st
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

OPENAI_API_KEY = "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"


# Initialize ChatOpenAI and ConversationChain
llm = ChatOpenAI(model_name="gpt-3.5-turbo")
conversation = ConversationChain(memory=st.session_state.buffer_memory, llm=llm)

st.title(" 🤖 Chatbot Made by Team BiteBase")
st.subheader(" Chat and Explore with AI :-")
query = st.text_input("Hey there! Ask your question ")

if query:
    with st.spinner("typing..."):
        response = conversation.predict(input=query)
        st.write(response)

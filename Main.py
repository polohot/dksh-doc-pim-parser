import pip_system_certs.wrapt_requests
import streamlit as st

st.title('Streamlit App')

bodyV1 = '''
V1 - 2025-03-07

First Version using llamaparse then input to openAI chatbot API
Mostly showing debug values

Step1: input PDF file
Step2: Parse PDF using llamaparse
Step3: Indexing/Embedding
Step4: Chat
'''
st.code(bodyV1)
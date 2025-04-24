import pip_system_certs.wrapt_requests

import streamlit as st
import os
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse


########
# INIT #
########

# STREAMLIT
st.set_page_config(page_title="PIM Document Parser",
                   layout='wide')
st.title("PIM Document Parser")

# LLAMA PARSE
load_dotenv()
parser = LlamaParse(
    api_key=os.environ['LLAMA_CLOUD_API_KEY'],  # can also be set in your env as LLAMA_CLOUD_API_KEY
    num_workers=4,                              # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    language="en",                              # optionally define a language, default=en
)

# SESSION STATE
if 'container' not in st.session_state:
    st.session_state.container = 1


###################################################
# CONTAINER1: UPLOAD AND CONVERT TO BASE64 STRING #
###################################################

if st.session_state.container == 1:
    st.write(os.environ['LLAMA_CLOUD_API_KEY'])

    # HEADER
    st.markdown('<h3 style="color: black;">Step1: Upload Documents</h3>', unsafe_allow_html=True)

    # UPLOAD FILE AND CONVERT TO B64 IMAGES
    uploadedDocs = st.file_uploader("Upload", type=['pdf','xlsx','jpg','jpeg','docx'], accept_multiple_files=True)

    if uploadedDocs:
        st.text(uploadedDocs)

        for doc in uploadedDocs:
            doc_parsed = parser.load_data(doc.getvalue(), extra_info={"file_name": "_"})

    
            st.text(doc_parsed)
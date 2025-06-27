import streamlit as st
import httpx
import time

st.set_page_config(page_title="Document Upload System", layout="wide")

st.title("Document Upload System")

# Add custom CSS for better UI
st.markdown(
    """
    <style>
    .stButton>button {
        width: 100%;
        margin-top: 20px;
    }
    .upload-status {
        margin-top: 20px;
        padding: 20px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# File uploader
uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True,
    help="You can upload multiple PDF files at once",
)

if uploaded_files:
    if st.button("Process Documents"):
        with st.spinner("Processing documents..."):
            try:
                files = [
                    ("files", (file.name, file.getvalue(), "application/pdf"))
                    for file in uploaded_files
                ]

                with httpx.Client() as client:
                    response = client.post(
                        "http://localhost:8000/api/upload-documents",
                        files=files,
                        timeout=None,
                    )

                if response.status_code == 200:
                    result = response.json()
                    if result["status"] == "success":
                        st.success(result["message"])
                        if result["processed_files"]:
                            st.write("Processed files:")
                            for file in result["processed_files"]:
                                st.write(f"✓ {file}")
                    else:
                        st.error(f"Error: {result['message']}")
                else:
                    st.error(
                        f"Error: Failed to process documents. Status code: {response.status_code}"
                    )

            except Exception as e:
                st.error(f"Error: {str(e)}")
else:
    st.info("Please upload PDF documents to process")

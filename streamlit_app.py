import streamlit as st

# Sample documents (you can replace these with your actual documents)
documents = {
    "Document 1": "This is the content of document 1. You can replace this with your actual document content.",
    "Document 2": "This is the content of document 2. You can replace this with your actual document content.",
    "Document 3": "This is the content of document 3. You can replace this with your actual document content.",
    "Document 4": "This is the content of document 4. You can replace this with your actual document content.",
    "Document 5": "This is the content of document 5. You can replace this with your actual document content.",
    "Document 6": "This is the content of document 6. You can replace this with your actual document content."
}

st.title("Document Viewer")

# Create a selectbox for document selection
selected_doc = st.selectbox(
    "Select a document to view:",
    list(documents.keys())
)

# Display the selected document
st.write("### Selected Document:")
st.write(documents[selected_doc]) 

import streamlit as st
import os
from docx import Document
from pathlib import Path

# Set page config for a nicer look
st.set_page_config(
    page_title="Pandacea Document Viewer",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stSelectbox {
        margin-bottom: 2rem;
    }
    .document-content {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        font-family: 'Segoe UI', sans-serif;
        line-height: 1.6;
    }
    .document-content h1 {
        font-size: 1.8em;
        margin-bottom: 1rem;
        color: #2c3e50;
    }
    .document-content h2 {
        font-size: 1.5em;
        margin-bottom: 0.8rem;
        color: #34495e;
    }
    .document-content ul {
        margin-left: 1.5em;
        margin-bottom: 1em;
    }
    .document-content li {
        margin-bottom: 0.5em;
    }
    .bullet-point {
        margin-left: 20px;
        position: relative;
    }
    .bullet-point::before {
        content: "•";
        position: absolute;
        left: -15px;
    }
    </style>
""", unsafe_allow_html=True)

# Title with custom styling
st.markdown("""
    <h1 style='text-align: center; color: #1f77b4; margin-bottom: 2rem;'>
        📚 Pandacea Document Viewer
    </h1>
""", unsafe_allow_html=True)

def get_paragraph_format(paragraph):
    """Extract formatting information from a paragraph"""
    text = paragraph.text.strip()
    if not text:
        return None
    
    # Check if it's a heading
    if paragraph.style.name.startswith('Heading'):
        level = int(paragraph.style.name[-1])
        return f"<h{level}>{text}</h{level}>"
    
    # Check if it's a list item (bullet point)
    if text.startswith('•') or paragraph.style.name.startswith('List'):
        text = text.lstrip('•').strip()
        return f'<div class="bullet-point">{text}</div>'
    
    # Regular paragraph
    return f"<p>{text}</p>"

def read_docx(file_path):
    doc = Document(file_path)
    formatted_text = []
    
    for paragraph in doc.paragraphs:
        formatted = get_paragraph_format(paragraph)
        if formatted:
            formatted_text.append(formatted)
    
    return '\n'.join(formatted_text)

# Get list of documents from the docs folder
docs_folder = Path("docs")
documents = {}
for doc_file in docs_folder.glob("*.docx"):
    # Create a nice display name by removing the .docx extension and replacing underscores
    display_name = doc_file.stem.replace("_", " ").replace("–", "-")
    documents[display_name] = str(doc_file)

# Create two columns for better layout
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("### Select Document")
    selected_doc = st.selectbox(
        "Choose a document to view:",
        list(documents.keys()),
        format_func=lambda x: x
    )

with col2:
    st.markdown("### Document Content")
    if selected_doc:
        try:
            doc_content = read_docx(documents[selected_doc])
            st.markdown(f'<div class="document-content">{doc_content}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error reading document: {str(e)}")

# Add a footer
st.markdown("""
    <div style='text-align: center; margin-top: 2rem; color: #666;'>
        <p>Pandacea Document Viewer | Built with Streamlit</p>
    </div>
""", unsafe_allow_html=True) 

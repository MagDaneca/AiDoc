import PyPDF2
import re
import streamlit as st


def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        text += page.extract_text()
    return text

def hide_streamlit_style():
    return """
        <style>
        [data-testid="stToolbar"] {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        </style>
        """

def init_session_state():
    if 'Glucose' not in st.session_state:
        st.session_state.Glucose = None
    if 'BloodPressure' not in st.session_state:
        st.session_state.BloodPressure = None
    if 'Insulin' not in st.session_state:
        st.session_state.Insulin = None

def check_parameters_filled(age, sex, height, kilo):
    if age is None or sex is None or height is None or kilo is None or age == 0 or height == 0 or kilo == 0:
        return False  
    return True  

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def init_session_state():
    if 'data' not in st.session_state:
        st.session_state.data = True

custom_css = """
    <style>
    .card {
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.1);
    }
    .card-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .card-content {
        font-size: 16px;
        color: black;
    }
    </style>
    """ 


def create_custom_markdown_card(text, image_url=None):
    # Apply custom CSS styles to the card
    st.markdown(custom_css, unsafe_allow_html=True)
    
    # Create the card
    st.markdown(
        """
        <div class="card" style="display: flex; align-items: center;">
            <div style="flex: 1;">
                <div class="card-title">Информация</div>
                <div class="card-content">
                """
        + text
        + """
                </div>
            </div>
            """
        # Add the image if URL is provided
        + (f'<img src="{image_url}" style="max-width:100%; border-radius: 5px; flex-shrink: 0; margin-left: 20px;">' if image_url else '')
        + """
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.write("")
    st.write("")

def create_basic_custom_markdown_card(text, image_url=None):
    # Apply custom CSS styles to the card
    st.markdown(custom_css, unsafe_allow_html=True)
    
    text_lines = text.split('\n')

    formatted_text = '<br>'.join(text_lines)
    
    # Create the card
    st.markdown(
        """
        <div class="card" style="display: flex; align-items: center;">
            <div style="flex: 1;">
                <div class="card-content">
                """
        + formatted_text
        + """
                </div>
            </div>
            """
        # Add the image if URL is provided
        + (f'<img src="{image_url}" style="max-width:100%; border-radius: 5px; flex-shrink: 0; margin-left: 20px;">' if image_url else '')
        + """
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.write("")
    st.write("")

def init_session_state():
    if 'data' not in st.session_state:
        st.session_state.data = True
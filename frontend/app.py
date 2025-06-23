import streamlit as st
import base64
from add_update import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab


def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read())

    # Get file extension to set correct MIME type
    file_extension = image_file.split('.')[-1].lower()
    if file_extension in ['jpg', 'jpeg']:
        mime_type = 'jpeg'
    elif file_extension == 'png':
        mime_type = 'png'
    elif file_extension == 'webp':
        mime_type = 'webp'
    else:
        mime_type = 'jpeg'  # default fallback

    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{mime_type};base64,{encoded_string.decode()});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Make content more readable with semi-transparent background */
    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}

    /* Style the title */
    h1 {{
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }}

    /* Style the tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        justify-content: center;
    }}

    .stTabs [data-baseweb="tab"] {{
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 8px;
        padding: 8px 16px;
        border: 1px solid rgba(0, 0, 0, 0.1);
        font-weight: 500;
        transition: all 0.3s ease;
    }}

    .stTabs [data-baseweb="tab"]:hover {{
        background-color: rgba(52, 152, 219, 0.3);
        transform: translateY(-1px);
    }}

    .stTabs [aria-selected="true"] {{
        background-color: rgba(52, 152, 219, 0.8) !important;
        color: white !important;
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


# Add background image
try:
    add_bg_from_local('images/bg.jpg')
except FileNotFoundError:
    st.warning("Background image 'bg.jpg' not found. Please ensure the image file is in the same directory as app.py")

st.title("Expense Tracking App for Hostel Students")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()
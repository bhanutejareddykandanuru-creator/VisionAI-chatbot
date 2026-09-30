import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Vision AI",
    page_icon="",
    layout="wide"  # replaces deprecated _container_width
)

# --- Custom CSS to move content to top ---
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0rem;  /* moves content to top */
        }
        .custom-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-top: 20px;   /* space above image */
            margin-bottom: 20px;/* space below image */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.title("Vision AI")

# --- Display Image ---
# You can adjust width to resize the image
st.image("images/image.png.png", width=600, caption="Vision AI Model")

# --- Move or Align Image (alternative HTML method) ---
# Centered image example:
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='images/image.png.png' width='500'>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Description ---
st.write("Welcome to your Vision AI app! This interface displays your model image and allows layout customization.")

import streamlit as st
import openai

# Set the page config at the beginning of the script
st.set_page_config(page_title="Scientific Article Summarizer", layout="wide")

# Configure the OpenAI API key
openai.api_key = "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"

# Function to generate the summary
def generate_summary(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please provide a summary of the following scientific article:\n\n{text}",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary = response.choices[0].text.strip()
    return summary

# Custom CSS for styling
def custom_css():
    st.markdown("""
    <style>
        .reportview-container {
            background-color: #F2F2F2;
        }
        .sidebar .sidebar-content {
            background-color: #F2F2F2;
        }
        h1 {
            color: #3C3C3C;
        }
        .stButton>button {
            background-color: #1E88E5;
            color: white;
        }
        .stButton>button:hover {
            background-color: #0D47A1;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

custom_css()

# Main app interface
st.title("Scientific Article Summarizer")

# Input fields
with st.form("summarizer_form"):
    st.markdown("Paste the key points of the scientific article or separate sentences here, each separated by a comma:")
    article_input = st.text_input("")
    article = [x.strip() for x in article_input.split(",")]
    submit_button = st.form_submit_button("Generate Summary")

if submit_button and article:
    article_text = " ".join(article)
    summary = generate_summary(article_text)
    st.subheader("Summary:")
    st.write(summary)

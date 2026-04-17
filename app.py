import sys
import os

# Fix paths (important for Streamlit Cloud)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "model "))  # ⚠️ space wala folder
sys.path.append(os.path.join(BASE_DIR, "utils"))

import streamlit as st
from PIL import Image

# Direct imports (no model. / utils.)
from blip import get_caption
from llm import ask_llama
from prompt import build_prompt


st.set_page_config(page_title="Multimodal AI Agent")

st.title("🧠 Multimodal AI Agent")
st.write("Upload an image and ask a question")

text = st.text_input("Enter your question:")
image = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if st.button("Analyze"):
    if text and image:
        img = Image.open(image)

        with st.spinner("Processing..."):
            caption = get_caption(img)
            prompt = build_prompt(text, caption)
            response = ask_llama(prompt)

        st.subheader("📸 Image Caption:")
        st.write(caption)

        st.subheader("💬 AI Response:")
        st.write(response)

    else:
        st.warning("Please provide both text and image!")

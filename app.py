# app.py

import streamlit as st
from groq_api.tools import generate_caption, generate_poetic_story
from PIL import Image
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="MyHeartAI - Scrapbook Generator", layout="centered")

st.title("💖 MyHeartAI: The Digital Scrapbook")
st.markdown("""Turn your memories into a poetic, heartfelt digital scrapbook using AI. Built for the world. Dedicated to the one who made me believe in love. """)

# User inputs
uploaded_image = st.file_uploader("📸 Upload a memory photo", type=["jpg", "jpeg", "png"])
memory_text = st.text_area("💭 Write a short memory or moment you shared (1–3 lines)", max_chars=300)

if st.button("✨ Generate MyHeart Scrapbook") and uploaded_image and memory_text:
    with st.spinner("Crafting your poetic memory..."):
        # Load and display the image
        image = Image.open(uploaded_image)
        st.image(image, caption="Your Uploaded Photo", use_column_width=True)

        # Save image to disk temporarily
        image_path = "temp_uploaded_image.png"
        image.save(image_path)

        # Generate caption and poetic story
        caption = generate_caption("A heartfelt photo of a couple in love. Write a poetic caption.")
        poetic_story = generate_poetic_story(memory_text)

        # Display results in Streamlit
        st.markdown("### 📜 Poetic Caption")
        st.write(f"_{caption}_")

        st.markdown("### 💌 AI-Love Story")
        st.write(poetic_story)

        # Export to PDF using reportlab
        pdf_path = "MyHeartAI_Scrapbook.pdf"
        doc = SimpleDocTemplate(pdf_path, pagesize=A4)
        styles = getSampleStyleSheet()
        normal_style = styles["Normal"]
        poetic_style = ParagraphStyle("Poetic", parent=normal_style, leading=18)

        story = []

        # Add image
        story.append(RLImage(image_path, width=400, height=300))
        story.append(Spacer(1, 20))

        # Add short memory
        story.append(Paragraph(f"<b>Memory:</b> {memory_text}", normal_style))
        story.append(Spacer(1, 12))

        # Add poetic caption
        story.append(Paragraph(f"<b>Caption:</b> {caption}", poetic_style))
        story.append(Spacer(1, 12))

        # Add poetic love story
        story.append(Paragraph(f"<b>Poetic Love Story:</b><br/>{poetic_story}", poetic_style))
        story.append(Spacer(1, 12))

        doc.build(story)

        # Show download
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📄 Download Your Scrapbook (PDF)",
                data=f,
                file_name="MyHeartAI_Scrapbook.pdf",
                mime="application/pdf"
            )

        # Clean up
        os.remove(image_path)
        os.remove(pdf_path)

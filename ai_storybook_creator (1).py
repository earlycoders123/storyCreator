import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import os

st.set_page_config(page_title="AI Storybook Cover Creator", layout="centered")
st.title("📖 AI Storybook Cover Creator")

# Character, mood, and theme options
characters = ["Dragon", "Robot", "Princess", "Astronaut", "Talking Cat", "Alien", "Knight"]
moods = ["Happy", "Mysterious", "Adventurous", "Scary", "Magical"]
themes = ["Space", "Forest", "Ocean", "Castle", "Desert", "Underwater"]

# User input
character = st.selectbox("Choose a main character:", characters)
mood = st.selectbox("Choose a mood:", moods)
theme = st.selectbox("Choose a story theme:", themes)

if st.button("🎨 Create Storybook Cover"):
    title = f"The {mood} {character} of the {theme}"
    st.subheader("📘 Storybook Title: " + title)

    # Generate a mock book cover image
    img = Image.new("RGB", (600, 800), color="white")
    draw = ImageDraw.Draw(img)

    # Load default font
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    if not os.path.exists(font_path):  # fallback
        font_path = None

    title_font = ImageFont.truetype(font_path, 40) if font_path else None
    sub_font = ImageFont.truetype(font_path, 24) if font_path else None

    # Draw title and character
    draw.text((50, 100), "STORYBOOK COVER", fill="darkblue", font=title_font)
    draw.text((50, 250), f"Title: {title}", fill="black", font=sub_font)
    draw.text((50, 350), f"Featuring a {character}", fill="gray", font=sub_font)
    draw.text((50, 400), f"Theme: {theme}", fill="gray", font=sub_font)
    draw.text((50, 450), f"Mood: {mood}", fill="gray", font=sub_font)

    st.image(img, caption="🖼️ Your AI-generated storybook cover!", use_column_width=True)

    # Optional: Save the image for download
    img.save("storybook_cover.png")
    with open("storybook_cover.png", "rb") as f:
        st.download_button("⬇️ Download Cover Image", f, file_name="storybook_cover.png")

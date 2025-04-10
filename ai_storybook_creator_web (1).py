
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

st.set_page_config(page_title="AI Storybook Cover Creator", layout="centered")
st.title("📚 AI Storybook Cover Creator")

characters = ["Dragon", "Princess", "Robot", "Unicorn", "Pirate"]
moods = ["Happy", "Scary", "Magical", "Funny"]
themes = ["Space", "Forest", "Ocean", "Castle"]

character = st.selectbox("Pick a Character:", characters)
mood = st.selectbox("Pick a Mood:", moods)
theme = st.selectbox("Pick a Theme:", themes)

theme_backgrounds = {
    "Space": "https://images.unsplash.com/photo-1477201221805-fb3a7dff03ee",
    "Forest": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "Ocean": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "Castle": "https://images.unsplash.com/photo-1549921296-3a70d82b5b9d"
}

if st.button("✨ Create My Book Cover"):
    title = f"The {mood} {character} in the {theme}"

    bg_url = theme_backgrounds[theme]
    response = requests.get(bg_url)
    bg_image = Image.open(BytesIO(response.content)).convert("RGB")
    bg_image = bg_image.resize((600, 800))

    draw = ImageDraw.Draw(bg_image)
    draw.rectangle((0, 20, 600, 120), fill="white")
    draw.text((30, 50), title, fill="black")

    st.image(bg_image, caption="Your Book Cover", use_column_width=True)
    bg_image.save("storybook_cover_web.png")

    with open("storybook_cover_web.png", "rb") as file:
        st.download_button("📥 Download Cover", file, "storybook_cover_web.png")

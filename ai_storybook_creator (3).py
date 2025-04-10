
import streamlit as st
from PIL import Image, ImageDraw
import random

# 🎨 App setup
st.set_page_config(page_title="Storybook Cover Creator", layout="centered")
st.title("📚 AI Storybook Cover Creator")

# 🎭 Choices for kids
characters = ["Dragon", "Princess", "Robot", "Unicorn", "Pirate"]
moods = ["Happy", "Scary", "Magical", "Funny"]
themes = ["Space", "Forest", "Ocean", "Castle"]

# ✏️ Select boxes
character = st.selectbox("Pick a Character:", characters)
mood = st.selectbox("Pick a Mood:", moods)
theme = st.selectbox("Pick a Theme:", themes)

if st.button("✨ Create My Book Cover"):
    title = f"The {mood} {character} in the {theme}"

    # 🖼️ Make a picture
    width, height = 600, 800
    bg_colors = {
        "Space": "midnightblue",
        "Forest": "green",
        "Ocean": "teal",
        "Castle": "gray"
    }
    img = Image.new("RGB", (width, height), color=bg_colors.get(theme, "white"))
    draw = ImageDraw.Draw(img)

    # 🌟 Draw simple scene
    if theme == "Space":
        for _ in range(30):
            x, y = random.randint(0, width), random.randint(0, height)
            draw.ellipse((x, y, x+5, y+5), fill="white")
    elif theme == "Forest":
        for _ in range(5):
            x = random.randint(50, width - 50)
            draw.rectangle((x, height - 100, x + 10, height), fill="brown")
            draw.ellipse((x - 20, height - 150, x + 30, height - 70), fill="limegreen")
    elif theme == "Ocean":
        for y in range(700, 800, 15):
            draw.arc((0, y, width, y + 30), 0, 180, fill="white")
    elif theme == "Castle":
        draw.rectangle((150, 500, 450, 750), fill="lightgray")
        draw.polygon([(200, 500), (275, 420), (350, 500)], fill="darkgray")

    # 📝 Add title text
    draw.rectangle((20, 20, 580, 100), fill="white")
    draw.text((30, 40), title, fill="black")

    # 📸 Show image
    st.image(img, caption="Your Book Cover", use_column_width=True)

    # 💾 Save and download
    img.save("storybook_cover.png")
    with open("storybook_cover.png", "rb") as file:
        st.download_button("📥 Download Book Cover", file, "storybook_cover.png")

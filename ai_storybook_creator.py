import streamlit as st
import random

st.set_page_config(page_title="📚 AI Storybook Cover Creator", layout="centered")

st.title("📖 AI Storybook Cover Creator")
st.write("✨ Pick your favorite characters, mood, and theme — let the AI create your storybook title and cover!")

characters = st.multiselect("🧚 Choose characters:", [
    "Dragon", "Unicorn", "Pirate", "Robot", "Fairy", "Astronaut",
    "Detective", "Witch", "Knight", "Alien"
])

mood = st.selectbox("🎭 Choose the story mood:", [
    "Funny", "Spooky", "Magical", "Adventurous", "Mysterious", "Happy", "Brave"
])

theme = st.selectbox("🌍 Choose a theme:", [
    "In Space", "Underwater", "In a Magical Forest",
    "On a Treasure Hunt", "In the Future", "In a Haunted House"
])

if st.button("✨ Generate Storybook Title and Cover"):
    if not characters:
        st.warning("Please choose at least one character.")
    else:
        title_adjectives = {
            "Funny": ["Hilarious", "Wacky", "Silly"],
            "Spooky": ["Haunted", "Creepy", "Ghostly"],
            "Magical": ["Enchanted", "Mystical", "Magical"],
            "Adventurous": ["Epic", "Brave", "Fearless"],
            "Mysterious": ["Secret", "Hidden", "Unknown"],
            "Happy": ["Joyful", "Cheerful", "Sunny"],
            "Brave": ["Heroic", "Bold", "Valiant"]
        }

        adjective = random.choice(title_adjectives[mood])
        char = random.choice(characters)
        title = f"The {adjective} {char} {theme}"

        st.subheader("📘 Your Storybook Title:")
        st.success(title)

        st.subheader("🎨 Your Cover Preview:")
        st.write(f"Imagine a beautiful cover with a {char.lower()} in a scene {theme.lower()}, feeling very {mood.lower()}!")
        st.image("https://cdn.pixabay.com/photo/2016/03/31/20/11/book-1294065_1280.png",
                 caption="Mock Storybook Cover", use_column_width=True)
import streamlit as st
from deep_translator import GoogleTranslator
import pyttsx3  # Optional: for text-to-speech

# App title
st.title("🌍 Language Translator Tool")

# Text input
text = st.text_area("Enter text to translate:")

# Language options
languages = ['english', 'hindi', 'marathi', 'french', 'german', 'spanish', 'japanese', 'chinese']

# Select source and target languages
source_lang = st.selectbox("Select source language", languages)
target_lang = st.selectbox("Select target language", languages)

# Translate button
if st.button("Translate"):
    try:
        # Perform translation
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        
        # Display result
        st.success(f"Translated Text: {translated}")
        
        # Optional: Speak translated text
        if st.button("🔊 Speak Translation"):
            engine = pyttsx3.init()
            engine.say(translated)
            engine.runAndWait()
    
    except Exception as e:
        st.error("⚠️ Translation failed. Please check the input or try again.")

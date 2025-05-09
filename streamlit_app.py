import streamlit as st
import openai

# OpenAI API key
openai.api_key = "JOUW_API_KEY_HIER"  # Vul hier je eigen API Key in

st.title("Viral Video Generator")

youtube_link = st.text_input("Plak hier je YouTube link:")

if st.button("Genereer viral clip!"):
    if youtube_link:
        with st.spinner("AI is bezig..."):
            prompt = f"Genereer een virale tekst en hashtags voor deze YouTube video: {youtube_link}"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response['choices'][0]['message']['content']
            st.success("Klaar!")
            st.write(result)
    else:
        st.error("Voer eerst een YouTube link in!")

import streamlit as st
import openai

# Zet hier je API key
client = openai.OpenAI(api_key=st.secrets["openai_api_key"])

st.title("Virale Video Generator")
st.write("Plak hier je YouTube link en ik genereer virale hashtags en tekst voor je!")

# Inputveld voor YouTube link
video_link = st.text_input("Plak je video link hier:")

if st.button("Genereer"):
    if video_link:
        with st.spinner("AI is aan het denken..."):
            # Prompt voor AI
            prompt = f"Genereer een virale tekst en hashtags voor deze video link: {video_link}"
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            
            result = response.choices[0].message.content
            st.success("Gegenereerd!")
            st.write(result)
    else:
        st.error("Plak eerst een video link!")
import requests
import streamlit as st


st.image("https://imgur.com/SmktDIH.png")
st.title("Song Lyrics")
  

singer = st.text_input("Digite o nome do cantor/banda: ", key="singer")
song = st.text_input("Digite o nome da música: ", key="song")
search = st.button("Pesquisar", key="search")

endpoint = f"https://api.lyrics.ovh/v1/{singer}/{song}"

response = requests.get(endpoint)


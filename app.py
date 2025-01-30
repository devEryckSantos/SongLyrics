import requests
import streamlit as st


# buscador
def search_lyrics(singer, song):
    endpoint = f"https://api.lyrics.ovh/v1/{singer}/{song}"

    # requisição
    response = requests.get(endpoint)

    # retorna a letra apenas se encontrá-la, do contrário, strign vazia
    lyrics = response.json()["lyrics"] if response.status_code == 200 else ""

    return lyrics


st.image("https://imgur.com/SmktDIH.png")
st.title("Song Lyrics")


singer = st.text_input("Digite o nome do cantor/banda: ", key="singer")
song = st.text_input("Digite o nome da música: ", key="song")
search = st.button("Pesquisar", key="search")

endpoint = f"https://api.lyrics.ovh/v1/{singer}/{song}"

response = requests.get(endpoint)

if search:
    lyrics = search_lyrics(singer, song)
    if lyrics:
        st.success("Encontramos a letra da sua música!")
        st.text(lyrics)
    else:
        st.error("Infelizmente não conseguimos encontrar a letra dessa música.")

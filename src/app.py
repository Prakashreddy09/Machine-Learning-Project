import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(music_title):
    url = "https://saavn.dev/api/search/songs"
    querystring = {"query":music_title}
    response = requests.get(url, params=querystring)
    data = response.json()
    return data['data']['results'][0]['image'][2]['url']

def recommend(musics,music: pd.DataFrame):
    music_index = music[music["title"] == musics].index[0]
    distances = similarity[music_index]
    music_list =  sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommend_music = []
    recommend_music_poster = []
    for musics in music_list:
        music_title = music.iloc[musics[0]].title
        recommend_music.append(music_title)
        recommend_music_poster.append(fetch_poster(music_title))
    # print(recommend_music)
    # print(recommend_music_poster)
    return recommend_music, recommend_music_poster


music_dict = pickle.load(open(r'musicrec.pkl', 'rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open(r'similarities.pkl', 'rb'))
st.title('Music Recommender System')


selected_music_name  = st.selectbox('Select a music you like ', music['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_music_name, music)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

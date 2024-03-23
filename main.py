# Import
import streamlit as st
from pydub import AudioSegment
from pydub.playback import play

# Def
def play_wav(path):
    song = AudioSegment.from_wav(path)
    play(song)  

# 테스트용 버튼
if st.button('audio test A'):
    # 버튼이 눌렸을 때 소리 재생
    play_wav('static/sound/piano_a.wav')

    # 테스트용 버튼
if st.button('audio test B'):
    # 버튼이 눌렸을 때 소리 재생
    play_wav('static/sound/piano_b.wav')





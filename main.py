# Import
import streamlit as st
from pydub import AudioSegment
from pydub.playback import play

# 상수 정의
PIANO_WHITE_KEYS = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
PIANO_BLACK_KEYS = ['C#', 'D#', 'F#', 'G#', 'A#']

STYLE = '''<style>
button {
    height: 20px;
    width: 30px
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    background-color: rgb(0, 0, 0);
    opacity: 0.8;
    display:inline-block;
}
</style>'''

# 함수 정의
def play_mp3(path):
    mp3 = AudioSegment.from_mp3(path)
    play(mp3)  

st.markdown(STYLE, unsafe_allow_html=True,)

# 테스트용 버튼
for key in PIANO_WHITE_KEYS:
    if st.button(key):
        # 버튼이 눌렸을 때 소리 재생
        play_mp3(f'static/sound/piano_{key.lower()}.wav')

for key in PIANO_BLACK_KEYS:
    if st.button(key):
        # 버튼이 눌렸을 때 소리 재생
        play_mp3(f'static/sound/piano_{key.lower()}.wav')
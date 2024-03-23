# Import
import streamlit as st
from pydub import AudioSegment
from pydub.playback import play

# 상수 정의
PIANO_KEYS = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# 함수 정의
def play_wav(path):
    song = AudioSegment.from_wav(path)
    play(song)  

st.markdown(
    """
<style>
button {
    height: 100px;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# 테스트용 버튼
for key in PIANO_KEYS:
    if st.button(key):
        # 버튼이 눌렸을 때 소리 재생
        play_wav(f'static/sound/piano_{key.lower()}.wav')
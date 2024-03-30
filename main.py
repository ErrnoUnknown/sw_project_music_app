# streamlit run c:\Users\DICCE\Desktop\sw_project_music_app\main.py

# Import
import streamlit as st
from pydub import AudioSegment
from pydub.playback import play
import mido

# 상수 정의
PIANO_KEYS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
KEY_TO_NOTE = {}

for index in range(12):
    KEY_TO_NOTE[PIANO_KEYS[index]] = index + 60

# 함수 정의
def play_mp3(path):
    mp3 = AudioSegment.from_mp3(path)
    play(mp3)

def record_note(note, time):
    global music_track

    music_track.append(
        'note_on',
        note=note,
        velocity=64,
        time=time
    )

    music_track.append(
        'note_off',
        note=note,
        velocity=64,
        time=time + 0.25
    )

# 메인
mid = mido.MidiFile()
music_track = mido.MidiTrack()
mid.tracks.append(music_track)

for key in PIANO_KEYS:
    if st.button(key):
        # 버튼이 눌렸을 때 소리 재생
        play_mp3(f'static/sound/piano_{key.lower()}.wav')
        record_note(record_note(KEY_TO_NOTE), 0)
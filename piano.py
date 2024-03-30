# streamlit run c:\Users\DICCE\Desktop\sw_project_music_app\piano.py

# Import
import threading as th
from datetime import datetime
import streamlit as st
from pydub import AudioSegment
from pydub.playback import play
from mido import Message, MidiFile, MidiTrack

# 상수 정의
PIANO_KEYS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
KEY_TO_NOTE = {}

for index in range(12):
    KEY_TO_NOTE[PIANO_KEYS[index]] = index + 60

# 함수 정의
def play_mp3(path):
    mp3 = AudioSegment.from_mp3(path)
    play(mp3)

def start_recording():
    with open('temp/start_time.txt', 'w') as file:
        file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def record_note(note, time):
    global start_time, music_track

    music_track.append(Message(
        'note_on',
        note=note,
        velocity=64,
        time=time
    ))

    music_track.append(Message(
        'note_off',
        note=note,
        velocity=64,
        time=time + 1000
    ))

def note_handler():
    global note_queue

    start_time = datetime.now()

    while True:
        if note_queue:
            note = note_queue.pop()

            time_delta = (datetime.now() - start_time).total_seconds()

            record_note(note, time_delta)
            print(note, time_delta)

# 메인
mid = MidiFile()
music_track = MidiTrack()
mid.tracks.append(music_track)

note_queue = []

thread_note_handle = th.Thread(target=note_handler)
thread_note_handle.start()

if st.button('녹음하기'):
    # 버튼이 눌렸을 때 시작 시간 설정
    start_recording()

if st.button('저장하기'):
    # 버튼이 눌렸을 때 파일 저장
    mid.save('temp/output.mid')

for key in PIANO_KEYS:
    if st.button(key):
        # 버튼이 눌렸을 때 소리 재생
        note_queue.append(KEY_TO_NOTE[key])
        play_mp3(f'static/sound/piano_{key.lower()}.wav')
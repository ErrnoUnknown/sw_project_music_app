# 모듈 가져오기
from pydub import AudioSegment
from pydub.playback import play

# 함수 정의
def play_wav(path):
    audio = AudioSegment.from_wav(path)
    play(audio)

# Piano
def play_piano_c(event):
    play_wav('static/sound/piano_c.wav')

def play_piano_c_sharp(event):
    play_wav('static/sound/piano_c#.wav')

def play_piano_d(event):
    play_wav('static/sound/piano_d.wav')

def play_piano_d_sharp(event):
    play_wav('static/sound/piano_d#.wav')

def play_piano_e(event):
    play_wav('static/sound/piano_e.wav')

def play_piano_f(event):
    play_wav('static/sound/piano_f.wav')

def play_piano_f_sharp(event):
    play_wav('static/sound/piano_f#.wav')

def play_piano_g(event):
    play_wav('static/sound/piano_g.wav')

def play_piano_g_sharp(event):
    play_wav('static/sound/piano_g#.wav')

def play_piano_a(event):
    play_wav('static/sound/piano_a.wav')

def play_piano_a_sharp(event):
    play_wav('static/sound/piano_a#.wav')

def play_piano_b(event):
    play_wav('static/sound/piano_b.wav')
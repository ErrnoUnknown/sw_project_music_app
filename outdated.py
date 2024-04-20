# 모듈 가져오기
import flet as ft
from pydub import AudioSegment
from pydub.playback import play

# 함수 정의
def play_wav(path):
    audio = AudioSegment.from_wav(path)
    play(audio) 

# 홈 페이지
def main(page: ft.Page):
    # 버튼 이벤트 함수 정의
    def route_to_home(event):
        route_change('/home')
    
    def route_to_login(event):
        route_change('/login')
    
    def route_to_signup(event):
        route_change('/signup')

    def route_to_app_piano(event):
        route_change('/app/piano')

    # 라우팅 함수 정의
    def route_change(route):
        # 페이지 초기화
        page.views.clear()

        # 네비게이션 바 정의
        nav_bar_home = [
                ft.FilledButton(text='App', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_app_piano),
                ft.FilledButton(text='Login', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_login),
                ft.FilledButton(text='Signup', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_signup)
            ]
        
        nav_bar_signup = [
                ft.FilledButton(text='Home', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_home),
                ft.FilledButton(text='App', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_app_piano),
                ft.FilledButton(text='Login', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_login)
            ]
        
        nav_bar_app = [
                ft.FilledButton(text='Home', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_home),
                ft.FilledButton(text='Login', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_login),
                ft.FilledButton(text='Signup', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_signup)
            ]

        # 홈
        if route == '/home':
            page.title = 'Welcome to Orchestra Maker'
            view_contents = [
                # 네비게이션 바
                ft.Row(nav_bar_home, alignment=ft.alignment.top_left),

                # Welcome to 텍스트
                ft.Divider(height=100, color='white'),
                ft.Row(
                    [
                        ft.Text(value='Welcome to', color='black', size=30)
                    ], alignment=ft.MainAxisAlignment.CENTER),

                # Orchestra Maker 로고
                ft.Row([
                        ft.Text(value='Orchestra Maker', color='red', size=50)
                    ], alignment=ft.MainAxisAlignment.CENTER),

                # The easiest way to be a composer! 텍스트
                ft.Row([
                        ft.Text(value='The easiest way to be a composer!', color='black', size=30)
                    ], alignment=ft.MainAxisAlignment.CENTER),

                # Try now! 버튼
                ft.Divider(height=20, color='white'),
                ft.Row(
                    [
                        ft.ElevatedButton(text='Try now!', on_click=route_to_signup, width=350, style=ft.ButtonStyle(bgcolor='red', color='white'))
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ]

        # 가입
        elif route == '/signup':
            page.title = 'Sign into Orchestra Maker'
            view_contents = [
                # 네비게이션 바
                ft.Row(nav_bar_signup, alignment=ft.alignment.top_left),

                # Sign into Orchestra Maker 텍스트
                ft.Divider(height=100, color='white'),
                ft.Row(
                    [
                        ft.Text(value='Sign into', color='black', size=30),
                        ft.Text(value='Orchestra Maker', color='red', size=50),
                    ], alignment=ft.MainAxisAlignment.CENTER),

                # 인풋 위젯
                ft.Divider(height=10, color='white'),
                ft.Row(
                    [
                    ft.Column(
                        [
                            ft.TextField(label='Username'),
                            ft.TextField(label='Password'),
                            ft.TextField(label='Confirm Password')
                        ], alignment=ft.MainAxisAlignment.CENTER, width=300)
                    ], alignment=ft.MainAxisAlignment.CENTER),

                # 가입 버튼
                ft.Divider(height=10, color='white'),
                ft.Row(
                    [
                        ft.FilledButton(text='Signin', style=ft.ButtonStyle(bgcolor='red', color='white'), on_click=route_to_app_piano),
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ]

        # 앱
        elif route[0:5] == '/app/':
            view_contents = [
                    # 네비게이션 바
                    ft.Row(nav_bar_app, alignment=ft.alignment.top_left),
                    ft.Divider(height=5, color='white')
                        ]
            
            # 피아노
            if route[5:] == 'piano':
                # 악기 이름
                inst_name = 'Piano'

                # 악기 UI
                page.title = f'Orchestra Maker | {inst_name}'
                view_contents += [
                    ft.Row(
                        [
                            ft.Text(value=inst_name, color='black', size=40)
                        ], alignment=ft.alignment.top_left, height=50)
                    ]

            # 악기 네비게이션 바
            view_contents = [ft.Row(
                [
                    ft.Column(
                        [
                            ft.FilledButton(text='Piano', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_app_piano, width=200),
                            ft.FilledButton(text='Elec Piano', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_app_piano, width=200)
                        ], width=200), view_contents[0]
                ], alignment=ft.alignment.top_left)]

        # 페이지 업데이트
        page.views.append(ft.View(route, view_contents, bgcolor=ft.colors.WHITE))
        page.update()

    route_change('/home')

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
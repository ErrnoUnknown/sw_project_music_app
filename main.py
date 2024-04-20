# 모듈 가져오기
import flet as ft
from module.play_inst import *

# 홈 페이지
def main(page: ft.Page):
    # 버튼 이벤트 함수 정의
    def route_to_home(event):
        route_change('/home')

    def route_to_app_piano(event):
        route_change('/app/piano')

    def route_to_app_elec_piano(event):
        route_change('/app/elec_piano')

    # 라우팅 함수 정의
    def route_change(route):
        # 페이지 초기화
        page.views.clear()

        # 네비게이션 바 정의
        nav_bar_home = [
                ft.FilledButton(text='App', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_app_piano)
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
                        ft.ElevatedButton(text='Try now!', on_click=route_to_app_piano, width=350, style=ft.ButtonStyle(bgcolor='red', color='white'))
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ]

        # 앱
        elif route[0:5] == '/app/':
            # 피아노
            if route[5:] == 'piano':
                # 악기 이름
                inst_name = 'Piano'
            
                # app_contents는 Column 안으로 들어감
                app_contents = [ft.OutlinedButton(text='C', on_click=play_piano_c, width=250, height=35, style=ft.ButtonStyle(bgcolor='white', color='black')),
                                ft.OutlinedButton(text='C#', on_click=play_piano_c_sharp, width=250, height=35, style=ft.ButtonStyle(bgcolor='black', color='white')),
                                ft.OutlinedButton(text='D', on_click=play_piano_d, width=250, height=35, style=ft.ButtonStyle(bgcolor='white', color='black')),
                                ft.OutlinedButton(text='D#', on_click=play_piano_d_sharp, width=250, height=35, style=ft.ButtonStyle(bgcolor='black', color='white')),
                                ft.OutlinedButton(text='E', on_click=play_piano_e, width=250, height=35, style=ft.ButtonStyle(bgcolor='white', color='black')),
                                ft.OutlinedButton(text='F', on_click=play_piano_f, width=250, height=35, style=ft.ButtonStyle(bgcolor='white', color='black')),
                                ft.OutlinedButton(text='F#', on_click=play_piano_f_sharp, width=250, height=35, style=ft.ButtonStyle(bgcolor='black', color='white')),
                                ft.OutlinedButton(text='G', on_click=play_piano_g, width=250, height=35, style=ft.ButtonStyle(bgcolor='white', color='black')),
                                ft.OutlinedButton(text='G#', on_click=play_piano_g_sharp, width=250, height=35, style=ft.ButtonStyle(bgcolor='black', color='white')),
                                ft.OutlinedButton(text='A', on_click=play_piano_a, width=250, height=35, style=ft.ButtonStyle(bgcolor='white', color='black')),
                                ft.OutlinedButton(text='A#', on_click=play_piano_a_sharp, width=250, height=35, style=ft.ButtonStyle(bgcolor='black', color='white')),
                                ft.OutlinedButton(text='B', on_click=play_piano_b, width=250, height=35, style=ft.ButtonStyle(bgcolor='white', color='black'))]
            elif route[5:] == 'elec_piano':
                # 악기 이름
                inst_name = 'Elec Piano'
            
                # app_contents는 Column 안으로 들어감
                app_contents = [ft.Text(value='eqeq', color='black', size=25),
                                ft.Text(value='rwwrw', color='black', size=25),
                                ft.Text(value='eqeqeqweeewewew', color='black', size=25)]

            # UI 구성
            view_contents = [ft.Row(
                [   
                    ft.Row([
                        ft.Column(
                            [
                                ft.FilledButton(text='Home', style=ft.ButtonStyle(bgcolor='red', color='white'), on_click=route_to_home, width=200),
                                ft.FilledButton(text='Piano', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_app_piano, width=200),
                                ft.FilledButton(text='Elec Piano', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=route_to_app_elec_piano, width=200)
                            ], alignment=ft.alignment.top_left)], height=1000),
                    ft.Row(width=80, height=1),
                    ft.Row([
                        ft.Column(
                            [
                                ft.Text(value=inst_name, color='black', size=45),
                                ft.Divider(height=15, color='white'),
                                ft.Column(app_contents, alignment=ft.alignment.top_left)
                            ])], height=1000)
                ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.MainAxisAlignment.START)]

            page.title = f'Orchestra Maker | {inst_name}'

        # 페이지 업데이트
        page.views.append(ft.View(route, view_contents, bgcolor=ft.colors.WHITE))
        page.update()

    route_change('/home')

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
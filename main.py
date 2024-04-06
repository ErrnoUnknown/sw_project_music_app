# 모듈 가져오기
import flet as ft

# 홈 페이지
def main(page: ft.Page):
    # 페이지 설정
    page.title = 'Welcome to Orchestra Maker'

    # 버튼 이벤트 정의
    def on_app_btn_click(event):
        raise NotImplementedError

    def on_home_btn_click(event):
        route_change('/home')
    
    def on_login_btn_click(event):
        raise NotImplementedError
    
    def on_signup_btn_click(event):
        route_change('/signup')

    def on_trynow_btn_click(event):
        raise NotImplementedError

    # 라우팅 함수 정의
    def route_change(route):
        page.views.clear()
        
        nav_bar = ft.Row([
                ft.FilledButton(text='Home', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=on_home_btn_click),
                ft.FilledButton(text='App', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=on_app_btn_click),
                ft.FilledButton(text='Login', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=on_login_btn_click),
                ft.FilledButton(text='Signup', style=ft.ButtonStyle(bgcolor='black', color='white'), on_click=on_signup_btn_click),
            ], alignment=ft.alignment.top_left)
        
        if route == '/home':
            page.views.append(
            ft.View(
                '/home',
                [
                    nav_bar,
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

                    # Try now 버튼
                    ft.Divider(height=10, color='white'),
                    ft.Row(
                        [
                            ft.FilledButton(text='Try now', style=ft.ButtonStyle(bgcolor='red', color='white'), on_click=on_trynow_btn_click),
                        ], alignment=ft.MainAxisAlignment.CENTER)
                ]))
        elif route == '/signup':
            page.views.append(
            ft.View(
                '/signup',
                [
                    nav_bar,
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

                    # Try now 버튼
                    ft.Divider(height=10, color='white'),
                    ft.Row(
                        [
                            ft.FilledButton(text='Signin', style=ft.ButtonStyle(bgcolor='red', color='white'), on_click=on_trynow_btn_click),
                        ], alignment=ft.MainAxisAlignment.CENTER)
                ]))
            
        # 페이지 업데이트
        page.update()

    route_change('/home')

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
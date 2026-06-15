import flet as ft
# --- INJECTED DYNAMIC ASSETS HELPERS ---
import os
import flet as ft

FALLBACK_PROFILE = ['profile.avif']
FALLBACK_GITHUB = ['all_branches.png', 'my_branch.png']
FALLBACK_VIDEO = ['contribution-video.mp4']

def get_profile_pic():
    try:
        p = os.path.join(os.path.dirname(__file__), "assets", "pictures", "profile")
        if os.path.exists(p):
            files = [f for f in os.listdir(p) if f.lower() not in ["tokens.txt", "token.txt", "gittoken.txt"]]
            files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.avif'))]
            if files:
                return f"/pictures/profile/{files[0]}"
    except Exception:
        pass
    return f"/pictures/profile/{FALLBACK_PROFILE[0]}" if FALLBACK_PROFILE else None

def get_github_evidence():
    try:
        p = os.path.join(os.path.dirname(__file__), "assets", "pictures", "github")
        if os.path.exists(p):
            files = [f for f in os.listdir(p) if f.lower() not in ["tokens.txt", "token.txt", "gittoken.txt"]]
            files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
            if files:
                return [f"/pictures/github/{f}" for f in files]
    except Exception:
        pass
    return [f"/pictures/github/{f}" for f in FALLBACK_GITHUB]

def get_contribution_video():
    try:
        p = os.path.join(os.path.dirname(__file__), "assets", "videos", "contribution-video")
        if os.path.exists(p):
            files = [f for f in os.listdir(p) if f.lower() not in ["tokens.txt", "token.txt", "gittoken.txt"]]
            files = [f for f in files if f.lower().endswith(('.mp4', '.mov', '.avi', '.mkv'))]
            if files:
                return f"/videos/contribution-video/{files[0]}"
    except Exception:
        pass
    return f"/videos/contribution-video/{FALLBACK_VIDEO[0]}" if FALLBACK_VIDEO else None

def get_video_control(page):
    video_src = get_contribution_video()
    if not video_src:
        return ft.Container()
    if hasattr(ft, "Video"):
        try:
            if hasattr(ft, "VideoMedia"):
                media = ft.VideoMedia(video_src)
                return ft.Video(playlist=[media], autoplay=False, aspect_ratio=16/9, expand=True)
            else:
                return ft.Video(src=video_src, autoplay=False, aspect_ratio=16/9, expand=True)
        except Exception:
            pass
    # Fallback to browser launch
    return ft.Column([
        ft.Text("Embedded video player requires a newer version of Flet.", size=11, color=MUTED),
        ft.ElevatedButton(
            "Play Video",
            icon=ft.Icons.PLAY_ARROW,
            on_click=lambda _: page.launch_url(video_src)
        )
    ], spacing=5, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
# --- END INJECTED DYNAMIC ASSETS HELPERS ---


BG = '#07101E'
SURFACE = '#101B2D'
TEXT = '#F8FBFF'
MUTED = '#A8B6CC'
ACCENT = '#25C7F7'
GOLD = '#D8A73E'
SUCCESS = '#49D28F'
BORDER = '#273A5D'


def chip(text, color=ACCENT):
    return ft.Container(
        padding=ft.padding.symmetric(horizontal=12, vertical=7),
        border_radius=18,
        bgcolor=color,
        content=ft.Text(text, size=12, weight=ft.FontWeight.BOLD, color=BG),
    )


def tile(title, children, accent=GOLD):
    return ft.Container(
        padding=22,
        border_radius=8,
        bgcolor=SURFACE,
        border=ft.border.all(1, BORDER),
        content=ft.Column([
            ft.Text(title, size=18, weight=ft.FontWeight.W_900, color=TEXT),
            ft.Container(width=54, height=3, bgcolor=accent, border_radius=4),
            *children,
        ], spacing=10),
    )


def main(page: ft.Page):
    page.title = "Hilma Shuumbwa - SiteSpy Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = BG
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0

    hero = ft.Container(
        padding=ft.padding.symmetric(horizontal=28, vertical=34),
        bgcolor=BG,
        content=ft.Column([
            ft.Image(src='assets/sitespy-wordmark.svg', width=190, fit=ft.ImageFit.CONTAIN),
            ft.Row([chip("Electronics and Computer"), chip("Backend/Firebase", GOLD)], wrap=True, spacing=10),
            ft.Text("Hilma Shuumbwa", size=34, weight=ft.FontWeight.W_900, color=TEXT),
            ft.Text("GitHub: hilma-shuumbwa | Email: shuumbwahilma@gmail.com", color=MUTED, selectable=True),
            ft.Text("Firebase configuration and Expo environment loading.", size=16, color=TEXT),
            ft.Text("GitHub profile: https://github.com/hilma-shuumbwa", color=GOLD, selectable=True),
        ], spacing=13),
    )

    page.add(
        hero,
        ft.Container(
            padding=28,
            content=ft.ResponsiveRow([
                ft.Container(tile('Profile', [
                    ft.Container(
                        content=ft.Image(
                            src=get_profile_pic(),
                            width=100,
                            height=100,
                            fit=ft.ImageFit.COVER if hasattr(ft, "ImageFit") else ft.BoxFit.COVER,
                            border_radius=50
                        ),
                        alignment=ft.alignment.Alignment(0, 0),
                        margin=ft.Margin.only(bottom=10)
                    ) if get_profile_pic() else ft.Container(),
                    ft.Text("Department: Electronics and Computer", color=TEXT),
                    ft.Text("Suggested role/area: Backend/Firebase", color=MUTED),
                    ft.Text("Match status: MATCHED - LIVE GITHUB USERNAME APPLIED", color=SUCCESS),
                ], ACCENT), col={'xs': 12, 'md': 6}),
                ft.Container(tile('Contribution Area', [
                    ft.Text("Firebase configuration and Expo environment loading.", color=TEXT),
                ]), col={'xs': 12, 'md': 6}),
                ft.Container(tile('Files / Validation Area', [
                    ft.Text('- src/services/firebaseConfig.js', color=MUTED, size=13),
                    ft.Text('- app.config.js', color=MUTED, size=13),
                    ft.Text('- .env.example', color=MUTED, size=13),
                ], ACCENT), col={'xs': 12, 'md': 6}),
                ft.Container(tile('Local Git Setup', [
                    ft.Text("git config user.name \"Hilma Shuumbwa\"\ngit config user.email \"shuumbwahilma@gmail.com\"\ngit config --get user.name\ngit config --get user.email", color=TEXT, selectable=True),
                ]), col={'xs': 12, 'md': 6}),
                ft.Container(tile('Clone, Commit, Push', [
                    ft.Text("git clone \"Replace with your own fork URL after creating the fork.\"\ncd \"Replace with your cloned repository folder\"\ngit status\ngit checkout -b portfolio/shuumbwa-hmn-sitespy-portfolio\ngit add README.md index.html main.py\ngit commit -m \"Update Hilma Shuumbwa SiteSpy portfolio\"\ngit push -u origin portfolio/shuumbwa-hmn-sitespy-portfolio", color=TEXT, selectable=True),
                ], SUCCESS), col={'xs': 12, 'md': 6}),
                ft.Container(tile('Evidence', [
                    ft.Text('GitHub Evidence:', color=MUTED, size=13),
                    ft.Column([
                        ft.Container(
                            content=ft.Column([
                                ft.Image(src=img, fit=ft.ImageFit.CONTAIN if hasattr(ft, "ImageFit") else ft.BoxFit.CONTAIN, border_radius=8),
                                ft.Text(img.split('/')[-1], size=11, color=MUTED)
                            ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            border=ft.Border.all(1, BORDER),
                            border_radius=8,
                            padding=10
                        ) for img in get_github_evidence()
                    ], spacing=10) if get_github_evidence() else ft.Text('No GitHub evidence found.', color=TEXT),
                ]), col={'xs': 12, 'md': 6}),
                ft.Container(tile('Individual Video', [
                    get_video_control(page) if get_contribution_video() else ft.Text('No contribution video found.', color=TEXT),
                ], SUCCESS), col={'xs': 12, 'md': 6}),
                ft.Container(tile('Handover Note', [
                    ft.Text('Use your own fork or portfolio repository. Do not claim commits or authorship that are not personally yours.', color=TEXT),
                ]), col={'xs': 12, 'md': 6}),
            ], spacing=16, run_spacing=16),
        ),
    )


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')

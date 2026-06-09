from kivy.uix.screenmanager import Screen

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.image import Image

from kivy.uix.button import Button

from kivy.graphics import (
    Color,
    RoundedRectangle
)

from kivymd.uix.label import MDLabel

from sounds.sound_manager import (
    play_click
)


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        # ====================================
        # BACKGROUND
        # ====================================

        bg = Image(

            source="assets/bg.jpg",

            allow_stretch=True,

            keep_ratio=False,

            size_hint=(1, 1),

            pos_hint={
                "x": 0,
                "y": 0
            }
        )

        layout.add_widget(bg)

        
        # ====================================
        # LOGO
        # ====================================

        logo = Image(

            source="assets/logo.png",

            size_hint=(0.42, 0.18),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.90
            }
        )

        layout.add_widget(logo)

        # ====================================
        # SUBTITLE
        # ====================================

        subtitle = MDLabel(

            text="50 LEVEL CHALLENGE",

            halign="center",

            theme_text_color="Custom",

            text_color=(0.8, 0.9, 1, 1),

            font_style="Title",

            pos_hint={
                "center_y": 0.56
            }
        )

        layout.add_widget(subtitle)

        # ====================================
        # START BUTTON
        # ====================================

        start_btn = Button(

            text="START GAME",

            font_size=20,

            bold=True,

            background_normal="",

            background_down="",

            background_color=(
                0.10,
                0.65,
                1,
                1
            ),

            color=(1, 1, 1, 1),

            size_hint=(0.62, 0.085),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.38
            }
        )

        start_btn.bind(
            on_release=self.start_game
        )

        layout.add_widget(start_btn)

        # ====================================
        # LEADERBOARD BUTTON
        # ====================================

        leader_btn = Button(

            text="LEADERBOARD",

            font_size=18,

            bold=True,

            background_normal="",

            background_down="",

            background_color=(
                1,
                0.3,
                0.6,
                1
            ),

            color=(1, 1, 1, 1),

            size_hint=(0.62, 0.085),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.25
            }
        )

        leader_btn.bind(
            on_release=self.open_leaderboard
        )

        layout.add_widget(leader_btn)

        # ====================================
        # FINAL ADD
        # ====================================

        self.add_widget(layout)

    # ====================================
    # START GAME
    # ====================================

    def start_game(self, *args):

        play_click()

        quiz = self.manager.get_screen(
            "quiz"
        )

        quiz.start_level()

        self.manager.current = "quiz"

    # ====================================
    # OPEN LEADERBOARD
    # ====================================

    def open_leaderboard(self, *args):

        play_click()

        leaderboard = self.manager.get_screen(
            "leaderboard"
        )

        leaderboard.refresh_scores()

        self.manager.current = "leaderboard"
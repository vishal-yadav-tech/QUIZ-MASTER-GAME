from kivy.uix.screenmanager import Screen

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.image import Image

from kivy.uix.button import Button

from kivy.graphics import (
    Color,
    RoundedRectangle
)

from kivymd.uix.label import MDLabel

from utils.leaderboard import (
    load_scores
)

from sounds.sound_manager import (
    play_click
)


class LeaderboardScreen(Screen):

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

            size_hint=(0.34, 0.16),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.92
            }
        )

        layout.add_widget(logo)

        # ====================================
        # TITLE
        # ====================================

        title = MDLabel(

            text="LEADERBOARD",

            halign="left",

            theme_text_color="Custom",

            text_color=(1, 1, 1, 1),

            font_style="Headline",

            pos_hint={
                "center_y": 0.80
            }
        )

        layout.add_widget(title)

        # ====================================
        # SCORE LABELS
        # ====================================

        self.score_labels = []

        y = 0.70

        for i in range(10):

            lbl = MDLabel(

                text="",

                halign="left",

                theme_text_color="Custom",

                text_color=(0.8, 0.95, 1, 1),

                font_style="Body",

                pos_hint={
                    "x": 0.15,
                    "center_y": y
                }
            )

            self.score_labels.append(lbl)

            layout.add_widget(lbl)

            y -= 0.055

        # ====================================
        # BACK BUTTON
        # ====================================

        back_btn = Button(

            text="BACK",

            size_hint=(None, None),

            size=(240, 55),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.09
            },

            background_normal="",

            background_color=(1, 0.35, 0.35, 1),

            color=(1, 1, 1, 1),

            font_size=18
        )

        back_btn.bind(
            on_release=self.go_home
        )

        layout.add_widget(back_btn)

        self.add_widget(layout)

    # ====================================
    # REFRESH SCORES
    # ====================================

    def refresh_scores(self):

        scores = load_scores()

        for i in range(10):

            if i < len(scores):

                item = scores[i]

                self.score_labels[i].text = (

                    f"{i + 1}.   "

                    f"{item['name']}"

                    f"   -   "

                    f"{item['score']}"
                )

            else:

                self.score_labels[i].text = ""

    # ====================================
    # GO HOME
    # ====================================

    def go_home(self, *args):

        play_click()

        self.manager.current = "home"
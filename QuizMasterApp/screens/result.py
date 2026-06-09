from kivy.uix.screenmanager import Screen

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.image import Image

from kivy.graphics import (
    Color,
    RoundedRectangle
)

from kivymd.uix.label import MDLabel

from kivy.uix.button import Button

from kivymd.uix.textfield import MDTextField

from utils.leaderboard import save_score

from utils.game_manager import (
    load_game_data,
    save_game_data
)

from sounds.sound_manager import (
    play_click
)


class ResultScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.final_score = 0

        layout = FloatLayout()

        # =====================================
        # BACKGROUND
        # =====================================

        bg = Image(

            source="assets/bg.jpg",

            allow_stretch=True,

            keep_ratio=False
        )

        layout.add_widget(bg)

       
        # =====================================
        # LOGO
        # =====================================

        logo = Image(

            source="assets/logo.png",

            size_hint=(0.42, 0.20),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.88
            }
        )

        layout.add_widget(logo)

        # =====================================
        # TITLE
        # =====================================

        self.title = MDLabel(

            text="ALL LEVELS COMPLETED!",

            halign="center",

            theme_text_color="Custom",

            text_color=(1, 1, 1, 1),

            font_style="Display",

            pos_hint={
                "center_y": 0.72
            }
        )

        layout.add_widget(self.title)

        # =====================================
        # SCORE
        # =====================================

        self.score_label = MDLabel(

            text="TOTAL SCORE : 0",

            halign="center",

            theme_text_color="Custom",

            text_color=(0.2, 1, 0.5, 1),

            font_style="Display",

            pos_hint={
                "center_y": 0.64
            }
        )

        layout.add_widget(
            self.score_label
        )

        # =====================================
        # NAME INPUT
        # =====================================

        self.name_input = MDTextField(

            hint_text="ENTER YOUR NAME",

            mode="outlined",

            size_hint=(0.75, 0.08),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.48
            }
        )

        layout.add_widget(
            self.name_input
        )

        # =====================================
        # SAVE BUTTON
        # =====================================

        save_btn = Button(

            text="SAVE SCORE",

            font_size=22,

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
                "center_y": 0.33
            }
        )

        save_btn.bind(
            on_release=self.save_final
        )

        layout.add_widget(save_btn)

        # =====================================
        # HOME BUTTON
        # =====================================

        home_btn = Button(

            text="BACK HOME",

            font_size=20,

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
                "center_y": 0.20
            }
        )

        home_btn.bind(
            on_release=self.back_home
        )

        layout.add_widget(home_btn)

        self.add_widget(layout)

    # =====================================
    # SET SCORE
    # =====================================

    def set_score(self, score):

        self.final_score = score

        self.score_label.text = (
            f"TOTAL SCORE : {score}"
        )

    # =====================================
    # SAVE SCORE
    # =====================================

    def save_final(self, *args):

        play_click()

        name = (
            self.name_input.text.strip()
        )

        if name == "":
            return

        save_score(
            name,
            self.final_score
        )

        data = load_game_data()

        data["current_level"] = 1

        save_game_data(data)

        self.title.text = (
            "SCORE SAVED!"
        )

    # =====================================
    # BACK HOME
    # =====================================

    def back_home(self, *args):

        play_click()

        self.manager.current = "home"
from kivy.uix.screenmanager import Screen

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.image import Image

from kivy.graphics import (
    Color,
    RoundedRectangle
)

from kivymd.uix.label import MDLabel

from kivy.uix.button import Button

from utils.game_manager import (
    get_level_questions,
    load_game_data,
    save_game_data
)

from sounds.sound_manager import (
    play_click,
    play_correct,
    play_wrong
)


class QuizScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.level = 1

        self.score = 0

        self.total_score = 0

        self.current_question = 0

        self.questions = []

        layout = FloatLayout()

        # ===================================
        # BACKGROUND
        # ===================================

        bg = Image(

            source="assets/bg.jpg",

            allow_stretch=True,

            keep_ratio=False
        )

        layout.add_widget(bg)

        
        # ===================================
        # LOGO
        # ===================================

        logo = Image(

            source="assets/logo.png",

            size_hint=(0.42, 0.20),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.93
            }
        )

        layout.add_widget(logo)

        # ===================================
        # LEVEL LABEL
        # ===================================

        self.level_label = MDLabel(

            text="LEVEL 1",

            halign="center",

            theme_text_color="Custom",

            text_color=(1, 1, 1, 1),

            font_style="Title",

            role="large",

            pos_hint={
                "center_y": 0.83
            }
        )

        layout.add_widget(self.level_label)

        # ===================================
        # QUESTION
        # ===================================

        self.question_label = MDLabel(

            text="QUESTION",

            halign="center",

            theme_text_color="Custom",

            text_color=(1, 1, 1, 1),

            font_style="Headline",

            role="small",

            size_hint=(0.8, 0.2),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.70
            }
        )

        layout.add_widget(self.question_label)

        # ===================================
        # SCORE
        # ===================================

        self.score_label = MDLabel(

            text="Score : 0",

            halign="center",

            theme_text_color="Custom",

            text_color=(0.7, 0.9, 1, 1),

            pos_hint={
                "center_y": 0.60
            }
        )

        layout.add_widget(self.score_label)

        # ===================================
        # OPTION BUTTONS
        # ===================================

        self.option_buttons = []

        y_positions = [
            0.47,
            0.36,
            0.25,
            0.14
        ]

        for i in range(4):

            btn = Button(

                text="OPTION",

                font_size=19,

                bold=True,

                background_normal="",

                background_down="",

                background_color=(
                    0,
                    1,
                    0,
                    1
                ),

                color=(1, 1, 1, 1),

                size_hint=(0.70, 0.08),

                pos_hint={
                    "center_x": 0.5,
                    "center_y": y_positions[i]
                }
            )

            btn.index = i

            btn.bind(
                on_release=self.check_answer
            )

            self.option_buttons.append(btn)

            layout.add_widget(btn)

        # ===================================
        # NEXT BUTTON
        # ===================================

        self.next_btn = Button(

            text="NEXT",

            font_size=22,

            bold=True,

            background_normal="",

            background_down="",

            background_color=(
                1,
                0,
                0,
                1
            ),

            color=(1, 1, 1, 1),

            size_hint=(0.50, 0.08),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.05
            },

            opacity=0,

            disabled=True
        )

        layout.add_widget(self.next_btn)

        self.next_btn.bind(
            on_release=self.next_question
        )


        self.add_widget(layout)

    
    def start_level(self):

        self.current_question = 0

        self.score = 0

        self.load_level()

        self.load_question()

    # ===================================
    # START QUIZ
    # ===================================

    def start_quiz(self):

        data = load_game_data()

        self.level = data["current_level"]

        self.total_score = 0

        self.load_level()

    # ===================================
    # LOAD LEVEL
    # ===================================

    def load_level(self):

        self.questions = get_level_questions(
            self.level
        )

        self.current_question = 0

        self.score = 0

        self.level_label.text = (
            f"LEVEL {self.level}"
        )

        self.load_question()

    # ===================================
    # LOAD QUESTION
    # ===================================

    def load_question(self):

        q = self.questions[
            self.current_question
        ]

        self.question_label.text = (
            q["question"]
        )

        self.score_label.text = (
            f"Score : {self.total_score}"
        )

        for i, btn in enumerate(
            self.option_buttons
        ):

            btn.text = q["options"][i]

            btn.disabled = False

            btn.background_color = (
                0.15,
                0.65,
                1,
                1
            )

        self.next_btn.opacity = 0

        self.next_btn.disabled = True

    # ===================================
    # CHECK ANSWER
    # ===================================

    def check_answer(self, instance):

        play_click()

        q = self.questions[
            self.current_question
        ]

        correct = q["answer"]

        selected = instance.index

        # DISABLE BUTTONS
        for btn in self.option_buttons:

            btn.disabled = True

        # WRONG
        if selected != correct:

            instance.background_color = (
                1,
                0.2,
                0.2,
                1
            )

            play_wrong()

        # CORRECT
        else:

            play_correct()

            self.score += 1

            self.total_score += 1

        # SHOW CORRECT ANSWER
        self.option_buttons[
            correct
        ].background_color = (

            0.2,
            0.85,
            0.3,
            1
        )

        # SHOW NEXT
        self.next_btn.opacity = 1

        self.next_btn.disabled = False

    # ===================================
    # NEXT QUESTION
    # ===================================

    def next_question(self, *args):

        self.current_question += 1

        # LEVEL COMPLETE
        if self.current_question >= len(
            self.questions
        ):

            self.level += 1

            # GAME COMPLETE
            if self.level > 50:

                result = self.manager.get_screen(
                    "result"
                )

                result.set_score(
                    self.total_score
                )

                self.manager.current = (
                    "result"
                )

                return

            # SAVE LEVEL
            data = load_game_data()

            data["current_level"] = (
                self.level
            )

            save_game_data(data)

            self.load_level()

            return

        self.load_question()
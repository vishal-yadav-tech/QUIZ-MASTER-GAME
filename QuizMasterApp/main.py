# MUSIC
from sounds.sound_manager import (
    play_bg_music
)

from kivy.core import window
from kivymd.app import MDApp

from kivy.core.window import Window

from kivy.uix.screenmanager import (
    ScreenManager,
    FadeTransition
)

# SCREENS
from screens.home import HomeScreen

from screens.quiz import QuizScreen

from screens.result import ResultScreen

from screens.leaderboard import (
    LeaderboardScreen
)


# WINDOW
Window.size = (400, 700)

window.resizable = False


class QuizApp(MDApp):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(
            HomeScreen(name="home")
        )

        sm.add_widget(
            QuizScreen(name="quiz")
        )

        sm.add_widget(
            ResultScreen(name="result")
        )

        sm.add_widget(
            LeaderboardScreen(name="leaderboard")
        )

        play_bg_music()
        
        return sm

QuizApp().run()
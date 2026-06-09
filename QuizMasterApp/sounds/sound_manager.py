from kivy.core.audio import SoundLoader

bg_music = SoundLoader.load(
    "sounds/bgmusic.wav"
)

click_sound = SoundLoader.load(
    "sounds/click.wav"
)

correct_sound = SoundLoader.load(
    "sounds/correct.wav"
)

wrong_sound = SoundLoader.load(
    "sounds/wrong.wav"
)

finish_sound = SoundLoader.load(
    "sounds/finish.wav"
)


def play_bg_music():

    if bg_music:

        bg_music.loop = True

        bg_music.volume = 1

        bg_music.play()


def play_click():

    if click_sound:

        click_sound.play()


def play_correct():

    if correct_sound:

        correct_sound.play()


def play_wrong():

    if wrong_sound:

        wrong_sound.play()


def play_finish():

    if finish_sound:

        finish_sound.play()
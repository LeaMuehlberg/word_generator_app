from wonderwords import RandomWord
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class WortGenerator:
    def __init__(self):
        self.generator = RandomWord()

    def zufallswort(self):
        return self.generator.word(
            include_parts_of_speech=["nouns"]
        )


class RandomWordApp(App):

    def build(self):
        self.wg = WortGenerator()

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        self.label = Label(
            text="Click the button",
            font_size=40
        )

        button = Button(
            text="New Word",
            font_size=30
        )

        button.bind(on_press=self.neues_wort)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def neues_wort(self, instance):
        self.label.text = self.wg.zufallswort()


if __name__ == "__main__":
    RandomWordApp().run()
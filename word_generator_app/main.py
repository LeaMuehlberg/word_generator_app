from wonderwords import RandomWord
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class WordGenerator:
    def __init__(self):
        self.generator = RandomWord()
    def random_word(self):
        return self.generator.word(
            include_parts_of_speech = ["nouns"]
        )
        
class RandomWordApp(App):
    def build(self):
        self.generator = WordGenerator()
        layout = BoxLayout(
            orientation = "vertical",
            padding = 20,
            spacing = 20
        )
        self.label = Label(
            text = "...",
            font_size = 40
        )
        button = Button(
            text = "New Word",
            font_size = 30
        )
        button.bind(on_press = self.new_word)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout
    def new_word(self, instance):
        self.label.text = self.generator.random_word()

if __name__ == "__main__":
    RandomWordApp().run()
from wonderwords import RandomWord
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

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
        Window.clearcolor = (0.3, 0.3, 0.3, 1)
        layout = BoxLayout(
            orientation = "vertical",
            padding = 20,
            spacing = 20
        )
        title = Label(
            text = "Don't know what to draw again?\nGenerate a random word! >:D",
            font_size = 50
        )
        self.label = Label(
            text = "...",
            font_size = 70
        )
        button = Button(
            text = "New Word",
            font_size = 40
        )
        button.bind(on_press = self.new_word)
        layout.add_widget(title)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout
    def new_word(self, instance):
        self.label.text = self.generator.random_word()

if __name__ == "__main__":
    RandomWordApp().run()
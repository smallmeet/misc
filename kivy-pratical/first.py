import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require('1.9.0')


class MyApp(App):

    def build(self):
        return Label(text="HW")

if __name__ == '__main__':
    MyApp().run()

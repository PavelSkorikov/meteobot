from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


from kivy.config import  Config
Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '780')

class MeteoBotApp(App):
    def build(self):
        bl = BoxLayout(orientation='vertical', padding=[30], spacing=10)
        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text='Кнопка1'))
        bl.add_widget(Button(text='Кнопка2'))
        bl.add_widget(Button(text='Кнопка3'))
        return bl


if __name__ == "__main__":
    MeteoBotApp().run()
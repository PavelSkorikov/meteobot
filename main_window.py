from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


from kivy.config import  Config
Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '860')

Activity = '''
BoxLayout:
    orientation: 'horizontal'
    size_hint: [1, 1]
    spacing: 10
    padding: [10,10,10,10]
    canvas:
        Color:
            rgb: [(113/100/2.55), (122/100/2.55), (115/100/2.55)]
        Rectangle:
            size: self.size    
    BoxLayout:
        orientation: 'vertical'
        size_hint: [.25, .96]
        spacing: 10
        padding: [5,5,10,40]
        Label:
            text_size: 220, None
            text: 'Location:'
            font_size: 18
            size_hint: [.9, .02]
        TextInput:
            font_size: 18
            size_hint: [.9, .03]
        Button:
            text: 'Search'
            font_size: 18 
            background_color: [(146/100/2.55), (146/100/2.55), (146/100/2.55), 1]
            size_hint: [.9, .03]
        Button:
            text: 'Graphics'
            font_size: 18 
            background_color: [(146/100/2.55), (146/100/2.55), (146/100/2.55), 1]
            size_hint: [.9, .03]
        Label:
            size_hint: [.9, .3]
            text_size: 220, None
            text: 'This is a weather widget program with a charting function.'
            font_size: 16
        Button:
            text: 'About'
            font_size: 18 
            size_hint: [.9, .03]
            background_color: [(146/100/2.55), (146/100/2.55), (146/100/2.55), 1]
            
        Button:
            text: 'Quit'
            font_size: 18 
            background_color: [(146/100/2.55), (146/100/2.55), (146/100/2.55), 1]
            size_hint: [.9, .03]
            on_press: app.stop()
    GridLayout:
        cols: 9
        rows: 9
        size_hint: [.7, 1]
        padding: [5,5,5,5]
        Label:
            text: 'Дата:'
            color: [0, 0, 0, 1]
            text_size: 100, None
        Label:
            text: 'сейчас'
        Label:
            text: '3'
        Label:
            text: '4'
        Label:
            text: '5'
        Label:
            text: '6'
        Label:
            text: '7'
        Label:
            text: '8'
        Label:
            text: '9'    
        Label:
            text: 'T.макс, Со:'
            color: [0, 0, 0, 1]
            text_size: 100, None
        Label:
            text: '2'
        Label:
            text: '3'
        Label:
            text: '4'
        Label:
            text: '5'
        Label:
            text: '6'
        Label:
            text: '7'
        Label:
            text: '8'
        Label:
            text: '9'
        Label:
            text: 'T.мин, Со:'
            color: [0, 0, 0, 1]
            text_size: 100, None
        Label:
            text: '2'
        Label:
            text: '3'
        Label:
            text: '4'
        Label:
            text: '5'
        Label:
            text: '6'
        Label:
            text: '7'
        Label:
            text: '8'
        Label:
            text: '9'
        Label:
            text: 'Ветер до, м/с:'
            color: [0, 0, 0, 1]
            text_size: 100, None
        Label:
            text: '2'
        Label:
            text: '3'
        Label:
            text: '4'
        Label:
            text: '5'
        Label:
            text: '6'
        Label:
            text: '7'
        Label:
            text: '8'
        Label:
            text: '9'
        Label:
            text: 'Осадки:'
            color: [0, 0, 0, 1]
            text_size: 100, None
        Label:
            text: '2'
        Label:
            text: '3'
        Label:
            text: '4'
        Label:
            text: '5'
        Label:
            text: '6'
        Label:
            text: '7'
        Label:
            text: '8'
        Label:
            text: '9'
        Label:
            text: 'Уровень осадков, мм:'
            color: [0, 0, 0, 1]
            text_size: 100, None
        Label:
            text: '2'
        Label:
            text: '3'
        Label:
            text: '4'
        Label:
            text: '5'
        Label:
            text: '6'
        Label:
            text: '7'
        Label:
            text: '8'
        Label:
            text: '9'
        Label:
            text: 'Видимость, км:'
            color: [0, 0, 0, 1]
            text_size: 100, None
        Label:
            text: '2'
        Label:
            text: '3'
        Label:
            text: '4'
        Label:
            text: '5'
        Label:
            text: '6'
        Label:
            text: '7'
        Label:
            text: '8'
        Label:
            text: '9'
        Label:
            text: 'Влажность, %:'
            color: [0, 0, 0, 1]
            text_size: 100, None
        Label:
            text: '2'
        Label:
            text: '3'
        Label:
            text: '4'
        Label:
            text: '5'
        Label:
            text: '6'
        Label:
            text: '7'
        Label:
            text: '8'
        Label:
            text: '9'
     
        
     
     '''
class MeteoBotApp(App):
    def build(self):
        return Builder.load_string(Activity)


if __name__ == "__main__":
    MeteoBotApp().run()
import json, requests
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from kivy.config import  Config
Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '720')

""""""

class MainForm(BoxLayout):
    search_input = ObjectProperty()
    info = ObjectProperty()
    date = ObjectProperty()
    tmax = ObjectProperty()
    tmin = ObjectProperty()

    def search_location(self):
        location = self.search_input.text
        if location == 'Москва':
            location = 'Moscow'
        url_apixu = 'http://api.apixu.com/v1/forecast.json?key=209e4be4a40a421ab34160306191302&q=%s&days=10' % (
            location)
        response = requests.get(url_apixu)
        if response.status_code == 400:
            self.info.text = 'Такое место не найдено'
            return
        else:
            w = json.loads(response.text)
            self.info.text = str(w['location'])
            for i in range(7):
                d = w['forecast']['forecastday'][i]['date'].replace('-','.')
                self.date[i].text = d[5:]
                self.tmax[i].text = str(w['forecast']['forecastday'][i]['day']['maxtemp_c'])
                self.tmin[i].text = str(w['forecast']['forecastday'][i]['day']['mintemp_c'])

            print(w['current']['last_updated'], w['current']['temp_c'], w['current']['condition']['icon'])
            print(w['forecast']['forecastday'][0]['date'], w['forecast']['forecastday'][0]['day'])

class MeteoBotApp(App):
    pass

if __name__ == "__main__":
    MeteoBotApp().run()
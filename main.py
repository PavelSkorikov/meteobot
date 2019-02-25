import json, requests
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from threading import Thread

from kivy.config import  Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '720')
Config.set('kivy', 'exit_on_escape', '0')

class Gerenciador(ScreenManager):
    pass


class MainForm(Screen):

    def search_location(self):
        location = self.search_input
        if location == 'Москва':
            location = 'Moscow'
        url_apixu = 'http://api.apixu.com/v1/forecast.json?key=209e4be4a40a421ab34160306191302&q=%s&days=10' % (
            location)
        try:
            response = requests.get(url_apixu)
        except ConnectionError:
            self.info.text = 'Ошибка, проверьте соединение с интернетом!'
            return
        if response.status_code == 400:
            self.info.text = 'Такое место не найдено'
            for i in range(7):
                self.tmax[i].text = ''
                self.tmin[i].text = ''
                self.wind[i].text = ''
                self.condition[i].source = 'faq.png'
                self.totalprecip[i].text = ''
                self.avgvis[i].text = ''
                self.avghumidity[i].text = ''
            return
        else:
            w = json.loads(response.text)
            nf = 'страна: ' + str(w['location']['country']) + '\n' + 'регион: ' + str(w['location']['region']) + '\n' + 'широта: ' + str(w['location']['lat']) + '\n' + 'долгота: ' + str(w['location']['lon']) + '\n' + 'время:' + str(w['location']['localtime'])
            self.info.text = nf
            for i in range(7):
                d = w['forecast']['forecastday'][i]['date'].replace('-','.')
                self.date[i].text = d[8:10] + d[4:7]
                self.tmax[i].text = str(w['forecast']['forecastday'][i]['day']['maxtemp_c'])
                self.tmin[i].text = str(w['forecast']['forecastday'][i]['day']['mintemp_c'])
                self.wind[i].text = str(w['forecast']['forecastday'][i]['day']['maxwind_mph'])
                self.condition[i].source = 'http:' + str(w['forecast']['forecastday'][i]['day']['condition']['icon'])
                self.totalprecip[i].text = str(w['forecast']['forecastday'][i]['day']['totalprecip_mm'])
                self.avgvis[i].text = str(w['forecast']['forecastday'][i]['day']['avgvis_km'])
                self.avghumidity[i].text = str(w['forecast']['forecastday'][i]['day']['avghumidity'])
                self.voshod[i].text = str(w['forecast']['forecastday'][i]['astro']['sunrise'])
                self.zakat[i].text = str(w['forecast']['forecastday'][i]['astro']['sunset'])
    def meteo_worker(self):
        t = Thread(target=self.search_location)
        t.start()
        t.join()
    def prog_info(self):
        self.info.text = 'Эта программа создана в целях изучения python + kivy. Автор - Скориков П.Г. spg75@yandex.ru'

class MeteoBotApp(App):
    def build(self):
        return Gerenciador()

if __name__ == "__main__":
    MeteoBotApp().run()
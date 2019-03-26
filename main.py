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
        # считываем название населенного пункта
        location = self.search_input
        if location == 'Москва':
            location = 'Moscow'
        # строим запрос к API сайта
        url_apixu = 'http://api.apixu.com/v1/forecast.json?key=********&q=%s&days=10' % (
            location)
        try:
        # скачиваем данные
            response = requests.get(url_apixu)
        except ConnectionError:
            self.info.text = 'Ошибка, проверьте соединение с интернетом!'
            return
        # если город не найден выдаем сообщение и сбрасываем данные формы
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
        # если все ОК разбираем JSON ответ и заполняем поля формы
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
        # запускаем загрузку данных в отдельном потоке, чтобы программа не зависла при плохом интернете
        t = Thread(target=self.search_location)
        t.start()
        t.join()
    def prog_info(self):
        self.info.text = 'Данные берутся с сайта apixu.com.'+'\n'+'Автор - Скориков П.Г. spg75@yandex.ru'

class MeteoBotApp(App):
    def build(self):
        self.icon = 'icon.png'
        return Gerenciador()

if __name__ == "__main__":
    MeteoBotApp().run()

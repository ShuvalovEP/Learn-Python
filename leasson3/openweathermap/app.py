import os
import requests
from flask import Flask, render_template
from datetime import datetime


weatr_city = 'Moscow,RU'


app = Flask(__name__)


def date_string():
    date = datetime.now()
    date = date.strftime('%d.%m.%y')
    return date


def open_weat():
    key = os.getenv('weatr_key', ' ')
    response = requests.get('http://api.openweathermap.org/data/2.5/find',
                            params={'q': weatr_city, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    if response.status_code == 200:
        data = response.json()
        rain = data['list'][0]['rain']
        city = data['list'][0]['name']
        temp = data['list'][0]['main']['temp']
        clouds = data['list'][0]['weather'][0]['description']
        if rain == None:
            rain = 'без осадков'
        if city == 'Moscow':
            city = 'Москве'
        weather = ('{date} В {city} сегодня {clouds} и {rain} а темпиратура +{temp} гадуса'
                   .format(city=city, date=date_string(), temp=temp, clouds=clouds, rain=rain))
        return weather


@app.route('/')
def hello():
    weather = open_weat()
    return render_template('index.html', weather=weather)


if __name__ == '__main__':
    app.run(debug=True)

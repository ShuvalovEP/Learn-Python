import os
import requests
from flask import Flask, render_template, request
from datetime import datetime


config = {
    'data_mos_key': os.getenv('data_mos_key', ' '),
    'open_weat_key': os.getenv('open_weat_key', ' '),
    'data_mos_url': 'http://api.data.mos.ru/v1/datasets/2009/rows',
    'open_weat_url': 'http://api.openweathermap.org/data/2.5/find',
    'weatr_city': 'Moscow,RU'}



def date_string():
    date = datetime.now()
    date = date.strftime('%d.%m.%y')
    return date


app = Flask(__name__)


def open_weat():
    response = requests.get(config.get('open_weat_url'), 
        params={'q': config.get('weatr_city'),
                'APPID': config.get('open_weat_key') ,    
                'lang': 'ru', 
                'type': 'like', 
                'units': 'metric'})
    if response.status_code == 200:
        data = response.json()
        rain = data['list'][0]['rain']
        city = data['list'][0]['name']
        if rain == None:
            rain = 'без осадков'
        if city == 'Moscow':
            city = 'Москве'
        weather = ('{date} В {city} сегодня {clouds} и {rain} а темпиратура +{temp} гадуса'
                   .format(
                           clouds = data['list'][0]['weather'][0]['description'],
                           date = date_string(), 
                           temp = data['list'][0]['main']['temp'], 
                           rain = rain, 
                           city = city
                           ))
        return weather


def data_mos(year):
    names_list = []
    response = requests.get(config.get('data_mos_url'), 
        params={'api_key': config.get('data_mos_key'), 
                '$filter': 'Cells/Year eq ''{year}'''.format(year=year)})
    if response.status_code == 200:
        data = response.json()
        for row in data:
            names_list.append(
                        {'global_id': row.get('global_id'),
                        'numb': row.get('Number'),
                        'name': row.get('Cells').get('Name').replace('\n',''),
                        'year': row.get('Cells').get('Year'),
                        'month': row.get('Cells').get('Month'),
                        'num_person': row.get('Cells').get('NumberOfPersons')})
    return names_list


@app.route('/')
def index():
    weather = open_weat()
    return render_template('index.html', weather=weather)


@app.route('/name')
def names():
    data = request.args.get('year', '2018')
    data_list = data_mos(data)
    return render_template('name.html', data_list=data_list)


if __name__ == '__main__':
    app.run(debug=True)

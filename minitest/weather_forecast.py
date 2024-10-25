import os
from dotenv import load_dotenv
import requests
import datetime


load_dotenv()

class WeatherForecast(object):

    def get_data(self):
        res = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q=jakarta&appid={os.getenv('WEATHER_API_KEY')}&units=metric')
        return res.json()['list']


    def main(self)-> None:
        result = self.get_data()
        print("Weather Forecast:")
        for data in result:
            timestamp = datetime.datetime.fromisoformat(data["dt_txt"])
            if timestamp.time() == datetime.time(12):
                formatted_time = timestamp.strftime("%a, %d %b %Y")
                temp = data['main']['temp']
                print(f"{formatted_time}: {temp}°C")




obj = WeatherForecast()
obj.main()
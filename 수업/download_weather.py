import requests
import os

def download(filename:str, station:int, year:int) -> None:
    URL = 'https://api.taegon.kr/stations/{}/?sy={}&ey={}&format=csv'.format(station, year, year)

    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            res = requests.get(URL)
            f.write(res.text)

def main():
    year = int(input('YEAR: '))
    station = int(input('지역 번호: '))
    filename = './weather_{}_{}.csv'.format(station, year)
    download(filename, station, year)

if __name__ == '__main__':
    main()

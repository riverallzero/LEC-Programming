import requests
import os

def download(filename, year):
    URL = 'https://api.taegon.kr/stations/146/?sy={}&ey={}&format=csv'.format(year, year)

    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            res = requests.get(URL)
            f.write(res.text)

def main():
    year = int(input('YEAR: '))
    filename = './weather_146_{}.csv'.format(year)
    download(filename, year)

if __name__ == '__main__':
    main()

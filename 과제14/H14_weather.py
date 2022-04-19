import os
from typing import List

import requests
import matplotlib.pyplot as plt

def download_weather(filename: str) -> None:
    """기상청에서 자료를 다운받아서 저장합니다."""
    URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19820101&endDt=20211231&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19820101&startYear=1982&endDay=20211231&endYear=2021&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="

    if not os.path.exists(filename):
        res = requests.get(URL)
        with open(filename, "w", newline="") as f:
            f.write(res.text)


def str2float(text: str, default_value: float = -999) -> float:
    try:
        return float(text)
    except ValueError:
        return default_value


def read_data(filename) -> (List[str], List[float], List[float]):
    """기상자료를 읽어서 날짜, 최저기온, 최고기온 리스트를 리턴합니다."""
    date_list = []
    tavg_list = []
    tmin_list = []
    tmax_list = []

    with open(filename) as f:
        lines = f.readlines()
        for line in lines[8:]:
            line = line.strip()
            if line == "":
                continue
            tokens = line.split(",")
            date_list.append(tokens[0].split("-"))
            tavg_list.append(str2float(tokens[2], 999))
            tmin_list.append(str2float(tokens[3], 999))
            tmax_list.append(str2float(tokens[4], -999))

    return date_list, tavg_list, tmin_list, tmax_list

def main():
    filename = "./history_jeonju.csv"
    download_weather(filename)

    dates, tavg, tmin, tmax = read_data(filename)

    year = int(input('YEAR: '))
    month = int(input('MONTH: '))
    date = int(input('DATE: '))
    input_tavg = [x[1] for x in zip(dates, tavg) if (int(x[0][1]) == month) and (int(x[0][2]) == date) and (int(x[0][0]) >= year)]
    tavg_history = [x[1] for x in zip(dates, tavg) if (int(x[0][1]) == month) and (int(x[0][2]) == date)]
    find_tavg = [x[1] for x in zip(dates, tavg) if (int(x[0][1]) == month) and (int(x[0][2]) == date) and (int(x[0][0]) == year)]

    tavg_list = []
    tavg_list.extend(tavg_history)
    tavg_list.sort(reverse=True)

    max_num = tavg_list.index(find_tavg[0])+1

    plt.plot(range(year, 2022), input_tavg, 'yellow')
    plt.plot(range(1982, 2022), tavg_history, 'yellow')
    plt.axhline(y=find_tavg[0], color='black', linestyle='--')
    plt.text(year, find_tavg[0], '   {}/40 HIGH'.format(max_num), color='red')
    plt.plot(year, find_tavg[0], 'ro')
    plt.show()
    print('40년 중 {}번째 높은 기온입니다.' .format(max_num))

if __name__ == "__main__":
    main()

from download_weather import download

def count_rain_days(rainfall):
    rain_days = 0
    for x in rainfall:
        if x > 0:
            rain_days += 1
    return rain_days

def sumifs(rainfall, months, selected = [6, 7, 8]):
    days = len(rainfall)
    sum_rainfall = 0
    for x in range(days):
        if months[x] in selected:
            sum_rainfall += rainfall[x]
    return sum_rainfall

def longest_rain_days(rainfall):
    rain_day = 0
    rain_day_list = []
    for x in rainfall:
        if x > 0:
            rain_day += 1
        else:
            if rain_day > 0:
                rain_day_list.append(rain_day)
            rain_day = 0
    if rain_day > 0:
        rain_day_list.append(rain_day)
    return max(rain_day_list)

def maximum_rainfall_event(rainfall):
    rain_day = 0
    rain_total = 0
    rain_day_list = []
    rain_total_list = []

    for x in rainfall:
        if x > 0:
            rain_day += 1
            rain_total += x
        else:
            if rain_day > 0:
                rain_day_list.append(rain_day)
                rain_total_list.append(rain_total)
            rain_day = 0
    if rain_day > 0:
        rain_day_list.append(rain_day)
        rain_total_list.append(rain_total)

    return max(rain_total_list)

def maximum_temp_gap(dates, tmax, tmin):
    length = len(dates)
    tmax_tmin = []
    for x in range(length):
        diff = tmax[x] - tmin[x]
        tmax_tmin.append(diff)

    return dates[tmax_tmin.index(max(tmax_tmin))], max(tmax_tmin)

def gdd(dates, tavg):
    length = len(dates)
    gdd_list = []
    for x in range(length):
        if dates[x][1] in [5, 6, 7, 8, 9]:
            gdd = tavg[x] - 5
            if gdd > 0:
                gdd_list.append(gdd)
    return sum(gdd_list)

def main():
    year = int(input('YEAR: '))
    filename = './weather_146_{}.html'.format(year)
    download(filename, year)

    with open(filename) as f:
        lines = f.readlines()

    rainfall = [float(x.split(',')[9]) for x in lines[1:]]
    months = [int(x.split(',')[1]) for x in lines[1:]]
    dates = [[int(x.split(',')[0]), int(x.split(',')[1]), int(x.split(',')[2])] for x in lines[1:]]
    tmax = [float(x.split(',')[3]) for x in lines[1:]]
    tmin = [float(x.split(',')[5]) for x in lines[1:]]
    tavg = [float(x.split(',')[4]) for x in lines[1:]]


    print('총 강수량: {:.1f} mm' .format(sum(rainfall)))
    print('강우 일수: {:d} 일' .format(count_rain_days(rainfall)))
    print('여름철(6월 ~ 8월) 총 강수량: {:.1f} mm' .format(sumifs(rainfall, months, [6, 7, 8])))
    print('최장연속강우일수: {:d} 일' .format(longest_rain_days(rainfall)))
    print('강우이벤트 중 최대 강수량: {:.1f} mm' .format(maximum_rainfall_event(rainfall)))
    print('일교차가 가장 큰 날짜, 해당일자의 일교차: {}, {:.1f}' .format((maximum_temp_gap(dates, tmax, tmin)[0]), (maximum_temp_gap(dates, tmax, tmin)[1])))
    print('5월부터 9월까지 적산온도: {:.1f}' .format(gdd(dates, tavg)))

if __name__ == '__main__':
    main()

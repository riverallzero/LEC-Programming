from datetime import datetime
import hw11_submission


def hot_date(dates, tmax_data):
    hot_date_list = []
    length = len(dates)
    for x in range(length):
        hot_date_list.append(tmax_data[x])
    return datetime.strptime(dates[hot_date_list.index(max(hot_date_list))], '%Y%m%d').date()


def cold_date(dates, tmin_data):
    cold_date_list = []
    length = len(dates)
    for x in range(length):
        cold_date_list.append(tmin_data[x])
    return datetime.strptime(dates[cold_date_list.index(min(cold_date_list))], '%Y%m%d').date()


def tmax(dates, tmax_data):
    hot_tmax_list = []
    length = len(dates)
    for x in range(length):
        hot_tmax_list.append(tmax_data[x])
    return max(hot_tmax_list)


def tmin(dates, tmin_data):
    cold_tmin_list = []
    length = len(dates)
    for x in range(length):
        cold_tmin_list.append(tmin_data[x])
    return min(cold_tmin_list)


def main():
    filename = 'jeonju_data.csv'

    with open(filename) as f:
        lines = f.readlines()

        name = '강다영'
        dates = [str(x.split(',')[0]) for x in lines[1:]]
        tmax_data = [float(x.split(',')[4]) for x in lines[1:]]
        tmin_data = [float(x.split(',')[3]) for x in lines[1:]]

    print('이름: {}'.format(name))
    print('최고기온: {:.1f}도'.format(tmax(dates, tmax_data)))
    print('최고기온날짜: {}'.format(hot_date(dates, tmax_data)))
    print('최저기온: {:.1f}도'.format(tmin(dates, tmin_data)))
    print('최저기온날짜: {}'.format(cold_date(dates, tmin_data)))

    hw11_submission.submit(
        name, hot_date(dates, tmax_data), tmax(dates, tmax_data), cold_date(dates, tmin_data), tmin(dates, tmin_data)
    )


if __name__ == '__main__':
    main()

from datetime import datetime

def hot_date(dates, tmax_data):
    hot_date_list = []
    length = len(dates)
    for x in range(length):
            hot_date_list.append(tmax_data[x])
    return datetime.strptime(dates[hot_date_list.index(max(hot_date_list))],'%Y%m%d').date()

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

if __name__ == '__main__':
    main()
    
    
    
    
#CSV 파일을 URL로 다운받고 하려고 했지만, 1900년대 리스트의 공백값  오류를 어떻게 처리하지 못하여 다운받은 후 엑셀을 조금 손봐준 뒤 실행하였습니다.
#열심히 구글링도 해보고 직접 해보았지만 처음보는 오류들을 많이 경험하였고 해결하지 못했습니다....
#금요일부터 시작한 과제는 쉬운방향으로 바꾸어 드디어 완료했습니다 ㅎㅎ
#과제를 끝내고 잠이 오지 않아 끄적여 봅니다..... 


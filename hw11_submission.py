import requests


def submit(name: str, hot_date: str, tmax: float, cold_date: str, tmin: float) -> None:
    URL = "https://script.google.com/macros/s/AKfycbyNex1PwGoPeR9Be--QlYrD90C8CR6FU_CC82K2EaGrc2-uVHtbHOw7ZwjfNTESHA5Eiw/exec"
    PARAMS = {
        '제출자': name,
        '최고기온': tmax,
        '최고기온날짜': hot_date,
        '최저기온': tmin,
        '최저기온날짜': cold_date}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        print("과제가 정상적으로 제출되지 않았습니다.")


if __name__ == "__main__":
    submit("홍길동", "2021-08-15", 40.1, "1978-01-04", -32.5)

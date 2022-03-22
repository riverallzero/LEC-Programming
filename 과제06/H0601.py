def average(nums):
    return sum(nums)/len(nums)

def main():
    nums = list(map(int, input('숫자(띄어쓰기로 여러 값 입력): ').split()))
    print('평균: {}' .format(average(nums)))


if __name__ == '__main__':
    main()

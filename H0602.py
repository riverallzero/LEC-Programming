def range_list(n):
    return n[0:int(len(n)+1)]

def main():
    num = int(input('숫자: '))
    n = list(range(1, num+1))
    print('1-{}까지의 리스트 = {}' .format(num, range_list(n)))

if __name__ == '__main__':
    main()

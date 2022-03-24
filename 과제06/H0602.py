# def range_list(n):
#     return list(range(1, int(n)+1))

# def main():
#     n = input('숫자: ')
#     n = n.strip('n=')
#     print('1-{}까지의 리스트 = {}' .format(n, range_list(n)))

# if __name__ == '__main__':
#     main()


def range_list(n):
    return [x for x in range(1, n+1)]

def main():
    n = int(input('숫자: '))
    print('1-{}까지의 리스트 {}' .format(n, range_list(n)))

if __name__ == '__main__':
    main()

def sum_n(n):
    return int(n*(n+1)/2)

if __name__ == '__main__':
    n = int(input('n: '))
    print(('1부터 {}까지의 합은 {}이다.' .format(n, sum_n(n)))

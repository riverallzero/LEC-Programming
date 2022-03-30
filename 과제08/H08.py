def main():
    f = open('number.txt')
    lines = f.readlines()
    str(lines).strip()
    remove = {'\n'}
    nums = [int(x) for x in lines if x not in remove]

    print(lines)
    print(nums)
    print('총 숫자의 개수', len(nums))
    print('평균', sum(nums) / len(nums))
    print('최댓값', max(nums))
    print('최솟값', min(nums))


if __name__ == '__main__':
    main()



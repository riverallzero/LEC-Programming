def text2list(nums):
    return list(nums)

def average(nums):
    return sum(nums) / len(nums)

def median(nums):
    nums = sorted(nums)
    m = len(nums) // 2
    if len(nums) % 2 == 0:
        return max(nums[m-1], nums[m])
    else:
        return nums[m]

def main():
    input_text = '5 10 3 4 7'
    nums = list(map(int, text2list(input_text.split())))
    print('주어진 리스트는', nums)
    print('평균값은 {:.1f}' .format(average(nums)))
    print('중앙값은 {}' .format(median(nums)))

if __name__ == '__main__':
    main()
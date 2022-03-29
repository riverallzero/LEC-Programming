def text2list(nums):
    return list(nums)
#return [int(x) for x in text_input.split()]

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

# 파일로 input 불러오기
#     f = open('파일이름.txt')
#     input_text = f.readline().strip() #input_text 덮어서 파일 데이터로 불러옴

    nums = list(map(int, text2list(input_text.split())))       
    print('주어진 리스트는', nums)
    print('평균값은 {:.1f}' .format(average(nums)))
    print('중앙값은 {}' .format(median(nums)))

if __name__ == '__main__':
    main()
    
    
    

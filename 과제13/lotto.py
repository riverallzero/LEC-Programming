import random

def read_input():
    return int(input('횟수: '))

def main():
    count = read_input()
    for i in range(count):
        print(random.sample(range(1, 45), 6))

if __name__ == '__main__':
    main()
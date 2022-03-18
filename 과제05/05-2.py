def c2f(t_c):
    return (t_c*1.8) + 32

if __name__ == '__main__':
    t_c = int(input('섭씨: '))
    print("섭씨 {} C -> 화씨 {} F" .format(t_c, c2f(t_c)))

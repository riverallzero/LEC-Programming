def c2f(t_c):

    t_f = (t_c*1.8)+32
    print("섭씨 {} C -> 화씨 {} F" .format(t_c, t_f))

if __name__ == '__main__':
    t_c = int(input('섭씨: '))
    c2f(t_c)

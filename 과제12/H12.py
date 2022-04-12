def main():
    text_list = []
    while True:
        text = input('X=? ')
        try:
            text = int(text)
            text_list.append(text)
        except:
            pass
        if text == -1:
            break
    print('입력된 값은 {}입니다.'.format(text_list))

if __name__ == '__main__':
    main()

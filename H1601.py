def toggle_text(text: str) -> str:
    textlist = []
    for x in range(len(text)):
        if (ord(text[x]) <= 90) and (ord(text[x]) >= 65):
            textlist.append(chr(ord(text[x]) + 32))
        elif (ord(text[x]) <= 122) and (ord(text[x]) >= 97):
            textlist.append(chr(ord(text[x]) - 32))
        else:
            textlist.append(text[x])

    result = ''.join(textlist)

    return result


def main():
    text = input('text: ')
    print('대소문자 변경: {} -> {}' .format(text, toggle_text(text)))


if __name__ == '__main__':
    main()

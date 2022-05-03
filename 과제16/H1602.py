def caesar_encode(text: str, shift: int = 3) -> str:
    c_enlist = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
                'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
                'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    c_enlist_repeat = c_enlist * shift

    enlist = []
    for x in range(len(text)):
        if text[x] in c_enlist:
            enlist.append(c_enlist_repeat[c_enlist.index(text[x]) + 2 * shift])

    result = ''.join(enlist)

    return result


def caesar_decode(text: str, shift: int = 3) -> str:
    c_delist = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
                'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
                'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

    enlist = []
    for x in range(len(text)):
        if text[x] in c_delist:
            enlist.append(c_delist[c_delist.index(text[x]) - 2*shift])

    result = ''.join(enlist)

    return result


def main():
    text = input('text: ')
    print('카이사르 암호(encoding): {} -> {}'.format(text, caesar_encode(text)))
    print('카이사르 암호(decoding): {} -> {}'.format(text, caesar_decode(text)))


if __name__ == '__main__':
    main()

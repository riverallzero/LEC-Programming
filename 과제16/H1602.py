def caesar_encode(text: str, shift: int = 3) -> str:
    Llist = []   # 대문자 리스트
    slist = []   # 소문자 리스트

    for x in range(65, 91):
        Llist.append(chr(x))
    for y in range(97, 123):
        slist.append(chr(y))
    c_enlist = [*sum(zip(Llist, slist), ())]

    c_enlist_repeat = c_enlist * shift

    enlist = []
    for z in range(len(text)):
        if text[z] in c_enlist:
            enlist.append(c_enlist_repeat[c_enlist.index(text[z]) + 2 * shift])

    result = ''.join(enlist)

    return result


def caesar_decode(text: str, shift: int = 3) -> str:
    Llist = []
    slist = []

    for x in range(65, 91):
        Llist.append(chr(x))
    for y in range(97, 123):
        slist.append(chr(y))
    c_delist = [*sum(zip(Llist, slist), ())]

    delist = []
    for x in range(len(text)):
        if text[x] in c_delist:
            delist.append(c_delist[c_delist.index(text[x]) - 2*shift])

    result = ''.join(delist)

    return result


def main():
    text = input('text: ')
    print('카이사르 암호(encoding): {} -> {}'.format(text, caesar_encode(text)))
    print('카이사르 암호(decoding): {} -> {}'.format(text, caesar_decode(text)))


if __name__ == '__main__':
    main()
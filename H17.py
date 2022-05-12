from tkinter import *


def caesar_encode(text: str, shift: int = 3) -> str:
    Llist = []
    slist = []

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
            delist.append(c_delist[c_delist.index(text[x]) - 2 * shift])

    result = ''.join(delist)

    return result


def gui_input():
    text = e1.get()
    return text


def result_encode():
    caesar_encoding = caesar_encode(gui_input()) + '                                                                  '
    return e2.insert(0, caesar_encoding)


def result_decode():
    caesar_decoding = caesar_decode(gui_input()) + '                                                                  '

    return e2.insert(0, caesar_decoding)


def window_quit():
    return window.destroy()


window = Tk()
window.title('카이사르 암호 해독기')
window.geometry('345x100')
window.resizable(width=False, height=False)

l1 = Label(window, text='문자 입력')
l2 = Label(window, text='해독 결과')
l1.grid(row=1, column=1)
l2.grid(row=2, column=1)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=1, column=2)
e2.grid(row=2, column=2)

b1 = Button(window, text='Encoding', height=1, width=10, fg='blue', command=result_encode)
b2 = Button(window, text='Decoding', height=1, width=10, fg='blue', command=result_decode)
b3 = Button(window, text='Quit', height=1, width=10, fg='red', command=window_quit)
b1.grid(row=3, column=1, padx=10)
b2.grid(row=3, column=3, padx=10)
b3.grid(row=3, column=2)

window.mainloop()


def main():
    window.mainloop()


if __name__ == '__main__':
    main()

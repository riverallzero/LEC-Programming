from tkinter import *


class CaesarCipyer:
    def __init__(self, shift: int = 3):
        self.shift = shift
        self.window = Tk()
        self.window.title('카이사르 암호 해독기')
        self.window.geometry('345x100')
        self.window.resizable(width=False, height=False)

        self.l1 = Label(self.window, text='문자 입력')
        self.l2 = Label(self.window, text='해독 결과')
        self.l1.grid(row=1, column=1)
        self.l2.grid(row=2, column=1)

        self.e1 = Entry(self.window)
        self.e2 = Entry(self.window)
        self.e1.grid(row=1, column=2)
        self.e2.grid(row=2, column=2)

        self.b1 = Button(self.window, text='Encoding', height=1, width=10, fg='blue', command=self.result_encode)
        self.b2 = Button(self.window, text='Decoding', height=1, width=10, fg='blue', command=self.result_decode)
        self.b3 = Button(self.window, text='Quit', height=1, width=10, fg='red', command=self.window_quit)
        self.b1.grid(row=3, column=1, padx=10)
        self.b2.grid(row=3, column=3, padx=10)
        self.b3.grid(row=3, column=2)


    def caesar_encode(self, text: str, shift: int = 3) -> str:
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


    def caesar_decode(self, text: str, shift: int = 3) -> str:
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


    def gui_input(self):
        text = self.e1.get()
        return text


    def result_encode(self):
        caesar_encoding = self.caesar_encode(self.gui_input()) + '                                                                  '
        return self.e2.insert(0, caesar_encoding)


    def result_decode(self):
        caesar_decoding = self.caesar_decode(self.gui_input()) + '                                                                  '

        return self.e2.insert(0, caesar_decoding)


    def window_quit(self):
        return self.window.destroy()




    def show(self):
        return self.window.mainloop()


def main():
    caesar_gui = CaesarCipyer(5)
    caesar_gui.show()

if __name__ == '__main__':
    main()

import tkinter
import tkinter.font

def run(code_t):
    import tkinter

    window = tkinter.Tk()

    window.title("Preview")
    window.geometry("1000x1000+100+100")
    window.resizable(False, False)

    line_list = code_t.split("\n")
    for string in line_list:
        word_list = string.split(" ")
        for word in word_list:
            if word.replace(' ', '') == '':
                pass
            if word == "#title":
                font = tkinter.font.Font(size=30)
                print('w', str(word_list[1:]))
                text = ""
                for i in word_list[1:]:
                    text += i + ' '
                label = tkinter.Label(window, text=text, font=font)
                label.pack()
            if word == "#subtitle":
                pass
            if word == "#headline":
                pass
            if word == "#text":
                pass
            if word == "#footline":
                 pass
    window.mainloop()
    return

if __name__ == '__main__':
    code = "#title hello, and I am coder!"
    run(code)
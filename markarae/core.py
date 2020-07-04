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
                font = tkinter.font.Font(size=35, weight='bold')
                print('w', str(word_list[1:]))
                text = ""
                for i in word_list[1:]:
                    text += i + ' '
                label = tkinter.Label(window, text=text, font=font, wraplength=900)
                label.pack()
            if word == "#subtitle":
                font = tkinter.font.Font(size=30)
                print('w', str(word_list[1:]))
                text = ""
                for i in word_list[1:]:
                    text += i + ' '
                label = tkinter.Label(window, text=text, font=font, wraplength=900)
                label.pack()
            if word == "#headline":
                font = tkinter.font.Font(size=20)
                print('w', str(word_list[1:]))
                text = ""
                for i in word_list[1:]:
                    text += i + ' '
                label = tkinter.Label(window, text=text, font=font, wraplength=900)
                label.pack()
            if word == "#text":
                font = tkinter.font.Font(size=15)
                print('w', str(word_list[1:]))
                text = ""
                for i in word_list[1:]:
                    text += i + ' '
                label = tkinter.Label(window, text=text, font=font, wraplength=900)
                label.pack()
            if word == "#footline":
                font = tkinter.font.Font(size=10)
                print('w', str(word_list[1:]))
                text = ""
                for i in word_list[1:]:
                    text += i + ' '
                label = tkinter.Label(window, text=text, font=font, wraplength=900)
                label.pack()
    window.mainloop()
    return


if __name__ == '__main__':
    with open('file.mkarae') as f:
        run(f.read())

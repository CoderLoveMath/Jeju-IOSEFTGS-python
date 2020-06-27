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
    run(
        """
#title Hello, and this is Markarae hypertext language!
#subtitle made by coder
#headline 2020-06-27
#text Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam
        """
    )
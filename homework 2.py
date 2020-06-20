import time
from tkinter import *

mode = input('GUI or CUI? gui:1, cui:any(except 1): ')

def cui():
    print("""
     __  __ _             _         _          __  __                   
     |  \/  (_)           | |       | |        |  \/  |                  
     | \  / |_ _ __  _   _| |_ ___  | |_ ___   | \  / | __ _ _ __  _   _ 
     | |\/| | | '_ \| | | | __/ _ \ | __/ _ \  | |\/| |/ _` | '_ \| | | |
     | |  | | | | | | |_| | ||  __/ | || (_) | | |  | | (_| | | | | |_| |
     |_|  |_|_|_| |_|\__,_|\__\___|  \__\___/  |_|  |_|\__,_|_| |_|\__, |
                                                                    __/ |
                                                                   |___/ 
    """)
    base = int(input('minute time: '))

    print('converting...')
    time.sleep(2)
    h = base // 60
    m = base % 60

    print('convert finished: ', h, 'hour', m, 'minute')

def gui():
    window = Tk()
    window.title("Minute to Many")
    window.geometry("640x480+100+100")
    window.resizable(False, False)

    label = Label(window)
    label.config(text="Minute to Many")

    spacer = Label(window)
    spacer.config(text="  ")

    input_e = Entry(window)

    result = Label(window)

    def calc():
        base = int(input_e.get())
        h = base // 60
        m = base % 60
        result_str = str(h) + 'hour ' + str(m) + 'min'
        result.config(text=result_str)

    btn = Button(window)
    btn.config(text="Convert", command=calc)

    label.pack()
    spacer.pack()
    input_e.pack()
    btn.pack()
    result.pack()

    window.mainloop()


if mode == '1':
    gui()
else:
    cui()




from tkinter import *
from workers import Worker


def make_plan():
    a = Input.get(1.0, 'end')
    s = Worker()
    parts = a.split('\n')
    name_time = parts[0].split(',')
    s.name = name_time[0]
    out = ''
    flag = 0
    for i in parts:
        if i.find('https://') != -1:
            if flag == 1:
                s.this_week.append(i)
            elif flag == 2:
                s.next_week.append(i)
        elif i.find('едел') != -1:
            flag += 1
    s.make_tasks()
    tasks = s.out()
    for i in tasks:
        out = out + i + '\n'
    Output.insert(1.0, out)


def clear_text():
    Input.delete(1.0, 'end')
    Output.delete(1.0, 'end')

def _onKeyRelease(event):
    ctrl = (event.state & 0x4) != 0
    if event.keycode == 88 and ctrl and event.keysym.lower() != "x":
        event.widget.event_generate("<<Cut>>")
    if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")
    if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")
    if event.keycode == 65 and ctrl and event.keysym.lower() != "a":
        event.widget.event_generate("<<SelectAll>>")


if __name__ == '__main__':
    links = ['https://apkdk.kaiten.ru/space/20752/card/4859473', 'https://apkdk.kaiten.ru/space/20752/card/1724375',
             'https://apkdk.kaiten.ru/space/20752/card/4855532']

    Window = Tk()
    Window['bg'] = "#555"
    Window.title("СФО")
    Window.geometry('1080x720')
    Window.bind("<Control-KeyPress>", _onKeyRelease)
    Input = Text(width=50, height=35, background="#fafafa")
    Output = Text(width=50, height=35, background="#fafafa")
    Make = Button(text="Создать отчет", background="#fafafa", command=make_plan, )
    Clear = Button(text="Очистить", background="#fafafa", command=clear_text, )
    Input.place(x=100, y=20)
    Output.place(x=600, y=20)
    Make.place(x=300, y=600, height=40, width=500)
    Clear.place(x=300, y=650, height=40, width=500)

    Window.mainloop()

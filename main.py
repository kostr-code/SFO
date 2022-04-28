from tkinter import *
from workers import Worker


def make_plan():
    a = Input.get(1.0, 'end')
    parts = a.split('\n')
    name_time = parts[0].split(',')
    name = name_time[0]
    link = []
    out = ''
    for i in parts:
        if i.find('https://') != -1:
            link.append(i)
    s = Worker()
    s.links = link
    s.name = name
    s.make_tasks()
    tasks = s.out()
    for i in tasks:
        out = out + i + '\n'
    Output.insert(1.0, out)

def clear_text():
    Input.delete(1.0, 'end')
    Output.delete(1.0, 'end')

if __name__ == '__main__':
    links = ['https://apkdk.kaiten.ru/space/20752/card/4859473', 'https://apkdk.kaiten.ru/space/20752/card/1724375',
             'https://apkdk.kaiten.ru/space/20752/card/4855532']
    Window = Tk()
    Window['bg'] = "#555"
    Window.title("СФО")
    Window.geometry('1080x720')
    Input = Text(width=50, height=35, background="#fafafa")
    Output = Text(width=50, height=35, background="#fafafa")
    Make = Button(text="Создать отчет", background="#fafafa", command=make_plan,)
    Clear = Button(text="Очистить", background="#fafafa", command=clear_text, )
    Input.place(x=100, y=20)
    Output.place(x=600, y=20)
    Make.place(x=300, y=600, height=40, width=500)
    Clear.place(x=300, y=650, height=40, width=500)


    Window.mainloop()

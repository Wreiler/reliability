from tkinter import *
from tkinter.ttk import Radiobutton, Style
from PIL import ImageTk, Image
from turtle import RawTurtle, TurtleScreen
import ctypes

# Для вывода иконки в панель задач
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Вопросы
phrases = [['Тип заряжания', '1 - раздельно-гильзовое', '2 - унитарное', '3 - картузное'],
           ['Калибр', '1 - малый', '2 - средний', '3 - крупный'],
           ['Масса боеприпаса', '1 - до 50 кг', '2 - больше 50 кг'],
           ['Расположение боеукладки', '1 - в корпусе', '2 - в башне'],
           ['Тип крепления в боеукладке', '1 - барашковое крепление', '2 - лирочное крепление',
            '3 - хомутовое крепление', '4 - стеллажная немеханизированная укладка', '5 - стопорное крепление'],
           ['Способ подачи на линию досылания', '1 - элеватор', '2 - перегружатель', '3 - механизм заряжания'],
           ['Тип досылателя', '1 - пружинный штоковый досылатель', '2 - гидропневматический штоковый досылатель',
            '3 - электромеханический цепной досылатель', '4 - роликовый досылатель']]

# Коэффициенты
consts = [{1: 0.969, 2: 0.978, 3: 0.995},
          {1: 0.996, 2: 0.997, 3: 0.998},
          {1: 0.998, 2: 0.997},
          {1: 0.988, 2: 0.988},
          {1: 0.987, 2: 0.969, 3: 0.959, 4: 0.984, 5: 0.996},
          {1: 0.987, 2: 0.978, 3: 0.985},
          {1: 0.991, 2: 0.983, 3: 0.989, 4: 0.979}]

# Картинки
pics = [{1: '1_1', 2: '1_2', 3: '1_3'},
        {},
        {},
        {1: '4_1', 2: '4_2'},
        {1: '5_1', 2: '5_2', 3: '5_3', 4: '5_4', 5: '5_5'},
        {1: '6_1', 2: '6_2', 3: '6_3'},
        {1: '7_1', 2: '7_2', 3: '7_3', 4: '7_4'},
        {1: '8_1', 2: '8_2', 3: '8_3', 4: '8_4', 5: '8_5'},
        {1: '9_1', 2: '9_2', 3: '9_3'},
        {1: '10_1', 2: '10_2', 3: '10_3', 4: '10_4'}]

# Функции для схемы
moves = {4: {1: 'right()', 2: 'right()'},
         6: {1: 'up()', 2: 'arc()', 3: 'right()'},
         7: {1: 'right()', 2: 'right()', 3: 'right()', 4: 'right()', 5: 'right()'},
         9: {1: 'up()', 2: 'arc()', 3: 'right()'},
         10: {1: 'right()', 2: 'right()', 3: 'right()', 4: 'right()', 5: 'right()'}}

oboz = 'BCDEFGH'

# Предельное значение
lim = 0.98

results = []

# Вывод основного окна программы
window = Tk()
window.title("Расчет надежности системы")
window.iconphoto(False, PhotoImage(file=r'images\icon3.png'))
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
xax = w//2 + 70 if w < 1920 else 900
yax = h//2 + 250 if h < 1080 else 750
window.geometry(f'{xax}x{yax}')
window.resizable(0, 0)


def right():
    """Движение вправо на схеме"""
    global oboz
    turtle.forward(let)
    turtle.dot(5, 'black')
    turtle.write(oboz[0])
    oboz = oboz[1:]


def up():
    """Движение вверх на схеме"""
    global oboz, yax
    turtle.left(90)
    turtle.forward(int(yax*0.09))
    turtle.right(90)
    turtle.dot(5, 'black')
    turtle.write(oboz[0])
    oboz = oboz[1:]


def arc():
    """Движение по дуге на схеме"""
    global oboz
    turtle.circle(let//2, 90)
    turtle.right(90)
    turtle.dot(5, 'black')
    turtle.write(oboz[0])
    oboz = oboz[1:]


def draw(ans):
    """Вывод топологической схемы"""
    global xax, moves, oboz, window

    turx, tury = xax - int(xax*0.3), int(yax*0.25)
    bg_def = window.cget('bg')
    canvas = Canvas(window, relief='sunken', borderwidth=5, width=turx, height=tury, background=bg_def)
    canvas.place(relx=0.5, rely=0.1, y=int(yax*0.19), anchor=CENTER)
    screen = TurtleScreen(canvas)
    global turtle
    turtle = RawTurtle(canvas)

    turtle.speed(5)
    turtle.hideturtle()

    allen = (turx - int(xax*0.2))
    global let
    if len(ans) > 7:
        if ans[5] == 1 and ans[8] == 1:
            let = allen // 3
        else:
            if ans[5] == 1:
                let = allen // 4
            elif ans[8] == 1:
                let = allen // 4
            else:
                let = allen // 5
        if ans[5] == 2:
            allen -= let//2
        if ans[8] == 2:
            allen -= let//2

    else:
        if ans[5] == 1:
            let = allen // 2
        else:
            let = allen // 3
        if ans[5] == 2:
            allen -= let//2

    turtle.color('white')
    turtle.up()
    turtle.goto(x=-allen // 2, y=-int(yax*0.09))
    turtle.down()
    turtle.color('black')
    turtle.dot(5, 'black')
    turtle.write('A')

    for i in [moves[k + 1][x] for k, x in enumerate(ans) if k + 1 in moves]:
        print(i)
        eval(i)


def visual(r):
    """Отображение всех вопросов с 2 по 7 (10)"""
    global ans
    ques = Label(window, text=phrases[r][0], font=("Helvetica", int(yax*0.0345)+2, 'italic'))
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    ans = phrases[r][1:]

    if r not in (1, 2):
        selected = IntVar()
        buts = []
        for i in range(len(ans)):
            buts.append(Radiobutton(window, text=ans[i], value=i+1, variable=selected))

        for k in range(len(buts)):
            buts[k].place(relx=0.5, rely=0.2, y=int(yax*0.2)+(int(yax*0.07)*k+1), width=int(xax*0.55), anchor=CENTER)

        return selected

    else:
        if r == 1:
            Label(window, text='Введите калибр системы (мм):', font=("Helvetica", int(yax * 0.0205))).place(relx=0.5, rely=0.4, anchor=CENTER)
        else:
            Label(window, text='Введите массу боеприпаса системы (кг):', font=("Helvetica", int(yax * 0.0205))).place(relx=0.5, rely=0.4, anchor=CENTER)
        txt = Entry(window, width=int(xax*0.05), font=("Arial", int(yax * 0.018)))
        txt.place(relx=0.5, rely=0.2, y=int(yax*0.2)+(int(yax*0.07)), width=int(xax*0.15), height=int(xax*0.03), anchor=CENTER)

        return txt


data = []


def define(all_choices):
    """Результаты: расчет надежности, вывод схемы и рисунков"""
    global consts, lim, pics, data, xax, yax

    # Надпись "Результаты"
    Label(window, text='РЕЗУЛЬТАТЫ', font=("Helvetica", int(yax*0.045), 'italic')).place(relx=0.5, rely=0.1, y=-int(yax*0.06), anchor=CENTER)

    # Расчет надежности и вывод результатов
    pap = Label(window)
    pap.place(relx=0.5, rely=0.5, y=int(yax*0.418), anchor=CENTER)
    num = round(sum([consts[i][x] for i, x in enumerate(all_choices)])/len(all_choices), 3)
    pap.configure(text=f'Вероятность безотказной работы: {num}', font=("Arial Bold", int(yax*0.0218), 'bold'))

    # Топологическая схема
    Label(window, text='Топологическая схема:', font=("Helvetica", int(yax*0.0196), 'italic underline')).place(relx=0.5, rely=0.1, y=int(yax*0.0118), anchor=CENTER)
    draw(all_choices)

    # Вывод картинок выбранных элеменотов
    images = [pics[i][x] for i, x in enumerate(all_choices) if i not in [1, 2]]
    print(images)
    Label(window, text='Выбранные элементы схемы:', font=("Helvetica", int(yax*0.0196), 'italic underline')).place(relx=0.5, rely=0.2, y=int(yax*0.245), anchor=CENTER)
    frame = Canvas(width=xax, height=int(yax*0.176))
    frame.place(relx=0.5, rely=0.2, y=int(yax*0.351), anchor=CENTER)

    col = len(images)
    if col == 5:
        size = int(yax*0.647)//col
        exc = -(col // 2) * (size + size // 4)
    else:
        size = int(yax*0.847)//col
        exc = -((col//2) * (size + size // 4)) + size//2 + size//8

    for i in range(col):
        global begin, code, path
        path = rf'images\{images[i]}.jpg'
        begin = Image.open(path).resize((size, size), Image.ANTIALIAS)
        code = ImageTk.PhotoImage(begin)
        data.append(code)

    # Подписи к картинкам
    max_len = 0
    text_el = {}
    patern = 'абвгдежз'
    for i in range(len(data)):
        Label(frame, image=data[i]).place(x=exc, relx=0.5, rely=0.5, anchor=CENTER)
        paper = f'"{phrases[int(images[i][0]) - 1][0]}" - {phrases[int(images[i][:-2]) - 1][int(images[i][-1])][4:]}'
        if len(paper) > max_len:
            max_len = len(paper)
        idx = patern[0]
        text_el[idx] = paper
        Label(frame, text=idx, font=("Helvetica", int(yax*0.013), 'italic')).place(x=exc, relx=0.5, rely=0.9, y=int(yax*0.0067), anchor=CENTER)
        patern = patern[1:]
        exc += (size + size//4)

    # Расшифровка подписей
    bg_def = window.cget('bg')
    blok = Canvas(relief='flat', width=int(xax*0.1), height=int(yax*0.0118))
    blok.place(relx=0.5, rely=0.5, y=int(yax*0.25), anchor=CENTER)
    text = Text(blok, relief='flat', width=max_len+3, height=col, bg=bg_def, font=("Helvetica", int(yax*0.0127), 'italic'))
    text.pack()
    k = 1.0
    for i, x in text_el.items():
        text.insert(k, f'{i}) {x}\n')
        k += 1.1
    text.configure(state=DISABLED)


# Вывод первого вопроса
beg = 0
res = visual(beg)


def ret():
    """Возвращение назад к предыдущему вопросу (можно вернуться хоть в самое начало)"""
    global beg, res, results, phrases, consts, egg

    if len(results) == 1:
        if results[0] == 1:
            phrases = phrases[:-3]
            consts = consts[:-3]
        for w in window.winfo_children():
            w.destroy()
        btn = Button(window, text="Подтвердить", font=("Arial Bold", int(yax*0.0198)), command=clicked)
        btn.place(relx=0.5, rely=0.2, y=int(yax*0.65), anchor=CENTER)
        egg = Button(window, text='КУПОЛ', font=("Helvetica", 7, 'italic'), fg='#FFFFFF', relief='flat', command=kupolizm)
        egg.place(relx=0.0425, rely=0.5, y=int(yax * 0.47), anchor=CENTER)
    else:
        for w in window.winfo_children():
            if w.winfo_class() != 'Button':
                w.destroy()
        back = Button(window, text="Назад", font=("Arial", int(yax*0.0172)), command=ret)
        back.place(relx=0.5, rely=0.3, y=int(yax*0.623), anchor=CENTER)
    results = results[:-1]
    beg -= 1
    res = visual(beg)


def clicked():
    """Принятие выбора и очистка окна от наполнения бездействие (если ничего не выбрано)"""
    global beg, res, results, phrases, consts, egg
    if res.get() != 0 and res.get() != '':
        print(f'Выбранный вариант: {res.get()}')
        if isinstance(res.get(), str) == True:
            paper = res.get()
            if ',' in paper:
                paper = paper.replace(',', '.')
            paper = float(paper)
            if len(results) == 1:
                if 30 < paper < 75:
                    paper = 1
                elif 76 < paper < 152.4:
                    paper = 2
                else:
                    paper = 3
            else:
                if paper < 10:
                    paper = 1
                else:
                    paper = 2
        else:
            paper = res.get()
        results.append(paper)
        if len(results) == 1:
            if results[0] == 1:
                phrases += [
                    ['Тип крепления заряда', '1 - барашковое крепление', '2 - лирочное крепление',
                     '3 - хомутовое крепление', '4 - стеллажная немеханизированная укладка', '5 - стопорное крепление'],
                    ['Способ подачи заряда на линию досылания', '1 - элеватор', '2 - перегружатель',
                     '3 - механизм заряжания'],
                    ['Тип досылателя заряда', '1 - пружинный штоковый досылатель',
                     '2 - гидропневматический штоковый досылатель', '3 - электромеханический цепной досылатель',
                     '4 - роликовый досылатель']]
                consts += [{1: 0.987, 2: 0.969, 3: 0.959, 4: 0.984, 5: 0.996},
                           {1: 0.987, 2: 0.978, 3: 0.985},
                           {1: 0.991, 2: 0.983, 3: 0.989, 4: 0.979}]
        if len(results) >= 1:
            egg.destroy()
        for w in window.winfo_children():
            if w.winfo_class() != 'Button':
                w.destroy()
        back = Button(window, text="Назад", font=("Arial", int(yax*0.0172)), command=ret)
        back.place(relx=0.5, rely=0.3, y=int(yax*0.623), anchor=CENTER)
        if beg != len(phrases)-1:
            beg += 1
            res = visual(beg)
        else:
            for w in window.winfo_children():
                w.destroy()
            print(results)
            define(results)
    else:
        pass


def kupolizm():
    """Поймет только группа Е152"""
    global ans
    zam = 'КУПОЛ'

    photo = PhotoImage(file=r'images\Background.png')
    l = Label(window, image=photo)
    l.pack(side='top', fill='both', expand='yes')
    l.image = photo

    Button(window, text=zam, font=("Arial Bold", int(yax*0.0198)), command=clicked).place(relx=0.5, rely=0.2, y=int(yax*0.7), anchor=CENTER)
    Label(window, text=zam, font=("Helvetica", int(yax*0.0235), 'italic')).place(relx=0.5, rely=0.2, anchor=CENTER)

    window.title(zam)

    selected = IntVar()
    buts = []
    for i in range(len(ans)):
        buts.append(Radiobutton(window, text=zam, value=i + 1, variable=selected))

    for k in range(len(buts)):
        buts[k].place(relx=0.5, rely=0.2, y=int(yax*0.2) + (int(yax*0.08) * k + 1), width=int(yax*0.47), anchor=CENTER)

    egg.destroy()


# Шрифт для кнопок выбора ответа
style = Style(window)
style.configure("TRadiobutton", font=("Arial", int(yax*0.0175)))

# Кнопка "Подтвердить"
btn = Button(window, text="Подтвердить", font=("Arial Bold", int(yax*0.0188)), command=clicked)
btn.place(relx=0.5, rely=0.2, y=int(yax*0.65), anchor=CENTER)

# Секрет
egg = Button(window, text='КУПОЛ', font=("Helvetica", 5, 'italic'), fg='#FFFFFF', relief='flat', command=kupolizm)
egg.place(relx=0.0425, rely=0.5, y=int(yax*0.47), anchor=CENTER)

# Удержание окна программы открытым
window.mainloop()

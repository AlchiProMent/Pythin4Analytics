# программа в стиле GUI
import tkinter as gui
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from const import *

def exit_click():
    # обработчик выбора пункта ВЫХОД
    win.quit()

def new_click():
    # обработчик выбора пункта меню НОВЫЙ
    # очистить редактор
    editor.delete(1.0, gui.END)

def open_click():
    # обработчик выбора пункта меню ОТКРЫТЬ
    file = filedialog.askopenfile(filetypes=( ('Python файл','*.py'),
                                              ('Текстовый файл','*.txt'),
                                              ('Все файлы','*.*') ))
    # в заголовок имя файла
    win.title(file.name)
    # очистить редактор
    new_click()
    # загрузить текст из файла в редактор
    editor.insert(gui.END, file.read().encode('cp1251').decode())

def save_click():
    # обработчик выбора пункта меню СОХРАНИТЬ
    filedialog.asksaveasfilename()

# создать главное окно программы
win = gui.Tk()

# задать размеры окна
win.geometry(INIT_WIN_SIZE)
# задать заголовок
win.title(MAIN_TITLE)

# создать систкему меню
main_menu = gui.Menu(win)
# создать первую группу
file_item = gui.Menu(main_menu)

# пункты первой группы меню
file_item.add_command(label=FILE_NEW,command=new_click)
file_item.add_command(label=FILE_OPEN,command=open_click)
file_item.add_command(label=FILE_SAVE,command=save_click)
# разделитель
file_item.add_separator()
file_item.add_command(label=FILE_EXIT, command=exit_click)
# подключить группу к главному меню
main_menu.add_cascade(label=MAIN_ITEM_FILE,menu=file_item)
# подключить меню к окну
win.config(menu=main_menu)

# разместить в окне редактор текста
editor = scrolledtext.ScrolledText(win, font=FONT_SIZE, wrap=gui.WORD)
editor.pack(expand=True, fill=gui.BOTH)

# запустить окно (программу)
win.mainloop()




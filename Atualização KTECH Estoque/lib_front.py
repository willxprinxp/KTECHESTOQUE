import openpyxl as opx
import tkinter as tk
from tkinter import*
import tkinter.filedialog as tkfiledialog

class ConfigScreen():


    def __init__(self, title, bg):
        self.window = Tk()
        self.window.resizable()
        self.window.title(title)
        self.bg = self.window.configure(bg=bg)

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_height}')

        self.button = None
        # self.wtwd = None

        #Talvez self.var_stock e var_do tenham que estar em lib_back.py
        self.var_stock = None
        self.var_do = None

    def start_screen (self):
        self.window.mainloop()
    

class Screen(ConfigScreen):


    def __init__(self, )


    def create_frame(self, wtwd=None, bg=None):
        frame = Frame(self.wtwd, bg=bg)
        return frame
        '''wtwd is (what window?)'''


    
    def create_button(self, text, bg, command):
        button = tk.Button(self.window, text=text, bg=bg, command=command)
        return button


    def create_cbox(self, wtwd, values=None):
        cbox = ttk.Combobox(self.wtwd, values=values)
        return cbox
    

    def create_radbton(self, wtwd, text, bg, variable=None, value=None):
        radbton = tk.Radiobutton(self.wtwd, text=text, bg=bg, variable=variable, value=value)
        return radbton

    def var_do(self, valueINT):
        self.var_do = tk.IntVar(value=valueINT)
        return self.var_do

    def var_stock(self, valueSTR):
        self.var_stock = tk.StringVar(value=valueSTR)
        return self.var_stock
        



    # def create_label(self, wtwd, text, bg= None, fg= None, ):



    def to_add(self, what, width, height, x= None, y= None, relx= None, rely= None, anchor= None):
        what.place(width=width, height=height, x=x, y=y, relx=relx, rely=rely, anchor=anchor)
        '''anchor é bugado mas 'center' funciona'''



    def create_new_window_button(self, wtwd, text, bg):
        return self.create_button(wtwd, text, bg, command=lambda: self.new_window(text))



    def button_clicked(self, text):
        return print(text)

    


# Arrumar função antes de usar-la pois ela só pode ser criada e não tem como adicionar nada na janela.
    def new_window(self, title):
        '''deve ser passada para um botão'''
        '''must be assigned to a button'''
        younger_window = tk.Toplevel(self.window)
        younger_window.transient(self.window)
        younger_window.title(title)
        return younger_window
'''Caso seja preciso criar uma tela secundária maior, dar uma olhada no exemplo
 do pyCharm sobre agencias para criar uma classe ao invés de uma função'''

# ^
# |
# |

'''Será preciso pois não consigo adicionar coisas dentro de uma Toplevel'''


# class 
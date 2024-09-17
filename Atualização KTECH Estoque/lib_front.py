import openpyxl as opx
import tkinter as tk
from tkinter import*
import tkinter.filedialog as tkfiledialog


class Screen():


    def __init__(self, screen_conf):
        self.screen_conf = screen_conf
        self.window = self.screen_conf.window


    def create_frame(self, bg=None):
        frame = Frame(self.window, bg=bg)
        return frame


    
    def create_button(self, text, bg, command):
        button = tk.Button(self.window, text=text, bg=bg, command=command)
        return button


    def create_cbox(self, values=None):
        cbox = ttk.Combobox(self.window, values=values)
        return cbox
    

    def create_entry(self,
     text,
      bg=None,
       bd=None,
        font=None,
         fg=None,
          justify=None,
           relief=None,
            show=None):

        return tk.Entry(self.window,
        text=text,
         bg=bg,
          bd=bd,
           font=font,
            fg=fg,
             justify=justify,
              relief=relief,
               show=show)
        


    def create_radbton(self, text, bg, variable=None, value=None):
        radbton = tk.Radiobutton(self.window, text=text, bg=bg, variable=variable, value=value)
        return radbton

    def var_do(self, valueINT):
        self.var_do = tk.IntVar(value=valueINT)
        return self.var_do

    def var_stock(self, valueSTR):
        self.var_stock = tk.StringVar(value=valueSTR)
        return self.var_stock
        


    def create_label(self,
                 text, 
                 bg,
                 anchor=None,       
                 height=None,              
                 width=None,              
                 bd=None,                  
                 font=None, 
                 cursor=None,             
                 padx=None,               
                 pady=None,                
                 justify=None,    
                 relief=None,     
                 underline=None,           
                 wraplength=None):

        return tk.Label(self.window,
         text=text,
          bg=bg,
           fg=self.screen_conf.bg,
            anchor=anchor,
             height=height,
              width=width,
               bd=bd,
                font=font,
                 cursor=cursor,
                  padx=padx,
                   pady=pady,
                    justify=justify,
                     relief=relief,
                      underline=underline,
                       wraplength=wraplength)



    def to_add(self, what, width, height, x= None, y= None, relx= None, rely= None, anchor= None):
        what.place(width=width, height=height, x=x, y=y, relx=relx, rely=rely, anchor=anchor)
        '''anchor é bugado mas 'center' funciona'''




    # for test
    def button_clicked(self, text):
        return lambda: print(text) #colocar lambda antes dos comandos que não precisam ser iniciados automaticamente
        

    

# Arrumar função antes de usar-la pois ela só pode ser criada e não tem como adicionar nada na janela.
    '''def new_window(self, title):
        deve ser passada para um botão
        must be assigned to a button
        younger_window = tk.Toplevel(self.window)
        younger_window.transient(self.window)
        younger_window.title(title)
        return younger_window'''





class ConfigScreen(Screen):


    def __init__(self, title, bg, width=None, height=None):
        self.window = None
        self.bg = bg
        self.title = title
        self.screen_width = width
        self.screen_height = height

    def create_window(self):
        if self.window is None or not self.window.winfo_exists():

            self.window = Tk()
            self.window.resizable()
            self.window.title(self.title)
            self.window.configure(bg=self.bg)
            if self.screen_width and self.screen_height != None:
                self.window.geometry(f'{self.screen_width}x{self.screen_height}')
            
            # Criar uma lógica onde a tela abra no centro da tela!!

            else:
                self.config_screen_width = self.window.winfo_screenwidth()
                self.config_screen_height = self.window.winfo_screenheight()
                self.screen_width = self.config_screen_width
                self.screen_height = self.config_screen_height
                self.window.geometry(f'{self.screen_width}x{self.screen_height}')

            #Talvez self.var_stock e var_do tenham que estar em lib_back.py
            self.var_stock = None
            self.var_do = None

        

    def cmd_new_window(self):
        return lambda: self.create_window()

    def init_window(self):
        if self.window is not None:
            self.window.mainloop()

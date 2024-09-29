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
            show=None,
             width=None):

        return tk.Entry(self.window,
        text=text,
         bg=bg,
          bd=bd,
           font=font,
            fg=fg,
             justify=justify,
              relief=relief,
               show=show,
                width=width)
        


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
                 fg,
                 bg=None,
                 anchor=None,       
                 width=None,              
                 height=None,              
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
          fg=fg,
           bg=bg,
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



    def to_add(self, what, **kwargs):
        what.place(**kwargs)



    # for test
    def button_clicked(self, text):
        return lambda: print(text) #colocar lambda antes dos comandos que não precisam ser iniciados automaticamente
        
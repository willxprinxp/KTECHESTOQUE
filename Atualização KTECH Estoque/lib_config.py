import os
from lib_front import*


class ConfigScreen(Screen):


    def __init__(self, title, bg, width=None, height=None, icon=None):
        self.window = None
        self.bg = bg
        self.title = title
        self.screen_width = width
        self.screen_height = height

    def create_window(self):
        if self.window is None or not self.window.winfo_exists():
            self.window = tk.Tk()
            self.window.title(self.title)
            self.window.configure(bg=self.bg)

            self.config_screen_width = self.window.winfo_screenwidth()
            self.config_screen_height = self.window.winfo_screenheight()

            if self.screen_width is not None and self.screen_height is not None:
                self.w = (self.config_screen_width//2) - (self.screen_width//2)
                self.h = (self.config_screen_height//2) - (self.screen_height//2)
                self.window.geometry(f'{self.screen_width}x{self.screen_height}+{self.w}+{self.h}')

                self.window.resizable(False, False)
            else:
                self.screen_width = self.config_screen_width
                self.screen_height = self.config_screen_height
                self.window.geometry(f'{self.screen_width}x{self.screen_height}')

            #icon of window
            self.icon = os.path.join(os.path.dirname(__file__),'images','Amasia.ico')
            self.window.iconbitmap(self.icon)

            #Talvez self.var_stock e var_do tenham que estar em lib_back.py
            self.var_stock = None
            self.var_do = None

        

    def cmd_new_window(self):
        return lambda: self.create_window()

    def init_window(self):
        if self.window is not None:
            self.window.mainloop()

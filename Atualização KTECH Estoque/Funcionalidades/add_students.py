from base_screen import BaseScreen

class AddStudents():
    def __init__(self):
        self.screen = BaseScreen('Window_Base_Test', None, None)
        
        self.button = self.screen.front.create_button('Button', command=self.screen.screen.button_clicked('Funciona!'))
        self.screen.screen.to_add(self.button, x=2, y=5)
        
        self.screen.screen.init_window()
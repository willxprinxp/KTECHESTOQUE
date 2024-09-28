from lib_front import*
from lib_config import*



log_screen = ConfigScreen('Login - KTECH Estoque', 'lightblue', 500, 500)
log_screen.create_window()

front_log = Screen(log_screen)

title_log = front_log.create_label('Login Ktech Estoque', 'white')
log_screen.to_add(title_log, log_screen.screen_width, 20) 

input_test = front_log.create_entry('Teste', 'white')
log_screen.to_add(input_test, 50, 20, 50, 50)


log_screen.init_window()

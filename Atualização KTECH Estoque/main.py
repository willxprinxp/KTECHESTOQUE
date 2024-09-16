from lib_front import*

log_screen = ConfigScreen('Login - KTECH Estoque', 'lightblue', 100, 300)
log_screen.create_window()

front_log = Screen(log_screen)
title_log = front_log.create_label('Login Ktech Estoque', 'white')
# log_screen.to_add(title_log, )

log_screen.init_window()

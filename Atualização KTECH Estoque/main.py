from lib_front import*

log_screen = ConfigScreen('Login - KTECH Estoque', 'lightblue')
log_screen.modify_wh(100, 100)

front_log = Screen(log_screen)
title_log = front_log.create_label('Login Ktech Estoque', 'white')
# log_screen.to_add(title_log, )

log_screen.init_window()

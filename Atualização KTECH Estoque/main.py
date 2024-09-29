from lib_front import*
from lib_config import*


log_screen = ConfigScreen('Login - KTECH Estoque', 'lightblue', 450, 350)
log_screen.create_window()

front_log = Screen(log_screen)

title_log = front_log.create_label('Login Ktech Estoque', log_screen.bg, 'white')
log_screen.to_add(title_log, width=log_screen.screen_width, height=25)

greeting_log = front_log.create_label('Bem-vindo(a)!', 'white', log_screen.bg, font=('Arial Black', 17))
log_screen.to_add(greeting_log, x=log_screen.screen_width/3.35, y=60)


label_user_log = front_log.create_label('User:', 'white', log_screen.bg, font=('Arial', 12, 'bold'))
log_screen.to_add(label_user_log, x=60, y=160)
user_input_log = front_log.create_entry('user', bg='white', fg='black', width=20, font=('Arial Black', 9, 'bold'))
log_screen.to_add(user_input_log, x=log_screen.screen_width/3.2, y=160)


label_password_log = front_log.create_label('Password:', 'white', log_screen.bg, font=('Arial', 12, 'bold'))
log_screen.to_add(label_password_log, x=43, y=220)
password_input_log = front_log.create_entry('password', bg='white', fg='black', width=20, font=('Arial Black', 9, 'bold'), show='*')
log_screen.to_add(password_input_log, x=log_screen.screen_width/3.2, y=220)


label_unit_log = front_log.create_label('Unit:', 'white', log_screen.bg, font=('Arial', 12, 'bold'))
log_screen.to_add(label_unit_log, x=63, y=300)
wait_unit = front_log.create_label('', 'black', 'white', font=('Arial', 12, 'bold'), width=20)
log_screen.to_add(wait_unit, x=log_screen.screen_width/3.2, y=300)


log_screen.init_window()
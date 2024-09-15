from lib_front import*

init_screen = ConfigScreen('Janela teste', 'lightblue')
init_screen.create_window()

log_screen = ConfigScreen('Log Teste', 'lightblue')

screen_front = Screen(init_screen)

label_test = screen_front.create_label('KTECHESTOQUE', 'white')
init_screen.to_add(label_test, init_screen.screen_width, 25)

button_test = screen_front.create_button('New Button', 'red', log_screen.new_window())
init_screen.to_add(button_test, 100, 100)

init_screen.init_window()
from lib_front import*

init_screen = ConfigScreen('Janela teste', 'lightblue')
# log_screen = ConfigScreen('Log Teste', 'lightblue')

screen_front = Screen(init_screen)

label_test = screen_front.create_label('KTECHESTOQUE', 'white')
# screen_front.to_add(label_test, init_screen.screen_width, 25)

# button_test = screen_front.create_button('New Button', 'red', log_screen.create_and_init_window())
# screen_front.to_add(button_test, 100, 100)

init_screen.create_and_init_window()


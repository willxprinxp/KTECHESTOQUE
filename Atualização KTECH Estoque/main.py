from lib_front import*

init_screen = ConfigScreen('Janela teste', 'lightblue')

screen_front = Screen(init_screen)


button_test = screen_front.create_button('New Button', 'red',
 screen_front.button_clicked('clicooooooooooooooou'))
init_screen.to_add(button_test, 100, 100)

label_test = screen_front.create_label('KTECHESTOQUE', 'white')
screen_front.to_add(label_test, init_screen.screen_width, 25)

init_screen.start_screen()

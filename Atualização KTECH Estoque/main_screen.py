from lib_front import*
from lib_config import*
from lib_back import*


main_screen = ConfigScreen('KTECH Estoque', 'white')
main_screen.create_window()

front_main = Screen(main_screen)


title_main = front_main.create_label('Ktech Estoque', main_screen.bg, 'lightblue')
main_screen.to_add(title_main, width=main_screen.screen_width, height=25)


sidebar_main = front_main.create_frame(bg='lightblue')
main_screen.to_add(sidebar_main, height=main_screen.screen_height, width=35)

icon_user = front_main.to_icon(r'.venv\images\Usuario.png', (25,25))
user_button = front_main.create_button('', image=icon_user, bg='lightblue', relief='flat', activebackground='lightblue', command=main_screen.button_clicked('Ícone Clicado'))
main_screen.to_add(user_button, x=2, y=main_screen.screen_height-100)


bloco_prod = front_main.create_button('Pesquisa de Blocos', bg='lightblue', fg='white', command=front_main.button_clicked('Botão Clicado'))
main_screen.to_add(bloco_prod, x=100, y=100)

main_screen.init_window()
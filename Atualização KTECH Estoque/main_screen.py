from lib_front import*
from lib_config import*
from lib_back import*


main_screen = ConfigScreen('KTECH Estoque', 'white')
main_screen.create_window()

front_main = Screen(main_screen)


title_main = front_main.create_label('Ktech Estoque', main_screen.bg, 'lightblue')
main_screen.to_add(title_main, width=main_screen.screen_width, height=25)


bloco_prod = front_main.create_button('Pesquisa de Blocos', bg='lightblue', fg='white')
main_screen.to_add(bloco_prod, x=100, y=100)

main_screen.init_window()
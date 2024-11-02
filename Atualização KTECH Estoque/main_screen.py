from lib_front import*
from lib_config import*
from lib_back import*
from base_screen import BaseScreen
from Funcionalidades.add_students import AddStudents

class Main:
    def __init__(self):
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


        icon_general_search = front_main.to_icon(r'.venv\images\lupa.png', (22,22))
        general_search_button = front_main.create_button('', image=icon_general_search, bg='lightblue',
        relief='flat',
        activebackground='lightblue',
        command=main_screen.button_clicked('Pesquisa Clicado'))
            #Para general_search, em sua função. Será Criada uma function que é alimentada pelo input do user. O objeto ativado pode ser decidido depois do adicionamento de funcionalidades.
            #O objeto será possívelmente uma Combobox. Pelos objetos em tela (Pesquisa Geral será uma subtela/tela sec)
        main_screen.to_add(general_search_button, x=3, y=main_screen.screen_height-743.5)


        bloco_prod = front_main.create_button('Pesquisa de Blocos', bg='lightblue', fg='white', command=front_main.button_clicked('Botão Clicado'))
        main_screen.to_add(bloco_prod, x=100, y=100)
        #Dentro da Pesquisa de Blocos, será permitido 5 blocos de retirada e 5 de transferências locais rápidas. Para mais será necessário modificações em suas funções específicas.


        #ad for cadastro estudantes
        students_regs_button = front_main.create_button('Registro de Estudantes', bg='lightblue', fg='white', command=AddStudents)
        main_screen.to_add(students_regs_button, x=5, y=5)

        #ad for manipulação de inventário
        # inventory_button = front_main.create_button('Inventário', bg='lightblue', fg='white', command=)

        #ad for auditar inventário


        main_screen.init_window()
from lib_front import Screen
import time

init_screen = Screen('Ktech Estoque', bg='lightblue')
# frame_title = init_screen.create_frame(init_screen, 'white')   
# init_screen.to_add(frame_title, 1366, 50)


# Aqui está Ok, estava testando se o Radiobutton ia dar certo e deu.
# frame_button_test = init_screen.create_frame(init_screen, bg=init_screen.bg)
# init_screen.to_add(frame_button_test, 200, 200, 100, 100)
button_test = init_screen.create_button(text= 'Lingua Patria',bg='red', command=lambda: init_screen.button_clicked('Botão Clicado'))
init_screen.to_add(button_test, 200, 200, 100, 100)


init_screen.start_screen()
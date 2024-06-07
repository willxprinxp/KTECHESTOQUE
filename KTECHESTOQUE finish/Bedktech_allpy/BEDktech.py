import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import shutil

excel = pd.ExcelFile('Planilhas\KTECH_ESTOQUEPRIMESUB.xlsx')
todas_as_planilhas = {nome: excel.parse(nome) for nome in excel.sheet_names}

root = tk.Tk()
root.iconbitmap('icon\Amasia.ico')
root.title('KTECHESTOQUE')
root.configure(bg='lightblue')
root.columnconfigure([0, 1, 2], weight=1)
root.rowconfigure([1, 2], weight=1)

label_title = tk.Label(text='KTECHESTOQUE', bg='white', fg='lightblue')
label_title.grid(row=0, column=0, columnspan=3, sticky='NSWE')

label_estoque = tk.Label(text='Selecione o estoque que deseja MODIFICAR:', bg='lightblue')
label_estoque.grid(row=1, column=0, columnspan=3, sticky='NSWE', padx=10, pady=10)

estoques = ['Lingua Patria', 'Matematica', 'Ingles', 'Coord.Motora', 'B.Matricula']
var_estoque = tk.StringVar(value='vazio')
var_do = tk.IntVar(value=2)


button_lp = tk.Radiobutton(text='Lingua Pátria', bg='#FBF61A', variable=var_estoque, value='Lingua Pátria')
button_lp.grid(row=2, column=0, sticky='NSWE')
button_mt = tk.Radiobutton(text='Matemática', bg='#438FEB', variable=var_estoque, value='Matemática')
button_mt.grid(row=2, column=1, sticky='NSWE')
button_en = tk.Radiobutton(text='Inglês', bg='#FF1111', variable=var_estoque, value='Inglês')
button_en.grid(row=3, column=1, sticky='NSWE')
button_cm = tk.Radiobutton(text='Coord.Motora', bg='#0BAD1E', variable=var_estoque, value='Coord.Motora')
button_cm.grid(row=3, column=2, sticky='NSWE')
button_bm = tk.Radiobutton(text='B.Matrícula', bg='#021498', variable=var_estoque, value='B.Matrícula')
button_bm.grid(row=2, column=2, sticky='NSWE')

label_estagio = tk.Label(text='Estágio desejado: ', bg='lightblue')
label_estagio.grid(row=4, column=0, sticky='nsew')
estagio = tk.Entry(root)
estagio.grid(row=4, column=1, sticky='nsew', padx=10, pady=10)

label_bloco = tk.Label(text='Bloco da modificação: ', bg='lightblue')
label_bloco.grid(row=5, column=0, sticky='nsew', padx=10, pady=10)
blocos = ('1', '11', '21', '31', '41', '51', '61', '71', '81', '91', '101', '111', '121', '131', '141', '151', '161', '171', '181', '191', 'TXB')
bloco = ttk.Combobox(root, values=blocos)
bloco.grid(row=5, column=1, padx=10, pady=10)

label_qtde = tk.Label(text='Quantidade:', bg='lightblue')
label_qtde.grid(row=6, column=2, sticky='NSWE')
quantidade = tk.Entry(root)
quantidade.grid(row=7, column=2, sticky='nsew', padx=10, pady=10)

label_do = tk.Label(text='Você deseja:', bg='lightblue')
label_do.grid(row=6, column=0, sticky='nswe', padx=10)
adicionar = tk.Radiobutton(text='ADICIONAR', bg='RED', variable=var_do, value='0')
adicionar.grid(row=7, column=0, sticky='NSWE', padx=10, pady=5)
retirar = tk.Radiobutton(text='RETIRAR', bg='BLUE', variable=var_do, value='1')
retirar.grid(row=8, column=0, sticky='NSWE', padx=10, pady=5)

mensagem_final = tk.Label(text='Nada foi modificado ainda..')
mensagem_final.grid(row=7, column=1, sticky='nsew', padx=10, pady=10)
mensagem_end2 = tk.Label(text='')
mensagem_end2.grid(row=8, column=1, sticky='nsew', padx=10, pady=10)

mapeamento_blocos = {bloco: indice for indice, bloco in enumerate(blocos)}


def ler_coluna(planilha, coluna):
    dados_planilha = pd.read_excel('Planilhas\KTECH_ESTOQUEPRIMESUB.xlsx', sheet_name=planilha)
    return dados_planilha[coluna]


def ler_determinada_linha(planilha, coluna, indice_associado):
    dados_coluna = ler_coluna(planilha, coluna)

    # Verifica se a série não está vazia e se o valor é NaN
    if not dados_coluna.empty and pd.isna(dados_coluna.iloc[indice_associado]):
        novo_valor = 0
    else:
        novo_valor = int(dados_coluna.iloc[indice_associado])

    return novo_valor


def adicionar_valor(planilha, coluna, indice_associado):
    qtde = ler_determinada_linha(planilha, coluna, indice_associado)
    if pd.isna(qtde) or qtde >= 0:
        num = int(quantidade.get())
        novo_valor = qtde + num
    return novo_valor


def diminuir_valor(planilha, coluna, indice_associado):
    qtde = ler_determinada_linha(planilha, coluna, indice_associado)
    if pd.isna(qtde) or qtde <= 0:
        novo_valor = 0
        mensagem_end2.config(text="Não há bloquinhos!")

    else:
        num = int(quantidade.get())
        novo_valor = qtde - num

    return novo_valor


def escrever_valor(novo_valor, planilha, coluna, indice_associado):
    # Carrega o arquivo Excel
    arquivo = 'Planilhas\KTECH_ESTOQUEPRIMESUB.xlsx'

    # Lê a planilha específica do arquivo Excel
    dados = pd.read_excel(arquivo, sheet_name=planilha)

    # Atualiza o valor na célula específica (indice_associado na coluna 'ZI')
    dados.at[indice_associado, str(coluna)] = novo_valor

    # Salva as alterações na cópia temporária do arquivo Excel
    temp_arquivo = 'temp_KTECH_ESTOQUEPRIMESUB.xlsx'
    dados.to_excel(temp_arquivo, sheet_name=planilha, index=False, engine='openpyxl')

    # Copia as outras planilhas do arquivo original para o temporário
    with pd.ExcelWriter(temp_arquivo, engine='openpyxl', mode='a') as writer:
        for nome in pd.ExcelFile(arquivo).sheet_names:
            if nome != planilha:  # Pular a planilha atual
                dados_planilha = pd.read_excel(arquivo, sheet_name=nome)
                dados_planilha.to_excel(writer, sheet_name=nome, index=False)

    # Substitui o arquivo original pelo temporário
    shutil.move(temp_arquivo, arquivo)


def realizar_operacao_soma(planilha, coluna, mapeamento_blocos, indice_associado, bloco_procurado):
    resultado = ler_determinada_linha(planilha, coluna, indice_associado)
    novo_valor = adicionar_valor(planilha, coluna, indice_associado)
    mensagem_end2.config(text=f"Novo valor de {coluna} - {bloco_procurado}: {novo_valor}")
    return novo_valor


def realizar_operacao_subtracao(planilha, coluna, mapeamento_blocos, indice_associado, bloco_procurado):
    resultado = ler_determinada_linha(planilha, coluna, indice_associado)
    novo_valor = diminuir_valor(planilha, coluna, indice_associado)
    mensagem_end2.config(text=f"Novo valor de {coluna} - {bloco_procurado}: {novo_valor}")
    return novo_valor


def modificar():
    if var_estoque.get() != 'vazio':
        planilha = var_estoque.get()
        coluna = str(estagio.get()).upper()  # Convertendo para maiúsculas aqui
        bloco_procurado = bloco.get()
        indice_associado = mapeamento_blocos.get(bloco_procurado)

        if var_do.get() == 0:
            novo_valor = realizar_operacao_soma(planilha, coluna, mapeamento_blocos, indice_associado, bloco_procurado)
            escrever_valor(novo_valor, planilha, coluna, indice_associado)

        elif var_do.get() == 1:
            novo_valor = realizar_operacao_subtracao(planilha, coluna, mapeamento_blocos, indice_associado, bloco_procurado)
            escrever_valor(novo_valor, planilha, coluna, indice_associado)

        mensagem_final.config(text=f'{var_estoque.get()} modificado com sucesso!')
    else:
        mensagem_final.config(text='Nenhum estoque selecionado!')


botao_modificar = tk.Button(root, text='Modificar', command=modificar)
botao_modificar.grid(row=8, column=2, sticky='nswe', padx=10, pady=5)

root.mainloop()
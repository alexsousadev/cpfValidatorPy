import tkinter as tk
from tkinter import messagebox
from validador_cpf import verificar_cpf

def verificar_cpf_interface():
    cpf = entrada_cpf.get()
    resultado = verificar_cpf(cpf)
    messagebox.showinfo("Resultado", resultado)

# Cria a janela principal
janela = tk.Tk()
janela.title("Validador de CPF")

# Rótulo para o campo de entrada
rotulo_cpf = tk.Label(janela, text="Digite o CPF:")
rotulo_cpf.pack(pady=10)

# Campo de entrada para o CPF
entrada_cpf = tk.Entry(janela)
entrada_cpf.pack(pady=5)

# Botão para verificar o CPF
botao_verificar = tk.Button(janela, text="Verificar", command=verificar_cpf_interface)
botao_verificar.pack(pady=10)

# Inicia o loop principal do Tkinter
janela.mainloop()